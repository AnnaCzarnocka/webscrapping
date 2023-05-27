from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page=1'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find('span', {'id': "Jobs"}).find_next('div').find_all('a')
links = ['https://nofluffjobs.com' + tag.a['href'] for tag in tags]

print(links)


# <a _ngcontent-serverapp-c304="" nfj-postings-item="" _nghost-serverapp-c309="" class="posting-list-item posting-list-item--support highlightId-TECHNICAL-SUPPORT-SPECIALIST-I-FORWARD-THINKING-SYSTEMS-POLSKA-KRAKOW-4 ng-star-inserted" id="nfjPostingListItem-technical-support-specialist-i-forward-thinking-systems-polska-Kraków" target="_self" href="/pl/job/technical-support-specialist-i-forward-thinking-systems-polska-krakow-4">