from django.db import models
from django.contrib.auth.models import User

class Domaine(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    icone = models.CharField(max_length=50, default='💼')  # Emoji ou classe d'icône
    couleur = models.CharField(max_length=7, default='#3498db')  # Code couleur hex
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']

class Metier(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    competences = models.TextField(blank=True)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name='metiers')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']

class Section(models.Model):
    nom = models.CharField(max_length=200)
    ordre = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['ordre']

class Question(models.Model):
    TYPE_CHOICES = [
        ('single', 'Choix unique'),
        ('multiple', 'Choix multiple'),
        ('text', 'Texte libre'),
    ]
    
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    texte = models.TextField()
    type_question = models.CharField(max_length=20, choices=TYPE_CHOICES, default='single')
    ordre = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Question {self.ordre}: {self.texte[:50]}"
    
    class Meta:
        ordering = ['ordre']

class ChoixReponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choix')
    texte = models.CharField(max_length=200)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, null=True, blank=True)
    points = models.IntegerField(default=0)  # Pour le scoring
    
    def __str__(self):
        return self.texte

class ReponseUtilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix = models.ForeignKey(ChoixReponse, on_delete=models.CASCADE, null=True, blank=True)
    texte_libre = models.TextField(blank=True, null=True)
    date_reponse = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'question']

class ProfilUtilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    score_total = models.IntegerField(default=0)
    domaines_recommandes = models.ManyToManyField(Domaine, blank=True)
    
    def __str__(self):
        return f"Profil de {self.user.username}"
