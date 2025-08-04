from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4144425061&distance=25&f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=103664787&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

time.sleep(3)
sign_in = driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()
time.sleep(1)
username = driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal_session_key"]')
username.send_keys("your_email)
password = driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys("your_password")
enter = driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
enter.click()
time.sleep(4)

# first_job_save = driver.find_element(By.XPATH,value='//*[@id="ember1593"]/div/div/div[1]')
# first_job_save.click()
# follow=driver.find_element(By.XPATH,value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/section/section/div[1]/div[1]/button/span')
# follow.click()

job_list=driver.find_elements(By.CSS_SELECTOR,'ul.rVFpBZlNaEQOtRIqvCFZkHqipnBTecJqNNLxMUQ li.ember-view.erfhlCczvjhljBkvmzpmhFlCWLeFmsKTIwhtA')
for job in job_list:
    try:
        time.sleep(3)
        driver.execute_script("arguments[0].scrollIntoView(true);", job)
        job.click()
        print("Job Chosen")
        time.sleep(1)
        save= driver.find_element(By.CSS_SELECTOR,'button.jobs-save-button.artdeco-button.artdeco-button--secondary.artdeco-button--3')
        save.click()
        print("Job Saved")
    except NoSuchElementException:
        print("Save button not found on the page.")
print("Reached end of available jobs. Ending Script Bye Bye")


driver.close()





