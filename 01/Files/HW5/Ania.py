# Task 1

# 1. Extract links to web page containing information about musicians 
#    specialising in music genre beginning with ”A”.

# 2. Extract the links to artists’ web pages for the first of the links from the
#    previous step.

# 3. From artist’s pages extract: name of the band, years active.

# 4. As an output use default print function on pandas data frame.

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

from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'title':re.compile('music genre.*')})

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]


# 2. Extract the links to artists’ web pages for the first of the links from the
#    previous step.

painter_links = []

for link in links:
    print(link)
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    
    tags = bs.find_all('ul')[13].find_all('li')

    link_temp_list = []
    for tag in tags:
        try:
            link_temp_list.append('http://en.wikipedia.org' + tag.a['href'])
        except:
            0 

    painter_links.extend(link_temp_list)


# 3. From artist’s pages extract: name of the band, years active.
d = pd.DataFrame({'name of the band':[], 'birth':[], 'death':[], 'nationality':[]})

for painter_link in painter_links[:100]:
    print(painter_link)

    html = request.urlopen(painter_link)
    bs = BS(html.read(), 'html.parser')
    
    try:
        name = bs.find('h1').text
    except:
        name = ''
        
    try:
        years = bs.find('th',string = 'Years active').next_sibling.text
    except:
        years = ''
    
    painter = {'name of the band':name, 'Years active':years}
    
    d = d.append(painter, ignore_index = True)
    print(d)

# 4. As an output use default print function on pandas data frame.
