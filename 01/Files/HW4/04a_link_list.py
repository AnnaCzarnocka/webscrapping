################################################################################
# Scraping Single Wikipedia Page - Example 1.
################################################################################
# This page exctracts links from single wikipedia page in a simplistic way:
from urllib import request
from bs4 import BeautifulSoup as BS
import re

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name' 
html = request.urlopen(url)
text_byte = html.read()
text_str = text_byte.decode('utf-8')
print(text_str)

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# The code below searches for all the <a> tags in the HTML content that have a title attribute matching the regular expression 'List of painters.*'. These tags likely link to pages containing lists of painters. The regular expression .* means any character (.) repeated zero or more times (*), so the regular expression matches any title that starts with the string 'List of painters' followed by any other characters.
tags = bs.find_all('a', {'title':re.compile('List of painters.*')})

# The code below constructs a list of links to the pages containing the lists of painters by appending the href attribute of each <a> tag to the base Wikipedia URL, 'http://en.wikipedia.org'. It then prints each link to the console using a for loop.
links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)
