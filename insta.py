from instaUserInfo import email, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Instagram:
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()
        self.email = email
        self.password = password

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(self.email)
        time.sleep(1)
        password_input.send_keys(self.password)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

        # Giriş sonrası gelen bildirim pencerelerini geç
        try:
            not_now_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(), 'Şimdi Değil')]")
            not_now_btn.click()
        except:
            pass

    def getFollowings(self):
        url_test = "https://www.instagram.com/_fahriaydn/"
        self.driver.get(url_test)

        time.sleep(2.2)

        # Finds following xpath and opens it
        following_xpath = "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span"
        follow_click = self.driver.find_elements(By.XPATH, following_xpath)
        if follow_click:
            follow_click[0].click()

        time.sleep(2)
        # Finds the path for scoll bar
        modal_xpath = "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(By.XPATH, modal_xpath)
        time.sleep(5) # Kaydırma sonrası kısa bir bekleme

        # Scroll döngüsü
        last_height, height = 0, 1
        scroll_count = 0

        while last_height != height :
            last_height = height
            self.driver.execute_script(
                "arguments[0].scrollTop += 1000", modal)
            time.sleep(10) # Kaydırma sonrası kısa bir bekleme
            height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
            scroll_count += 1
            print(f"Scroll Count: {scroll_count} ,last_height: {last_height} ,height: {height}")
            if last_height == height:
                print("Kaydırma yapılamıyor veya daha fazla içerik yok.")
                break

        links = modal.find_elements(By.TAG_NAME, 'a')
        followings_set = set()
        for link in links:
            href = link.get_attribute('href')
            if href and "https://www.instagram.com/" in href and href.count('/') == 4:
                followings_set.add(href) # İşte tekrar kontrolü burada dolaylı olarak yapılıyor.

        followings = list(followings_set)

        with open("followings.txt", "w", encoding="utf-8") as file:
            for user in followings:
                file.write(user + "\n")

        print(f"{len(followings)} takip edilen kişi bulundu.")

# Kullanım
instagram = Instagram(email, password)
instagram.login()
time.sleep(1000)
instagram.getFollowings()

