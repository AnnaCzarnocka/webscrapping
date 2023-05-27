from selenium import webdriver
import time

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


path = '/usr/local/bin/geckodriver'
url = 'http://www.google.com'


driver = webdriver.Firefox(executable_path = path)
time.sleep(3)
driver.get(url)
time.sleep(5)
driver.close()



