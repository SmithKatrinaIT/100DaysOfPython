"""
	CONCEPTS: WEB SCRAPING WITH BEAUTIFUL SOUP
	-- Web scraping is the process of extracting data from websites
	-- Beautiful Soup is a Python library that makes it easy to scrap data from websites
	-- Beautiful Soup object can be created by passing in the HTML source code of the website
	   -- two ways to parse the HTML: lxml and html.parser
	-- See the headers of your browser goTo: http://myhttpheader.com/
		--By Passing headers along, servers can give you the targeted page in your language and also in your currency.
		--Also, makes the request look (slightly) more human and less like a bot.
			-- Why? Headers include data that is sent over by a browser rather than a script.
			-- And many web servers like Amazon's may block requests they think originate from bots.
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
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
	"Accept-Language": "en-US,en;q=0.9",
	"Cache-Control": "max-age=0"
}

response = requests.get(url=AMAZON_URL, headers=headers)
fake_amazon_page = response.text

soup = BeautifulSoup(fake_amazon_page, "html.parser")
# print(soup)
# print(soup.prettify())


price_element = soup.select_one(".a-offscreen").getText()
print(price_element)

price = price_element.split("$")[1]
print(price)




product_on_sale = soup.find(id_="productTitle")
product_sale_price = float(price)
product_buy_link = AMAZON_URL

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
