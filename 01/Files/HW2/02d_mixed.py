################################################################################
# Parsing HTML using Beautiful Soup
################################################################################
# This program navigates the tree of simple site.

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

######################
from urllib import request as re
from bs4 import BeautifulSoup as BS

url = 'http://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

######################
# Much more convenient way to navigate through HTML is to use both methods.
# Here are some ideas to get Russian Doll text:

doll1 = bs.find('tr', {'id':'gift2'}).td.text

doll2 = bs.find_all('tr', {'id':'gift2'})[0].td.text

doll3 = bs.find('img', {'src':'../img/gifts/img2.jpg'}).parent.parent.td.text

print(doll1, doll2, doll3)
