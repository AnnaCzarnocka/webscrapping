from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Init:
gecko_path = '/opt/homebrew/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

# Actual program:
time.sleep(9)
driver.get(url)
print("************************\nBefore:\n*********\n")
print(driver.page_source)

time.sleep(9)

print("************************\nAfter::\n*********\n")
print(driver.page_source)
time.sleep(9)

# Close browser:
driver.quit()
