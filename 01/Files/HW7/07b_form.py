from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Init:
gecko_path = '/opt/homebrew/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options = options, service=ser)

url = 'http://pythonscraping.com/pages/files/form.html'

# Actual program:
time.sleep(9)
driver.get(url)
print(driver.page_source)

time.sleep(5)

username = driver.find_element(By.XPATH, '//input[@name="firstname"]')
username.send_keys('Spam')

password = driver.find_element(By.XPATH, '//input[@name="lastname"]')
password.send_keys('Eggs')

time.sleep(5)

button = driver.find_element(By.XPATH, '//input[@type="submit"]')
button.click()

time.sleep(5)
print(driver.page_source)

# Close browser:
driver.quit()
