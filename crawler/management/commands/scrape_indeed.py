# Crawler/management/commands/scrape_indeed.py
from django.core.management.base import BaseCommand
from crawler.scrap import scrape_indeed

class Command(BaseCommand):
    help = 'Scrape job listings from Indeed and save to the database'

    def handle(self, *args, **options):
        job_listings = scrape_indeed()
        self.stdout.write(self.style.SUCCESS(f'Successfully scraped {len(job_listings)} job listings'))
