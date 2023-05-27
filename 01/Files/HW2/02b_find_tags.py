################################################################################
# Parsing HTML using Beautiful Soup
################################################################################
# This pogram abuses the style of text to extract either red or green parts.

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

# Beautiful Soup 'find_all' method allows to create list of tags by class:
bs_name_list = bs.find_all('span', {'class':'excitingNote'})
for name in bs_name_list:
    print(name.get_text())

# Instead of displaying it one by one we might use list comprehension to put
# them into new list and pandas data frame:
name_list = [name.get_text() for name in bs_name_list]

# The data can be put into data frame, later into .csv file.
d = pd.DataFrame(name_list)
print(d)

