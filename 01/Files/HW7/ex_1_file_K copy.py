# Write a bot, that will log into a Campuswire, and will send itself (its .py file, not it’s code) to your tutor.
# Hint: You probably want to test it before - by sending direct messages to yourself :)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime

# Init:
gecko_path = '/opt/homebrew/bin/geckodriver'
ser = Service(gecko_path)
options = webdriver.firefox.options.Options()
options.headless = False
driver = webdriver.Firefox(options=options, service=ser)

url = 'http://campuswire.com/signin'

# Actual program:
time.sleep(9)

driver.get(url)

time.sleep(9)

username = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
my_email = input('Please provide your email:')
username.send_keys(my_email)

time.sleep(5)

password = driver.find_element(By.XPATH, '//input[@placeholder="password"]')
my_pass = getpass.getpass('Please provide your password:')
password.send_keys(my_pass)

time.sleep(5)

button = driver.find_element(By.XPATH, '//button[@type="submit"]')
button.click()

time.sleep(9)

# Navigate directly to the desired chat URL
url = 'https://campuswire.com/c/dms/anna.czarnocka5701'
driver.get(url)

time.sleep(4)

timestamp = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")

path = "/Users/annaczarnocka/Desktop/Webscrapping/Files/HW7/ex_1_me.py"
file_py = driver.find_element(By.XPATH, '//input[@type="file"]')
file_py.send_keys(path)

# Pressing enter:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()

time.sleep(10)

# Close browser:
driver.quit()
