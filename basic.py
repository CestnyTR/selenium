from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)
time.sleep(1)
search = driver.find_element(By.NAME, "q")

search.send_keys("python" , Keys.ENTER)
time.sleep(10)
driver.find_element(By.XPATH,"/html/body/div[3]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div/span/a/h3").click()
time.sleep(10)
