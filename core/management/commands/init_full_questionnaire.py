from django.core.management.base import BaseCommand
from core.models import Section, Question, ChoixReponse, Domaine

class Command(BaseCommand):
    help = 'Initialise le questionnaire complet d\'orientation'

    def handle(self, *args, **options):
        # Créer les domaines si nécessaire
        domaines = {
            'informatique': Domaine.objects.get_or_create(
                nom='Informatique & Technologies',
                defaults={'description': 'IT, développement, data science', 'icone': '💻', 'couleur': '#667eea'}
            )[0],
            'sante': Domaine.objects.get_or_create(
                nom='Santé & Médecine',
                defaults={'description': 'Médecine, soins, pharmacie', 'icone': '🏥', 'couleur': '#f093fb'}
            )[0],
            'commerce': Domaine.objects.get_or_create(
                nom='Commerce & Vente',
                defaults={'description': 'Business, vente, marketing', 'icone': '🛒', 'couleur': '#4facfe'}
            )[0],
            'ingenierie': Domaine.objects.get_or_create(
                nom='Ingénierie & Industrie',
                defaults={'description': 'Génie civil, mécanique', 'icone': '⚙️', 'couleur': '#fbc2eb'}
            )[0],
            'design': Domaine.objects.get_or_create(
                nom='Design & Arts Créatifs',
                defaults={'description': 'Design, graphisme, arts', 'icone': '🎨', 'couleur': '#a18cd1'}
            )[0],
        }
        
        # SECTION 1: EDUCATION
        section1, _ = Section.objects.get_or_create(nom='Education & Background', ordre=1)
        
        q1, _ = Question.objects.get_or_create(
            ordre=1,
            defaults={'texte': 'Do you have a Baccalauréat?', 'section': section1}
        )
        ChoixReponse.objects.get_or_create(question=q1, texte='Yes')
        ChoixReponse.objects.get_or_create(question=q1, texte='No (Still studying)')
        
        q2, _ = Question.objects.get_or_create(
            ordre=2,
            defaults={'texte': 'If yes, what is your Bac section?', 'section': section1}
        )
        ChoixReponse.objects.get_or_create(question=q2, texte='Sciences Math', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q2, texte='Sciences Expérimentales', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q2, texte='Sciences Techniques', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q2, texte='Sciences Informatique', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q2, texte='Economie & Gestion', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q2, texte='Lettres', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q2, texte='Other')
        
        q5, _ = Question.objects.get_or_create(
            ordre=5,
            defaults={'texte': 'What type of studies are/were you in?', 'section': section1}
        )
        ChoixReponse.objects.get_or_create(question=q5, texte='Engineering', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Medical / Health', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Business / Management', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q5, texte='IT / Computer Science', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Arts / Design', domaine=domaines['design'])
        
        # SECTION 2: PERSONALITY
        section2, _ = Section.objects.get_or_create(nom='Personality & Work Style', ordre=2)
        
        q8, _ = Question.objects.get_or_create(
            ordre=8,
            defaults={'texte': 'When facing a complex problem, you:', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q8, texte='Break it into logical steps', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q8, texte='Think creatively and imagine possibilities', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q8, texte='Ask others and collaborate', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q8, texte='Take action and adapt while moving', domaine=domaines['ingenierie'])
        
        q9, _ = Question.objects.get_or_create(
            ordre=9,
            defaults={'texte': 'In a group project, you usually:', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q9, texte='Take leadership', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q9, texte='Organize and structure', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q9, texte='Focus deeply on your part', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q9, texte='Motivate and support others', domaine=domaines['sante'])
        
        q11, _ = Question.objects.get_or_create(
            ordre=11,
            defaults={'texte': 'Which statement describes you best?', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q11, texte='I need structure and rules', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q11, texte='I need creative freedom', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q11, texte='I need purpose and meaning', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q11, texte='I need growth and achievement', domaine=domaines['commerce'])
        
        # SECTION 3: WORK ENVIRONMENT
        section3, _ = Section.objects.get_or_create(nom='Work Environment Preferences', ordre=3)
        
        q14, _ = Question.objects.get_or_create(
            ordre=14,
            defaults={'texte': 'You perform best in:', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q14, texte='Highly structured environments', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q14, texte='Fast-paced dynamic environments', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q14, texte='Calm stable environments', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q14, texte='Creative flexible environments', domaine=domaines['design'])
        
        q21, _ = Question.objects.get_or_create(
            ordre=21,
            defaults={'texte': 'What type of tasks make you proud?', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q21, texte='Solving technical problems', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Creating something original', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Helping someone succeed', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Achieving business targets', domaine=domaines['commerce'])
        
        q22, _ = Question.objects.get_or_create(
            ordre=22,
            defaults={'texte': 'If you could master one skill:', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q22, texte='Coding / Engineering', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q22, texte='Design / Art', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q22, texte='Psychology / Communication', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q22, texte='Business / Investment', domaine=domaines['commerce'])
        
        self.stdout.write(self.style.SUCCESS('Questionnaire complet initialisé avec succès!'))
