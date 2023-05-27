################################################################################
# Downloading a web file to python
################################################################################

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request as re

url = 'https://www.pythonscraping.com/pages/page3.html'
html = re.urlopen(url)
text_byte = html.read()
text_str = text_byte.decode('utf-8')

print(text_str)

