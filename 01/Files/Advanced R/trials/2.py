from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

d = pd.DataFrame({'position': [], 'company': [], 'location': []})

base_url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page='

total_pages = 5  # Set the total number of pages you want to scrape

print('Extracted position and company name:', '\n')

for page in range(1, total_pages+1):
    url = base_url + str(page)
    html = request.urlopen(url)
    bs = BS(html.read(), 'html.parser')

    job_listings = bs.find_all('div', {'class': 'posting-description'})

    for job in job_listings:
        try:
            position = job.find('h3', {'data-cy': 'title position on the job offer listing'}).text.strip()
        except:
            position = ''

        try:
            company = job.find('span', {'data-cy': 'company name on the job offer listing'}).text.strip()
        except:
            company = ''

        try:
            location = job.find('span', {'class': 'tw-text-ellipsis tw-inline-block tw-overflow-hidden tw-whitespace-nowrap lg:tw-max-w-[100px] tw-text-right'}).text.strip()
        except:
            location = ''

        job_info = {'position': position, 'company': company, 'location': location}
        d = d.append(job_info, ignore_index=True)

print(d)
