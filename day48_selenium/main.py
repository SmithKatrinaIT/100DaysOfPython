"""
	Concept: Web scraping with Selenium

	-- Webdriver: interacts with a specified browser
	-- Selenium goes beyond Beautiful Soup in that it can scrape websites that use more complex languages than HTML
		-- ANGULAR, REACT, JAVASCRIPT
		-- It also eliminates the need to use the "requests" library to get the browser infomation

	-- Selenium Locator stratergies: https://www.selenium.dev/documentation/webdriver/elements/locators/
		--
	Locating elements:
		-- By.CLASS_NAME
		-- By.ID
		-- By.NAME
		-- By.TAG_NAME
		-- By.CSS_SELECTOR
		-- By.XPATH
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(AMAZON_URL)

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The prices is: ${price_dollar.text}.{price_cents.text}")

# other webdriver functions to extract website elements
search_bar = driver.find_element(By.NAME, value="field-keywords")
print(search_bar.get_attribute("placeholder"))

# by ID
button = driver.find_element(By.ID, value="submit.buy-now-announce")
print(button.text)


#XPath - is an alternate way of finding an HTML element using a path structure.  It is commonly used when the item to extract
# doesn't have any uniquie identifiers (id, class, css selectors)

## In devtools, located the element you want to extract
## Right click on the element in the Inspect window and click "Copy > Copy XPath"
## Paste the XPath into the "By.XPath" function call

find_lower_price_link = driver.find_element(By.XPATH, value='//*[@id="pricingFeedbackDiv"]/span/b/a')
print(find_lower_price_link.text)



# closes a single tab you have open
# driver.close()

# closes the entire browser
driver.quit()


