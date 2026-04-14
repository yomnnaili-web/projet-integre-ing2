from django.core.management.base import BaseCommand
from core.scraper import MetierScraper

class Command(BaseCommand):
    help = 'Importe les métiers via web scraping'

    def handle(self, *args, **options):
        self.stdout.write('Début de l\'importation des métiers...')
        
        scraper = MetierScraper()
        count = scraper.importer_metiers()
        
        self.stdout.write(
            self.style.SUCCESS(f'Importation terminée: {count} métiers importés')
        )
