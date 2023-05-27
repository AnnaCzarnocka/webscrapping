################################################################################
# Regex + Beautiful Soup.
################################################################################
# This script shows how to use powerful regex as another tool to navigate tags

from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Lets download and import to Beautiful Soup already known page:
url = 'http://www.pythonscraping.com/pages/page3.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Now we search for images by regex:
images = bs.find_all('img', {'src':re.compile('\.\./img/gifts/img.*\.jpg')})

# Using the fact, that tag object works same as dictionary to access attribute:
for image in images:
    print(image['src'])

# It is also possible to navigate further:
for image in images:
    print(image.parent.parent.td.text)

################################################################################
# Experiment with code on your own.
# Can you extract all prices using regex? Directly? Indirectly?
