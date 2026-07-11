from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(100)
driver.save_screenshot('screenshot.png')

driver.close()