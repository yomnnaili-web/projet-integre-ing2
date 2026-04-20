from django.core.management.base import BaseCommand
from core.models import Question, ChoixReponse, Domaine

class Command(BaseCommand):
    help = 'Initialise les questions du questionnaire'

    def handle(self, *args, **options):
        # Créer des domaines si nécessaire
        informatique, _ = Domaine.objects.get_or_create(
            nom='Informatique',
            defaults={'description': 'Technologies et développement'}
        )
        sante, _ = Domaine.objects.get_or_create(
            nom='Santé',
            defaults={'description': 'Secteur médical et paramédical'}
        )
        commerce, _ = Domaine.objects.get_or_create(
            nom='Commerce',
            defaults={'description': 'Vente et marketing'}
        )
        
        # Question 1
        q1, created = Question.objects.get_or_create(
            ordre=1,
            defaults={'texte': 'Quel type d\'activité vous intéresse le plus?'}
        )
        if created:
            ChoixReponse.objects.create(
                question=q1,
                texte='Travailler avec des ordinateurs et technologies',
                domaine=informatique
            )
            ChoixReponse.objects.create(
                question=q1,
                texte='Aider et soigner les gens',
                domaine=sante
            )
            ChoixReponse.objects.create(
                question=q1,
                texte='Vendre et convaincre',
                domaine=commerce
            )
        
        # Question 2
        q2, created = Question.objects.get_or_create(
            ordre=2,
            defaults={'texte': 'Dans quel environnement préférez-vous travailler?'}
        )
        if created:
            ChoixReponse.objects.create(
                question=q2,
                texte='Bureau avec ordinateur',
                domaine=informatique
            )
            ChoixReponse.objects.create(
                question=q2,
                texte='Hôpital ou cabinet médical',
                domaine=sante
            )
            ChoixReponse.objects.create(
                question=q2,
                texte='Magasin ou terrain',
                domaine=commerce
            )
        
        self.stdout.write(self.style.SUCCESS('Questions initialisées avec succès'))
