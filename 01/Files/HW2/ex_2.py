
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd


url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a' 
html = re.urlopen(url)
text_byte = html.read()
text_str = text_byte.decode('utf-8')
print(text_str)

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')


# 1) Extact Pawel’s date of birth.
bs_bday = bs.find_all('span', {'class':'bday'})
bdate = [name.get_text() for name in bs_bday]
print('\n', 'Pawel’s date of birth:')
print(bdate[0], '\n')

# 2) Extract Pawel’s three occupations.
print('\n', 'Pawel’s three occupations:\n')
occupation_section = bs.find('div', {'class': 'hlist'})
occupations = occupation_section.find_all('li')
for occupation in occupations:
    print(occupation.text.strip(), '\n')


# 3) Extact the list of references.
print('\n', 'The the list of references:\n')
references_section = bs.find('div', {'class': 'reflist'})
references = references_section.find_all('li')
for reference in references:
    print(reference.text.strip())
