import requests
from bs4 import BeautifulSoup
from .models import Domaine, Metier

class MetierScraper:
    """
    Scraper pour collecter automatiquement les métiers par domaine.
    Utilisé uniquement pour l'initialisation de la base de données.
    """
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_metiers_exemple(self):
        """
        Exemple de fonction de scraping.
        À adapter selon la source choisie (ex: sites d'orientation publics).
        """
        # Données d'exemple pour démonstration avec icônes et couleurs
        metiers_data = {
            'Informatique & Technologies': {
                'icone': '💻',
                'couleur': '#667eea',
                'description': 'Développement logiciel, Data Science, Cybersécurité, Intelligence artificielle...',
                'metiers': [
                    {'nom': 'Développeur Web', 'description': 'Création de sites et applications web', 'competences': 'HTML, CSS, JavaScript, Python'},
                    {'nom': 'Data Scientist', 'description': 'Analyse de données et machine learning', 'competences': 'Python, R, SQL, Statistics'},
                    {'nom': 'Administrateur Système', 'description': 'Gestion des infrastructures IT', 'competences': 'Linux, Windows Server, Réseaux'},
                ]
            },
            'Santé & Médecine': {
                'icone': '🏥',
                'couleur': '#f093fb',
                'description': 'Médecine générale et spécialisée, Pharmacie, Soins infirmiers...',
                'metiers': [
                    {'nom': 'Infirmier', 'description': 'Soins aux patients', 'competences': 'Soins médicaux, Empathie, Communication'},
                    {'nom': 'Médecin', 'description': 'Diagnostic et traitement', 'competences': 'Médecine, Diagnostic, Chirurgie'},
                    {'nom': 'Pharmacien', 'description': 'Conseil et délivrance de médicaments', 'competences': 'Pharmacologie, Conseil, Gestion'},
                ]
            },
            'Commerce & Vente': {
                'icone': '🛒',
                'couleur': '#4facfe',
                'description': 'Commerce international, Retail et distribution, E-commerce...',
                'metiers': [
                    {'nom': 'Commercial', 'description': 'Vente de produits et services', 'competences': 'Négociation, Communication, Persuasion'},
                    {'nom': 'Chef de produit', 'description': 'Gestion de gamme de produits', 'competences': 'Marketing, Analyse, Stratégie'},
                ]
            },
            'Finance & Comptabilité': {
                'icone': '📊',
                'couleur': '#43e97b',
                'description': 'Audit et expertise comptable, Contrôle de gestion, Banque et assurance...',
                'metiers': [
                    {'nom': 'Comptable', 'description': 'Gestion de la comptabilité', 'competences': 'Comptabilité, Fiscalité, Gestion'},
                    {'nom': 'Analyste Financier', 'description': 'Analyse des marchés financiers', 'competences': 'Finance, Analyse, Excel'},
                ]
            },
            'Marketing & Communication': {
                'icone': '📢',
                'couleur': '#fa709a',
                'description': 'Marketing digital et growth, Relations publiques, Brand management...',
                'metiers': [
                    {'nom': 'Community Manager', 'description': 'Gestion des réseaux sociaux', 'competences': 'Social Media, Communication, Créativité'},
                    {'nom': 'Chargé de communication', 'description': 'Stratégie de communication', 'competences': 'Communication, Rédaction, Événementiel'},
                ]
            },
            'Design & Arts Créatifs': {
                'icone': '🎨',
                'couleur': '#a18cd1',
                'description': 'UX/UI Design, Direction artistique, Graphisme, Architecture...',
                'metiers': [
                    {'nom': 'Designer UX/UI', 'description': 'Conception d\'interfaces utilisateur', 'competences': 'Design, Figma, User Research'},
                    {'nom': 'Graphiste', 'description': 'Création visuelle et graphique', 'competences': 'Photoshop, Illustrator, Créativité'},
                ]
            },
            'Ingénierie & Industrie': {
                'icone': '⚙️',
                'couleur': '#fbc2eb',
                'description': 'Génie civil et BTP, Génie mécanique, Électronique et automatisme...',
                'metiers': [
                    {'nom': 'Ingénieur Civil', 'description': 'Conception de structures', 'competences': 'Génie civil, CAO, Gestion de projet'},
                    {'nom': 'Ingénieur Mécanique', 'description': 'Conception mécanique', 'competences': 'Mécanique, CAO, Innovation'},
                ]
            },
            'Droit & Juridique': {
                'icone': '⚖️',
                'couleur': '#ffecd2',
                'description': 'Avocat et conseil juridique, Droit des affaires, Notariat, Droit pénal...',
                'metiers': [
                    {'nom': 'Avocat', 'description': 'Conseil et défense juridique', 'competences': 'Droit, Plaidoirie, Analyse'},
                    {'nom': 'Juriste d\'entreprise', 'description': 'Conseil juridique en entreprise', 'competences': 'Droit des affaires, Contrats, Conseil'},
                ]
            },
        }
        
        return metiers_data
    
    def importer_metiers(self):
        """
        Importe les métiers scrapés dans la base de données.
        """
        metiers_data = self.scrape_metiers_exemple()
        count = 0
        
        for domaine_nom, domaine_info in metiers_data.items():
            domaine, created = Domaine.objects.get_or_create(
                nom=domaine_nom,
                defaults={
                    'description': domaine_info['description'],
                    'icone': domaine_info['icone'],
                    'couleur': domaine_info['couleur']
                }
            )
            
            # Mettre à jour l'icône et la couleur si le domaine existe déjà
            if not created:
                domaine.icone = domaine_info['icone']
                domaine.couleur = domaine_info['couleur']
                domaine.description = domaine_info['description']
                domaine.save()
            
            for metier_data in domaine_info['metiers']:
                Metier.objects.get_or_create(
                    nom=metier_data['nom'],
                    domaine=domaine,
                    defaults={
                        'description': metier_data['description'],
                        'competences': metier_data['competences']
                    }
                )
                count += 1
        
        return count
