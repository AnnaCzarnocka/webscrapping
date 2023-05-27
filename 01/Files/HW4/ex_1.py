# Exercise 1 - musicians

# We will work with a Wikipedia pages which contains information about musicians:

# https://en.wikipedia.org/wiki/List_of_hard_rock_musicians_(N%E2%80%93Z)

# • From the page linked above extract links to web pages containing information 
#   about musicians whose name begin with ”Q”.

from urllib import request
from bs4 import BeautifulSoup as BS
import re

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_hard_rock_musicians_(N%E2%80%93Z)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')
 
q_section = bs.find('span', {'class': 'mw-headline', 'id': 'Q'}).find_next('ul')
tags = q_section.find_all('a', {'title':re.compile('Q.*')})

print('Links to web pages containing information about musicians whose name begin with ”Q”:', '\n')

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)