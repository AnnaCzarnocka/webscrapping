################################################################################
# Lambda expressions + Beautiful Soup.
################################################################################
# This script uses lambda expressions with find_all func. to search for tags:

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
from bs4 import BeautifulSoup as BS

# Download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Oldschool method by creating function and passing it as an argument.
# This function should take "tag" as argument (any variable name, but the type 
# should be BS object representing a tag)

def AsessTag(tag):
    assessment = len(tag.get_text()) < 30
    return assessment

selected_tags = bs.find_all(AsessTag)

# Lambda expression put in place of tag beautiful soup will have 'tag' as value.
# You can make any selecting statements based on the tag, its methods and 
# attributes. It should return True/False value.

#selected_tags = bs.find_all(lambda tag: (len(tag.get_text()) < 30))
#selected_tags = bs.find_all(lambda tag: (len(tag.get_text()) < 30) & (len(tag.get_text()) > 5))
#selected_tags = bs.find_all(lambda tag: (len(tag.get_text()) < 30) & (len(tag.get_text()) > 5) & (',' not in tag.get_text()))
#selected_tags = bs.find_all(lambda tag: (len(tag.attrs) == 1))

for tag in selected_tags:
    print('*' * 30)
    print(tag.get_text())

###############################################################################
# Uncomment the printing loops to get the results of different statements.
# Try to understand them.
# Experiment with code on different site (e.g. shopping list).
