from astropy.utils.misc import did_you_mean
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
#logins in using already saved google account
time.sleep(1)
login = driver.find_element(By.XPATH,'//*[@id="q97493015"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()

time.sleep(1)

sndlogin = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]')
sndlogin.click()

base_window = driver.window_handles[0]
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(driver.title)


time.sleep(1)
open_up = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[4]/div/div[1]/div/div[2]')
open_up.click()
driver.switch_to.window(base_window)

for x in range(0,1000):
    try:
        time.sleep(1)
        dislike = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[2]/button/span/span[1]/svg/g/path')
        dislike.click()
    except NoSuchElementException:
        print("Save button not found on the page.")
        break
driver.close()

