import time

import wait
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait

import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import re

# Load ENV variables
load_dotenv("../.env")


SF_RENTING_FORM = os.environ.get("SF_RENTING_RESEARCH_FORM_URL")
SF_RENTING_SPREADSHEET = os.environ.get("SF_RENTING_RESEARCH_SHEET_URL")

headers = {
	"User-Agent": "CCBot/2.0 (https://commoncrawl.org/faq/)",
	"Accept-Language": "en-US,en;q=0.5"
}

""" USE BEAUTIFULSOUP TO GET THE DATA FROM THE WEBSITE """
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/", headers=headers)
zillow_clone_web_page = response.text
soup = BeautifulSoup(zillow_clone_web_page, "html.parser")

# Empty lists
listing_prices = []
listing_addresses = []
listing_dict = {}

## GET ALL PROPERTY LINKS - using list comprehension
listing_links = [anchor.get("href") for anchor in soup.find_all(name="a", class_="property-card-link")]
# print(f"listings: {listing_links}")

zillow_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

regex_pattern = re.compile(r"\$\d[\d,]*")

for price in zillow_prices:
	match = regex_pattern.findall(price.text)
	listing_prices.extend(match)

# print(f"listing prices array: {listing_prices}")

zillow_addresses = soup.find_all(name="address")
for address in zillow_addresses:
	address_stripped = address.text.strip("\n ")
	address_split = address_stripped.split("|")

	print(f"list length: {len(address_split)}")

	#print(f"length of address_split: {len(address_split)}")

	if len(address_split) >= 2:
		listing_addresses.append(len(address_split)-1)
	else:
		listing_addresses.append(address_split[0].strip())

""" Used for Debugging as I go """
# address_count = 1
# for address in zillow_addresses:
# 	print(f"{address_count}: {address}")
# 	address_count += 1



""" Fill out SF Renting Research Form """

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = ""

try:
	driver = webdriver.Chrome(options=chrome_options)

except Exception as e:
	print(f"{e}. please run this code again.")

else:
	# Navigate to site
	driver.get(SF_RENTING_FORM)
	driver.implicitly_wait(5)

wait = WebDriverWait(driver, 5)

for index in range(len(listing_addresses)):
	listing_dict[listing_addresses[index]] = (listing_prices[index], listing_links[index])


for key, item in listing_dict.items():

	# Access property address field
	property_address = wait.until(ec.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input' )))
	property_address.clear()
	property_address.send_keys(key)

	# print(listing_prices[0])
	# print(listing_links[0])

	property_price = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
	property_price.clear()
	property_price.send_keys(item[0])

	property_link = wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
	property_link.clear()
	property_link.send_keys(item[1])
	#
	driver.implicitly_wait(5)
	submit_form = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
	submit_form.click()

	submit_another_response = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Submit another response')))
	submit_another_response.click()

