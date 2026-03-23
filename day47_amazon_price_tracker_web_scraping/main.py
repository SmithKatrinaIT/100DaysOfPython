"""
	CONCEPTS: WEB SCRAPING WITH BEAUTIFUL SOUP
	-- Web scraping is the process of extracting data from websites
	-- Beautiful Soup is a Python library that makes it easy to scrap data from websites
	-- Beautiful Soup object can be created by passing in the HTML source code of the website
	   -- two ways to parse the HTML: lxml and html.parser

"""
import os

import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

SENDER_EMAIL = os.environ.get("TEST_EMAIL")
SENDER_PASSWORD = os.environ.get("TEST_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")
BEST_PRICE = 100.00
TEST_URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=TEST_URL)
fake_amazon_page = response.text

soup = BeautifulSoup(fake_amazon_page, "html.parser")
#print(soup)

#span class a-price-whole
# when trying to find a class attribute you have to use class_ instead of class because class is a python keyword
# price_element = soup.find(name="span", class_="a-offscreen")
# price = price_element.text
# price_list = price.split("$")
# price = price_list[1]
# print(price)

#SHORTER SOLUTION
price_element = soup.find(class_="a-offscreen").getText()
print(price_element)
price = price_element.split("$")[1]
# print(price)

product_on_sale = soup.find(id_="productTitle")
product_sale_price = float(price)
product_buy_link = TEST_URL

# the object used to connect to smtp server
if product_sale_price < BEST_PRICE:
	with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:

		# method of sending email securely - encrypted
		connection.starttls()

		# login to email
		connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
		msg_subject = "Price dropped!"
		contents = f"Subject: {msg_subject}\n\nThe price of the product is now {price}\n\n{product_on_sale}\n\n{product_buy_link}"

		# send email
		connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=TO_EMAIL,msg=f'Subject: {msg_subject}\n\n{contents}')
		print("Email sent successfully")
