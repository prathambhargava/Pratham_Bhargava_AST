# scrape.py
import requests
from bs4 import BeautifulSoup
from crawler.models import JobListing

def scrape_indeed(keyword='python+developer'):
    url = f'https://www.indeed.com/jobs?q={keyword}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = []
    for job in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = job.find('h2', class_='title').text.strip()
        company = job.find('span', class_='company').text.strip()
        location = job.find('div', class_='location').text.strip()

        job_data = {'title': title, 'company': company, 'location': location}
        job_listings.append(job_data)

        # Save to the database
        JobListing.objects.create(title=title, company=company, location=location)

    return job_listings