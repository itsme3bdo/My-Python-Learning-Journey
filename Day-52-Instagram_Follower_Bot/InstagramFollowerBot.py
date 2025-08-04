from bokeh.colors.named import ghostwhite
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

SIMILAR_ACCOUNT="instagram"
USERNAME="your username"
PASSWORD="your password"
url_main = "https://www.instagram.com/accounts/login/"
url_cris = "https://www.instagram.com/cristiano/"

class InstagramFollowerBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(url_main)

    def login(self):
        time.sleep(2)
        login_username = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        login_username.send_keys(USERNAME)
        login_password =self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        login_password.send_keys(PASSWORD)
        login = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button/div')
        login.click()
        time.sleep(15)

    def find_followers(self):
        time.sleep(4)
        self.driver.get(url_cris)
        time.sleep(10)
        followers = self.driver.find_element(By.XPATH,"//a[contains(@href,'/followers')]")
        followers.click()
        time.sleep(5)
        # scroll_script = "arguments[0].scrollTop += 300"  # Scrolls down by 300px
        # pop_up = self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        #
        # for _ in range(2):  # Scroll 5 times
        #     self.driver.execute_script(scroll_script, pop_up)
        #     time.sleep(6)

    def follow(self):
        time.sleep(5)
        dialog = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'))
        )
        follow_b = dialog.find_elements(By.TAG_NAME, 'button')
        check=0
        for button in follow_b:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(randint(1,3))
            button.click()
            time.sleep(randint(1,3))
            check +=1
            if check == 15:
                break
        print(f"Task finished with {check} users followed")
