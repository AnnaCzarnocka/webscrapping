# Import the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.keys import Keys
from urllib.parse import urljoin
import time

# Set up the WebDriver
chrome_path = '/path/to/chromedriver'  # Provide the path to your chromedriver executable
ser = Service(chrome_path)
options = webdriver.ChromeOptions()
options.headless = False
driver = webdriver.Chrome(service=ser, options=options)

# Open the page
url = 'https://nofluffjobs.com/pl/?lang=en&gclid=CjwKCAjwscGjBhAXEiwAswQqNB0HL4nZul0aq27jiZv4ZUlZ0UjUWfTdQfZMP_TCwygRpwYXGTDhtBoCIQcQAvD_BwE&criteria=jobLanguage%3Den&page=1'
driver.get(url)
time.sleep(5)

# Scroll down the page to load more content
body = driver.find_element(By.TAG_NAME, 'body')

tags = []


while True:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

    # Get the page source and create a BeautifulSoup object
    new_content = driver.page_source
    new_bs = BS(new_content, features='html.parser')

    # Find the <a> element within the <div> element
    new_tags = new_bs.find('div', {'_ngcontent-serverapp-c304': '', 'class': 'list-container ng-star-inserted'}).find_all('a', {'_ngcontent-serverapp-c304': '', 'nfj-postings-item': '', '_nghost-serverapp-c309': ''})

    if len(new_tags) > len(tags):
        tags = new_tags
    else:
        break


links = []
for tag in tags:
    a_tag = tag.find_next('a')
    if a_tag is not None:
        url = 'https://nofluffjobs.com/pl/job' + a_tag['href']
        links.append(url)

for link in links:
    print(link)


# Close the WebDriver
driver.quit()
