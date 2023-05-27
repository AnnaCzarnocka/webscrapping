import ssl
from urllib import request
from bs4 import BeautifulSoup as BS
ssl._create_default_https_context = ssl._create_unverified_context

# Download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

#How many times a tag consisting of a string "Anna Pavlovna" appears in the text?
Anna_Pavlovna_tags = bs.find_all(lambda tag: 'Anna Pavlovna' in tag.get_text())
print(Anna_Pavlovna_tags)
print(len(Anna_Pavlovna_tags))

#Enlist tags with exactly one attribute and print out the length of this list.
tags_with_one_attribute = bs.find_all(lambda tag: len(tag.attrs) == 1)
print(tags_with_one_attribute)
print(len(tags_with_one_attribute))
