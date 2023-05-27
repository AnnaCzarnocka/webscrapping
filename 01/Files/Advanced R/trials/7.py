from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.keys import Keys
import time

gecko_path = '/opt/homebrew/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options, service=ser)

url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page=1g'

driver.get(url)
time.sleep(5)

tags = []

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_content = driver.page_source
    new_bs = BS(new_content, features='html.parser')
    new_tags = new_bs.find('span', text="Jobs").find_next('div').find_all('a', {'_ngcontent-serverapp-c304="" nfj-postings-item="" _nghost-serverapp-c309'})

    if len(new_tags) > len(tags):
        tags = new_tags
    else:
        break

links = []
for tag in tags:
    a_tag = tag.find_next('a')
    if a_tag is not None:
        url = 'https://nofluffjobs.com' + a_tag['href']
        links.append(url)

for link in links:
    print(link)

driver.quit()
