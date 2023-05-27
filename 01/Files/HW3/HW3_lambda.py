# Exercise 1

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
from bs4 import BeautifulSoup as BS

# Download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
text_byte = html.read()
text_str = text_byte.decode('utf-8')
# print(text_str)


# Task 1: 
# Using lambda expressions print out how many times a tag consisting of a string 
# ”Anna Pavlovna” appears in the text.
def has_Anna_Pavlovna(tag):
    return 'Anna Pavlovna' in tag.get_text()

Anna_Pavlovna = bs.find_all(has_Anna_Pavlovna)
print(len(Anna_Pavlovna))


# Task 2:
# 1) Using lambda expressions enlist tags with exactly one attribute.
# 2) Also, print out the length of this list.
one_attribute_tags = bs.find_all(lambda tag: len(tag.attrs) == 1)
print(one_attribute_tags)
print(len(one_attribute_tags))


