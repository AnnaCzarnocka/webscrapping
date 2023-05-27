import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.keys import Keys
import time

gecko_path = '/opt/homebrew/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options=options, service=ser)

links = []
for i in range(1, 3):
    url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/warszawa/mokotow?distanceRadius=0&locations=%5Bdistricts_6-39%5D&viewType=listing&limit=72&page=' + str(i)
    driver.get(url)
    body = driver.find_element(By.TAG_NAME, 'body')
    tags = []

    while True:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        new_content = driver.page_source
        new_bs = BS(new_content, features='html.parser')
        new_tags = new_bs.find('h2', text="Wszystkie ogłoszenia").find_next('ul').find_all('li', {'data-cy': 'listing-item'})

        if len(new_tags) > len(tags):
            tags = new_tags
        else:
            break

    for tag in tags:
        a_tag = tag.find_next('a')
        if a_tag is not None:
            url = 'https://www.otodom.pl' + a_tag['href']
            links.append(url)

driver.quit()

# Create a DataFrame with the links
df = pd.DataFrame({'Link': links})

print(df)
