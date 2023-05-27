################################################################################
# Scraping Single Wikipedia Page - Example 2.
################################################################################
# This page exctracts links from wikipedia page in a simplistic way:
from urllib import request
from bs4 import BeautifulSoup as BS

painter_links = []

# Look at the page and the code
url = 'http://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22M%22' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('ul')[13].find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]

painter_links.extend(links)

for link in painter_links:
    print(link)
