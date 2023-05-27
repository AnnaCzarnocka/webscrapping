# Exercise 1

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
from bs4 import BeautifulSoup as BS

# Download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


# Task 1: 
# Using lambda expressions print out how many times a tag consisting of a string 
# ”Anna Pavlovna” appears in the text.
Anna_Pavlovna = bs.find_all(lambda tag: 'Anna Pavlovna' in tag.get_text())
print('\n', 'How many times a tag consisting of a string ”Anna Pavlovna” appears in the text:')
print(len(Anna_Pavlovna), '\n')


# Task 2:
# 1) Using lambda expressions enlist tags with exactly one attribute.
# 2) Also, print out the length of this list.
one_attribute_tags = bs.find_all(lambda tag: len(tag.attrs) == 1)
# print(one_attribute_tags)
print('\n', 'The length of the list of tags with exactly one attribute:')
print(len(one_attribute_tags))