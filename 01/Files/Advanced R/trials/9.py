from urllib import request
from bs4 import BeautifulSoup as BS

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page=1'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('a', {'_ngcontent-serverapp-c304': '', 'nfj-postings-item': '', '_nghost-serverapp-c309': ''})
links = ['https://nofluffjobs.com/pl/job/' + tag['href'] for tag in tags]

print("Hey, this is my list of job links!")
print(links)
