from urllib import request
from bs4 import BeautifulSoup as BS
import re
import time

# This part prepares preliminary links - links for lists of links
# In url we provide link with selected "Mokotów" as district

# There are 2 divs with 2 ul lists
##  search.listing.promoted - for promoted adv
## search.listing.organic - for "usual" adv

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/warszawa/mokotow?distanceRadius=0&locations=%5Bdistricts_6-39%5D&viewType=listing' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


tags = bs.find('h2', text="Wszystkie ogłoszenia").find_next('ul').find_all('li', {'data-cy': 'listing-item'})

#links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

links = []
for tag in tags:
    a_tag = tag.find_next('a')
    if a_tag is not None:
        url = 'https://www.otodom.pl' + a_tag['href']
        links.append(url)

for link in links:
    print(link)