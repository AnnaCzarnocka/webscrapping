from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page=1'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


# 1. Extract links to web page containing information about musicians 
#    specialising in music genre beginning with ”A”.
tags = bs.find('span', {'id': "A"}).find_next('ul').find_all('li')
links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]