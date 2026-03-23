import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()