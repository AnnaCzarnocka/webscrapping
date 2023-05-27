
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

# At first, open the page below in a browser of your choice.
# Second, look how the code is constructed - view source in a browser.

# We download the code as before:
url = 'https://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

# And we can display it in python:


# 1) Extract bolded parts of the text.

# Beautiful Soup 'find_all' method allows to create list of tags by class:
bs_name_list = bs.find_all('span', {'class':'excitingNote'})

# Instead of displaying it one by one we might use list comprehension to put
# them into new list and pandas data frame:
name_list = [name.get_text() for name in bs_name_list]

# The data can be put into data frame, later into .csv file.
d = pd.DataFrame(name_list)
print('Bolded parts of the text:', d, '\n')


# 2) Extract the last Item Title from the table.
last_item = bs.find('tr', {'id': 'gift5'}).td.text
print('The last Item Title from the table:', last_item)


# 3) Extract the footer of the webpage.
footer_content = bs.find('div', {'id': 'footer'}).text.strip()
print('The footer of the webpage:\n', footer_content)


