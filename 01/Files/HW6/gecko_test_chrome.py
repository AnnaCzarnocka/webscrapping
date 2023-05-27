from selenium import webdriver
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

path = '/usr/local/bin/chromedriver'  # specify path to Chrome driver
url = 'http://www.google.com'

driver = webdriver.Chrome(executable_path=path)  # create Chrome driver
time.sleep(3)
driver.get(url)
time.sleep(5)
driver.close()
