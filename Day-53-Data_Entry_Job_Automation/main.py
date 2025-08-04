import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://docs.google.com/forms/d/e/1FAIpQLSfheLPXTfEzakvdb4s10m5s5prAsTrT5JO2-AZi46IJoR6ADA/viewform?usp=header'

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_webpage = response.text

soup  = BeautifulSoup(zillow_webpage,"html.parser")
properties = soup.select(".property-card-link")
prices  = soup.select(".PropertyCardWrapper__StyledPriceLine")
adress = soup.find_all(name="address")



property_links = [prop.get("href") for prop in properties]
pricess = [price_tag.getText().strip("+ /mo 1 bd") for price_tag in prices]
addresses = [place_tag.getText().strip(" \n ") for place_tag in adress]


print(property_links)
print(pricess)
print(addresses)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(4)
for n in range(len(addresses)):
    time.sleep(0.5)
    q_address = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_address.send_keys(addresses[n])
    q_rent = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_rent.send_keys(pricess[n])
    q_link= driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_link.send_keys(property_links[n])
    submit = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()
    another_one = driver.find_element(By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_one.click()
    # driver.get(url)
    time.sleep(1)

driver.quit()



