from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd
import datetime

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

d = pd.DataFrame({'name of the band':[], 'genre':[], 'years active':[]})

url = 'https://en.wikipedia.org/wiki/Queen_(band)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


print('Extracted name of the band, its genre and number of years active:', '\n')

try:
    name = bs.find('th', {'class': 'infobox-above'}).find('div').text
except:
    name = ''

try:
    genre = bs.find('th',string = 'Genres').next_sibling.text
except:
    genre = ''

try:
    years = bs.find('th',string = 'Years active').next_sibling.text
except:
    years = ''

try:
    active = bs.find('th',string = 'Years active').next_sibling.text.strip()
    active_years = active.split('–') # Split years range by en dash
    start_year = int(active_years[0]) # Get the starting year
    if active_years[1] == 'present':
        end_year = datetime.datetime.now().year # Set the ending year as the current year
    else:
        end_year = int(active_years[1]) # Get the ending year
    num_years_active = end_year - start_year
    active = f'{num_years_active} years'
except:
    active = ''


painter = {'name of the band':name, 'genre':genre, 'years active':years, 'number of years active':active}

d = d.append(painter, ignore_index = True)

print(d)