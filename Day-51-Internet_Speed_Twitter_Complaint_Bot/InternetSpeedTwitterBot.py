from bokeh.colors.named import ghostwhite
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.speedtest.net/")
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        time.sleep(4)
        login = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        login.click()
        time.sleep(30)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]'
                                                   '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]'
                                                      '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        print(self.down)


    def tweet_at_provider(self,emailadd,password):
        self.driver.get('https://x.com/?lang=en')
        time.sleep(4)
        enter_x = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div')
        enter_x.click()
        time.sleep(4)
        email=self.driver.find_element(By.NAME,'text')
        email.send_keys(emailadd)
        time.sleep(1)
        nextt = self.driver.find_element(By.XPATH,"//button[.//span[text()='Next']]")
        nextt.click()
        time.sleep(4)
        passworddd  = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passworddd.send_keys(password)
        time.sleep(4)
        login = self.driver.find_element(By.XPATH,"//button[.//span[text()='Log in']]")
        login.click()
        time.sleep(2)
        try:
            pop_up = self.driver.find_element(By.XPATH,
                                              '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button/div/svg')
            pop_up.click()
        except NoSuchElementException:
            print("No pop up")
        if float(self.up) <10 or float(self.down)<150:
            time.sleep(0.5)
            tweet_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))

            # Continue with your operations on tweet_box
            tweet_box.send_keys(f'Hey,Internet Provider, why is my internet speed {self.down}MBPS Download/{self.up}MBPS Upload when I pay for 150MBPS Download/10MBPS Upload')
            publish = self.driver.find_element(By.XPATH,'//button[@data-testid="tweetButtonInline"]')
            publish.click()





