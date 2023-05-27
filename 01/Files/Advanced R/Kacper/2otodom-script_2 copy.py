# here we open the page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.keys import Keys
import time

# This part prepares preliminary links - links for lists of links
# In url we provide link with selected "Mokotów" as district

# There are 2 divs with 2 ul lists
##  search.listing.promoted - for promoted adv
## search.listing.organic - for "usual" adv

gecko_path = '/opt/homebrew/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/warszawa/mokotow?distanceRadius=0&locations=%5Bdistricts_6-39%5D&viewType=listing' 

driver.get(url)
time.sleep(5)


body = driver.find_element(By.TAG_NAME, 'body')

tags = []


while True:
    body.send_keys(Keys.PAGE_DOWN)
    # Adjust sleep time as needed to allow the page to load.
    time.sleep(2)

    new_content = driver.page_source
    new_bs = BS(new_content, features = 'html.parser')
    new_tags = new_bs.find('h2', text="Wszystkie ogłoszenia").find_next('ul').find_all('li', {'data-cy': 'listing-item'})

    if len(new_tags) > len(tags):
        tags = new_tags
    else:
        break