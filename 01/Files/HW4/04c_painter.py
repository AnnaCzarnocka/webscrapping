################################################################################
# Scraping Single Wikipedia Page - Example 3.
################################################################################
# This page scraps the data for one painter from wikipedia:
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

d = pd.DataFrame({'name':[], 'birth':[], 'death':[], 'nationality':[]})

url = 'http://en.wikipedia.org/wiki/Edvard_Munch' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    name = bs.find('h1').text
except:
    name = ''

try:
    birth = bs.find('th',string = 'Born').next_sibling.text
    birth = re.findall('[0-9]+\s+[A-Za-z]+\s+[0-9]+', birth)[0]
except:
    birth = ''

try:
    death = bs.find('th',string = 'Died').next_sibling.text
    death = re.findall('[0-9]+\s+[A-Za-z]+\s+[0-9]+', death)[0]
except:
    death = ''

try:
    nationality = bs.find('th',string = 'Nationality').next_sibling.text
except:
    nationality = ''

painter = {'name':name, 'birth':birth, 'death':death, 'nationality':nationality}

d = d.append(painter, ignore_index = True)

print(d)
