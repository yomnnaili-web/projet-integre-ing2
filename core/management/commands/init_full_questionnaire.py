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
        
        # Question 3: Bac average (no domain mapping in current model)
        q3, _ = Question.objects.get_or_create(
            ordre=3,
            defaults={'texte': 'What was your average score in Bac?', 'section': section1}
        )
        
        # Optional choices for score ranges (kept domain=None)
        ChoixReponse.objects.get_or_create(question=q3, texte='10–12')
        ChoixReponse.objects.get_or_create(question=q3, texte='12–14')
        ChoixReponse.objects.get_or_create(question=q3, texte='14–16')
        ChoixReponse.objects.get_or_create(question=q3, texte='16+')

        # Question 4: Current status (kept domain=None)
        q4, _ = Question.objects.get_or_create(
            ordre=4,
            defaults={'texte': 'Are you currently?', 'section': section1}
        )
        
        ChoixReponse.objects.get_or_create(question=q4, texte='High school student')
        ChoixReponse.objects.get_or_create(question=q4, texte='University student')
        ChoixReponse.objects.get_or_create(question=q4, texte='Graduated')
        ChoixReponse.objects.get_or_create(question=q4, texte='Stopped studying')

        # Question 5: Type of studies (domain mapping)
        q5, _ = Question.objects.get_or_create(
            ordre=5,
            defaults={'texte': 'What type of studies are/were you in?', 'section': section1}
        )
        ChoixReponse.objects.get_or_create(question=q5, texte='Engineering', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Medical / Health', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Business / Management', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q5, texte='IT / Computer Science', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Arts / Design', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Law', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q5, texte='Other')

        # Question 6: Future choice (kept domain=None)
        q6, _ = Question.objects.get_or_create(
            ordre=6,
            defaults={'texte': 'Do you want to?', 'section': section1}
        )
        ChoixReponse.objects.get_or_create(question=q6, texte='Continue in the same field')
        ChoixReponse.objects.get_or_create(question=q6, texte='Change to another field')
        ChoixReponse.objects.get_or_create(question=q6, texte='Not sure yet')

        # Question 7: Reason for change (kept domain=None)
        q7, _ = Question.objects.get_or_create(
            ordre=7,
            defaults={'texte': 'If you want to change field, why?', 'section': section1}
        )
        ChoixReponse.objects.get_or_create(question=q7, texte='Not passionate')
        ChoixReponse.objects.get_or_create(question=q7, texte='Too difficult')
        ChoixReponse.objects.get_or_create(question=q7, texte='Family pressure')
        ChoixReponse.objects.get_or_create(question=q7, texte='Better opportunities elsewhere')

        
        # SECTION 2: PERSONALITY
        section2, _ = Section.objects.get_or_create(nom='Personality & Work Style', ordre=2)
        
        # SECTION 2: 1..6 (matching what your section2 template expects)
        # IMPORTANT: your DB uses `ordre` globally, not per-section.
        # So we must use unique ordre values for Section 2 to avoid clashing with Section 1 questions.
        q1_s2, _ = Question.objects.get_or_create(
            ordre=8,
            defaults={'texte': 'When facing a complex problem, what do you naturally do first?', 'section': section2}
        )

        ChoixReponse.objects.get_or_create(question=q1_s2, texte='Break it into logical steps and analyze it carefully', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q1_s2, texte='Imagine different creative solutions', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q1_s2, texte='Ask others and brainstorm together', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q1_s2, texte='Act quickly and adjust while moving', domaine=domaines['informatique'])

        q2_s2, _ = Question.objects.get_or_create(
            ordre=2,
            defaults={'texte': 'When working on a group project, you usually:', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q2_s2, texte='Take the leadership role', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q2_s2, texte='Organize tasks and structure the work', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q2_s2, texte='Focus deeply on your part', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q2_s2, texte='Motivate and support the team emotionally', domaine=domaines['sante'])

        q3_s2, _ = Question.objects.get_or_create(
            ordre=3,
            defaults={'texte': 'How do you react under pressure?', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q3_s2, texte='Stay calm and logical', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q3_s2, texte='Feel stressed but push through', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q3_s2, texte='Look for support from others', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q3_s2, texte='Get energized by the challenge', domaine=domaines['commerce'])

        q4_s2, _ = Question.objects.get_or_create(
            ordre=4,
            defaults={'texte': 'Which statement describes you best?', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q4_s2, texte='I need clear structure and rules', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q4_s2, texte='I need freedom and creativity', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q4_s2, texte='I need meaning and purpose', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q4_s2, texte='I need growth and achievement', domaine=domaines['commerce'])

        q5_s2, _ = Question.objects.get_or_create(
            ordre=5,
            defaults={'texte': 'In social situations, you:', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q5_s2, texte='Prefer small deep conversations', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q5_s2, texte='Enjoy large group discussions', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q5_s2, texte='Listen more than you speak', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q5_s2, texte='Naturally influence others', domaine=domaines['ingenierie'])

        q6_s2, _ = Question.objects.get_or_create(
            ordre=6,
            defaults={'texte': 'What drains your energy most?', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q6_s2, texte='Repetitive routine work', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q6_s2, texte='Lack of structure', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q6_s2, texte='Working alone too much', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q6_s2, texte='Not seeing progress', domaine=domaines['informatique'])

        # SECTION 2: extra questions from template (ordre 10, 12, 13 in DB)
        q3_s2_extra, _ = Question.objects.get_or_create(
            ordre=10,
            defaults={'texte': 'How do you react under pressure?', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q3_s2_extra, texte='Stay calm and logical', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q3_s2_extra, texte='Feel stressed but push through', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q3_s2_extra, texte='Look for support from others', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q3_s2_extra, texte='Get energized by the challenge', domaine=domaines['commerce'])

        q12_s2_extra, _ = Question.objects.get_or_create(
            ordre=12,
            defaults={'texte': 'In social situations, you:', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q12_s2_extra, texte='Prefer small deep conversations', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q12_s2_extra, texte='Enjoy large group discussions', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q12_s2_extra, texte='Listen more than you speak', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q12_s2_extra, texte='Naturally influence others', domaine=domaines['ingenierie'])

        q13_s2_extra, _ = Question.objects.get_or_create(
            ordre=13,
            defaults={'texte': 'What drains your energy most?', 'section': section2}
        )
        ChoixReponse.objects.get_or_create(question=q13_s2_extra, texte='Repetitive routine work', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q13_s2_extra, texte='Lack of structure', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q13_s2_extra, texte='Working alone too much', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q13_s2_extra, texte='Not seeing progress', domaine=domaines['informatique'])

        # SECTION 3: work environment (section1/templates/section1/section3.html expects 14..20)
        # IMPORTANT: `ordre` is global across sections in your DB, so we must use unique values.



        
        # SECTION 3: WORK ENVIRONMENT
        section3, _ = Section.objects.get_or_create(nom='Work Environment Preferences', ordre=3)
        
        q14, _ = Question.objects.get_or_create(
            ordre=14,
            defaults={'texte': 'You perform best in environments that are:', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q14, texte='Highly structured and organized', domaine=domaines['ingenierie'])
        ChoixReponse.objects.get_or_create(question=q14, texte='Fast-paced and dynamic', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q14, texte='Calm and stable', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q14, texte='Creative and flexible', domaine=domaines['design'])

        q15, _ = Question.objects.get_or_create(
            ordre=15,
            defaults={'texte': 'If your manager gives you full autonomy:', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q15, texte='Feel uncomfortable', domaine=None)
        ChoixReponse.objects.get_or_create(question=q15, texte='Feel motivated', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q15, texte='Feel lost', domaine=None)
        ChoixReponse.objects.get_or_create(question=q15, texte='Feel empowered', domaine=domaines['design'])

        q16, _ = Question.objects.get_or_create(
            ordre=16,
            defaults={'texte': 'Which workplace sounds ideal?', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q16, texte='Big international company with hierarchy', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q16, texte='Startup building new ideas', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q16, texte='Remote digital company', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q16, texte='Institution (hospital, school, government)', domaine=domaines['sante'])

        q17, _ = Question.objects.get_or_create(
            ordre=17,
            defaults={'texte': 'Would you rather:', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q17, texte='Have stable salary and security', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q17, texte='Earn more with performance bonuses', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q17, texte='Take risks for big future rewards', domaine=domaines['ingenierie'])

        q18, _ = Question.objects.get_or_create(
            ordre=18,
            defaults={'texte': 'How important is work-life balance?', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q18, texte='Very important', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q18, texte='Important but flexible', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q18, texte='I prioritize career growth', domaine=domaines['informatique'])

        q19, _ = Question.objects.get_or_create(
            ordre=19,
            defaults={'texte': 'What is your risk tolerance?', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q19, texte='Prefer stability', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q19, texte='Moderate risk', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q19, texte='High risk', domaine=domaines['ingenierie'])

        q20, _ = Question.objects.get_or_create(
            ordre=20,
            defaults={'texte': 'Work-life balance importance (choose your preference):', 'section': section3}
        )
        ChoixReponse.objects.get_or_create(question=q20, texte='Very important', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q20, texte='Important but flexible', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q20, texte='I prioritize career growth first', domaine=domaines['informatique'])

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

        # SECTION 4: INTERNAL TALENTS & MOTIVATION (template section1/templates/section1/section4.html)
        section4, _ = Section.objects.get_or_create(nom='Internal Talents & Motivation', ordre=4)

        # IMPORTANT: your DB uses `ordre` globally, so ordres 21/22 were already used in SECTION 3.
        # We must update the existing Question.section to point to section4.

        q21, _ = Question.objects.get_or_create(
            ordre=21,
            defaults={'texte': 'What type of tasks make you proud?', 'section': section4}
        )
        if q21.section_id != section4.id:
            q21.section = section4
            q21.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Solving technical problems', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Creating something original', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Helping someone succeed', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q21, texte='Achieving business targets', domaine=domaines['commerce'])

        q22_s4, _ = Question.objects.get_or_create(
            ordre=22,
            defaults={'texte': 'If you could master one skill:', 'section': section4}
        )
        if q22_s4.section_id != section4.id:
            q22_s4.section = section4
            q22_s4.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q22_s4, texte='Coding / Engineering', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q22_s4, texte='Design / Art', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q22_s4, texte='Psychology / Communication', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q22_s4, texte='Business / Investment', domaine=domaines['commerce'])

        q23, _ = Question.objects.get_or_create(
            ordre=23,
            defaults={'texte': 'What compliment do you hear most?', 'section': section4}
        )
        if q23.section_id != section4.id:
            q23.section = section4
            q23.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q23, texte='Smart and logical', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q23, texte='Creative', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q23, texte='Kind and supportive', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q23, texte='Confident and ambitious', domaine=domaines['commerce'])

        q24, _ = Question.objects.get_or_create(
            ordre=24,
            defaults={'texte': 'What frustrates you most in a job?', 'section': section4}
        )
        if q24.section_id != section4.id:
            q24.section = section4
            q24.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q24, texte='No intellectual challenge', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q24, texte='No creativity', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q24, texte='Toxic environment', domaine=domaines['sante'])
        ChoixReponse.objects.get_or_create(question=q24, texte='No financial growth', domaine=domaines['commerce'])

        # SECTION 5: CURRENT SKILLS (template section1/templates/section1/section5.html)
        section5, _ = Section.objects.get_or_create(nom='Current Skills', ordre=5)

        q25, _ = Question.objects.get_or_create(
            ordre=25,
            defaults={'texte': 'What skills do you already have? (Multiple choice)', 'section': section5}
        )
        if q25.section_id != section5.id:
            q25.section = section5
            q25.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Programming', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Graphic design', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Video editing / Content creation', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Public speaking', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Sales / persuasion', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Writing', domaine=domaines['design'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Data analysis', domaine=domaines['informatique'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Social media management', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q25, texte='Leadership', domaine=domaines['commerce'])
        ChoixReponse.objects.get_or_create(question=q25, texte='None yet')

        q26, _ = Question.objects.get_or_create(
            ordre=26,
            defaults={'texte': 'Your skill level:', 'section': section5}
        )
        if q26.section_id != section5.id:
            q26.section = section5
            q26.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q26, texte='Beginner')
        ChoixReponse.objects.get_or_create(question=q26, texte='Intermediate')
        ChoixReponse.objects.get_or_create(question=q26, texte='Advanced')

        q27, _ = Question.objects.get_or_create(
            ordre=27,
            defaults={'texte': 'Have you ever:', 'section': section5}
        )
        if q27.section_id != section5.id:
            q27.section = section5
            q27.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q27, texte='Done an internship')
        ChoixReponse.objects.get_or_create(question=q27, texte='Worked part-time')
        ChoixReponse.objects.get_or_create(question=q27, texte='Freelanced')
        ChoixReponse.objects.get_or_create(question=q27, texte='Participated in competitions')
        ChoixReponse.objects.get_or_create(question=q27, texte='None yet')

        # SECTION 6-7: FINANCIAL & LANGUAGES (template section1/templates/section1/section6-7.html)
        section6_7, _ = Section.objects.get_or_create(nom='Financial & Languages', ordre=6)

        q28, _ = Question.objects.get_or_create(
            ordre=28,
            defaults={'texte': 'Are you able to invest in further studies or certifications?', 'section': section6_7}
        )
        if q28.section_id != section6_7.id:
            q28.section = section6_7
            q28.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q28, texte='Yes')
        ChoixReponse.objects.get_or_create(question=q28, texte='Limited budget')
        ChoixReponse.objects.get_or_create(question=q28, texte='No')

        q29, _ = Question.objects.get_or_create(
            ordre=29,
            defaults={'texte': 'What languages do you speak fluently? (Multiple choice)', 'section': section6_7}
        )
        if q29.section_id != section6_7.id:
            q29.section = section6_7
            q29.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q29, texte='Arabic')
        ChoixReponse.objects.get_or_create(question=q29, texte='French')
        ChoixReponse.objects.get_or_create(question=q29, texte='English')
        ChoixReponse.objects.get_or_create(question=q29, texte='German')
        ChoixReponse.objects.get_or_create(question=q29, texte='Other')

        q30, _ = Question.objects.get_or_create(
            ordre=30,
            defaults={'texte': 'Which language are you most comfortable using professionally?', 'section': section6_7}
        )
        if q30.section_id != section6_7.id:
            q30.section = section6_7
            q30.save(update_fields=['section'])
        ChoixReponse.objects.get_or_create(question=q30, texte='Arabic')
        ChoixReponse.objects.get_or_create(question=q30, texte='French')
        ChoixReponse.objects.get_or_create(question=q30, texte='English')

        # SECTION 8: DOCUMENTS & MATCHING (template section1/templates/section1/section8.html)
        section8, _ = Section.objects.get_or_create(nom='Documents & Matching', ordre=8)

        # In this project, these fields are collected as text/file/url inputs.
        # Your current scoring model uses ChoixReponse for scoring; for uploads/links,
        # we create Questions without ChoixReponse.
        q31, _ = Question.objects.get_or_create(
            ordre=31,
            defaults={'texte': 'Upload your CV (PDF)', 'section': section8}
        )
        if q31.section_id != section8.id:
            q31.section = section8
            q31.save(update_fields=['section'])

        q32, _ = Question.objects.get_or_create(
            ordre=32,
            defaults={'texte': 'LinkedIn profile (optional)', 'section': section8}
        )
        if q32.section_id != section8.id:
            q32.section = section8
            q32.save(update_fields=['section'])

        self.stdout.write(self.style.SUCCESS('Questionnaire complet initialisé avec succès!'))


