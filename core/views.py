from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from .models import Domaine, Metier, Question, ChoixReponse, ReponseUtilisateur

def home(request):
    domaines_count = Domaine.objects.count()
    metiers_count = Metier.objects.count()
    return render(request, 'home.html', {
        'domaines_count': domaines_count,
        'metiers_count': metiers_count
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def questionnaire(request):
    questions = Question.objects.prefetch_related('choix').all()
    
    if request.method == 'POST':
        ReponseUtilisateur.objects.filter(user=request.user).delete()
        
        for question in questions:
            choix_id = request.POST.get(f'question_{question.id}')
            if choix_id:
                choix = ChoixReponse.objects.get(id=choix_id)
                ReponseUtilisateur.objects.create(
                    user=request.user,
                    question=question,
                    choix=choix
                )
        return redirect('resultats')
    
    return render(request, 'questionnaire.html', {'questions': questions})

@login_required
def resultats(request):
    reponses = ReponseUtilisateur.objects.filter(user=request.user)
    domaines_scores = {}
    
    for reponse in reponses:
        domaine = reponse.choix.domaine
        domaines_scores[domaine] = domaines_scores.get(domaine, 0) + 1
    
    domaine_recommande = max(domaines_scores, key=domaines_scores.get) if domaines_scores else None
    
    return render(request, 'resultats.html', {
        'domaine_recommande': domaine_recommande,
        'domaines_scores': sorted(domaines_scores.items(), key=lambda x: x[1], reverse=True)
    })

def domaines_list(request):
    domaines = Domaine.objects.annotate(nb_metiers=Count('metiers'))
    return render(request, 'domaines.html', {'domaines': domaines})

def metiers_list(request, domaine_id=None):
    if domaine_id:
        domaine = get_object_or_404(Domaine, id=domaine_id)
        metiers = Metier.objects.filter(domaine=domaine)
    else:
        domaine = None
        metiers = Metier.objects.all()
    
    return render(request, 'metiers.html', {
        'domaine': domaine,
        'metiers': metiers
    })
