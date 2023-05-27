################################################################################
# Scraping Single Wikipedia Page
################################################################################
# This page exctracts links from wikipedia page in a simplistic way:
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


################################################################################
# This part prepares preliminary links - links for lists of links :)
################################################################################
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('List of [aA].*')})

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

# Get section A
section_id = bs.find('span', {'class': 'mw-headline', 'id': 'A'})
ul_tag = section_id.find_next('ul')
tags = ul_tag.find_all('li')

genre_links = []

# Extract links from section A
for tag in tags:
    try:
        genre_links.append('http://en.wikipedia.org' + tag.a['href'])
    except:
        pass

#First bullet
for link in genre_links:
    print(link, end='\n')

################################################################################
# This part prepares real artists links
################################################################################

artists_links = []

link1 = genre_links[0]
# print(link1)

html = request.urlopen(link1)
bs = BS(html.read(), 'html.parser')
    
tags = bs.find_all('ul')[17].find_all('li')

link_temp_list = []
for tag in tags:
    try:
        link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
    except:
        0 
artists_links.extend(link_temp_list)

#Second bullet
for link in artists_links:
    print(link, end='\n')



################################################################################
# This part scraps artists data
################################################################################
 
d = pd.DataFrame({'name':[], 'active':[]})


for artist_link in artists_links[:100]:
    print(artist_link)

    html = request.urlopen(artist_link)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
    
    try:
        active = bs.find('th',string = 'Years active').next_sibling.text
        active = re.findall('[0-9]*\s*\,*\-*', active)
    except:
        active = ''
    
    artist = {'name':name, 'active':active}
    
    d = d.append(artist, ignore_index = True)
    print(d)

################################################################################
# This part saves data to csv.
################################################################################
# d.to_csv('painters.csv')