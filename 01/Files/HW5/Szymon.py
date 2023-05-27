from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


# 1. Extract links to web page containing information about musicians 
#    specialising in music genre beginning with ”A”.
tags = bs.find('span', {'id': "A"}).find_next('ul').find_all('li')
links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]


# 2. Extract the links to artists’ web pages for the first of the links from the
#    previous step.

url = links[0]
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find('span', {'id': "Artists"}).find_next('ul').find_all('li')
links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]


# 3. From artist’s pages extract: name of the band, years active.
# 4. As an output use default print function on pandas data frame.

d = pd.DataFrame({'name of the band':[], 'years active':[]})

for link in links:
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
    
    try:
        years = bs.find('th',string = re.compile('Years.active')).next_sibling.text
    except:
        years = ''
    
    d = d.append({'name of the band':name, 'years active':years}, ignore_index=True)


print(d)