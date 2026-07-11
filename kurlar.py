from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = "https://www.tcmb.gov.tr/kurlar/kurlar_tr.html"
driver.get(url)
time.sleep(1)
date = driver.find_element(
    By.XPATH, "/html/body/main/section/div[2]/div[2]/div[1]/div/div/div[2]/div/table/tbody/tr[2]/td[5]/a").click()
time.sleep(1)

show = driver.find_element(
    By.XPATH, "/html/body/main/section/div[2]/div[2]/div[1]/div/div/input").click()
time.sleep(1)
currency = driver.find_elements(By.CLASS_NAME, "para")
currency_list=[]
for i in currency :
    if "/" in i.text:
        currency_list.append(i)
for i in currency_list:
    print(i.text)