import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import re
from urllib import request
from bs4 import BeautifulSoup as BS

# Download and import to Beautiful Soup already known page:
url = 'https://en.wikipedia.org/wiki/United_Nations' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Task 1: Using regex extract the flags’ image paths for all the members of UN.

regex = r'/wiki/File:Flag_of_.*\.svg'
flags = []
for tag in bs.find_all('img', {'src': re.compile(regex)}):
    flags.append('https://en.wikipedia.org' + tag['src'])

print(flags)

