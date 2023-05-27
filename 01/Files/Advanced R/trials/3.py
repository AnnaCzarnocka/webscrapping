from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page=1'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find('h3', {'data-cy': 'title position on the job offer listing'}).find_next('div').find_all('a')
links = ['https://nofluffjobs.com' + tag['href'] for tag in tags]


print('Extracted position, company name, location, and salary:', '\n')

d = pd.DataFrame({'position': [], 'company': [], 'location': [], 'salary': []})

for link in links:
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    try:
        position = bs.find('h3', {'data-cy': 'title position on the job offer listing'}).text.strip()
    except:
        position = ''

    try:
        company = bs.find('span', {'data-cy': 'company name on the job offer listing'}).text.strip()
    except:
        company = ''

    try:
        location = bs.find('span', {'class': 'tw-text-ellipsis tw-inline-block tw-overflow-hidden tw-whitespace-nowrap lg:tw-max-w-[100px] tw-text-right'}).text.strip()
    except:
        location = ''

    try:
        salary = bs.find('span', {'data-cy': 'salary ranges on the job offer listing'}).text.strip()
    except:
        salary = ''

    job = {'position': position, 'company': company, 'location': location, 'salary': salary}

    d = d.append(job, ignore_index=True)

print(d)
