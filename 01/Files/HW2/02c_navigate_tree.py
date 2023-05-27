################################################################################
# Parsing HTML using Beautiful Soup
################################################################################
# This program navigates the tree of simple site.

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

######################
from urllib import request as re
from bs4 import BeautifulSoup as BS

######################
# At first look at the site and its code:
url = 'http://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

######################
# To access a single html element, we access 'bs' object variables with 
# dot operator:
my_text1 = bs
my_text2 = bs.html
my_text3 = bs.html.head
my_text4 = bs.html.body
my_text5 = bs.html.body.div
my_text6 = bs.html.body.div.table.tr.th
my_text7 = bs.html.body.div.table.tr.th.find_next_sibling()
my_text8 = bs.html.body.div.table.tr.th.find_next_sibling().find_next_sibling().find_next_sibling()


# print(my_text1)
# print(my_text2)
# print(my_text3)
# print(my_text4)
# print(my_text5)
# print(my_text6)
# print(my_text7)
print(my_text8)

# However it can be quite a long way to go :)

######################
# You can use such code as help to find next tags:
# for child in bs.html.body.div.table.children:
#     print('*******************************')
#     print(child)

######################
# For other helpful navigation commands explore python help for BeautifulSoup tag object:
# help(bs.html)
