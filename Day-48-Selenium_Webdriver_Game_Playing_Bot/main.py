from selenium import webdriver
from selenium.webdriver.common.by import By
import time

duration = 301

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


time.sleep(10)
language_select = driver.find_element(By.XPATH,value='//*[@id="langSelect-EN"]')

language_select.click()

time.sleep(5)
cookie = driver.find_element(By.ID,"bigCookie")

def clickupgrades(upgrade):
    listt = []

    # Run your function here
    for x in upgrade:
        listt.append(x)
    listt.reverse()
    for x in listt:
        x.click()



start_time = time.time()
last_run_time = time.time()
sec=56
while time.time() - start_time < duration:
    current_time = time.time()
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    cookie.click()
    if current_time - last_run_time >= sec:
        print("5 seconds passed! Running function...")
        clickupgrades(upgrades)
        last_run_time = current_time
        print("Doing Upgrades...")
        sec-=10
print("Script has run for 5 minutes.")
time.sleep(1)
cookpersec = driver.find_element(By.XPATH,'//*[@id="cookiesPerSecond"]')

print(cookpersec.text)

driver.close() #closes specific tab






