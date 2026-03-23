"""
	Concept: Web scraping with Selenium

	-- Webdriver: interacts with a specified browser
	-- Selenium goes beyond Beautiful Soup in that it can scrape websites that use more complex languages than HTML
		-- ANGULAR, REACT, JAVASCRIPT
		-- It also eliminates the need to use the "requests" library to get the browser information

	-- Selenium Locator stratergies: https://www.selenium.dev/documentation/webdriver/elements/locators/
		-- documentation on what html selectors (locators) to use to extract elements

	-- To interact with a web page using Selenium, you call action methods of the Selenium object
		- Example seleniumObj.click()

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SIGN_UP_URL = "https://secure-retreat-92358.herokuapp.com/"

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(SIGN_UP_URL)


# GET ALL THE INPUT FIELDS
first_name_input = driver.find_element(By.NAME, value="fName")
last_name_input = driver.find_element(By.NAME, value="lName")
email_input = driver.find_element(By.NAME, value='email')

# Send input to a field while interacting with the website using Selenium
first_name_input.send_keys("Katrina")
first_name_input.send_keys(Keys.ENTER)

last_name_input.send_keys("Smith")
last_name_input.send_keys(Keys.ENTER)

email_input.send_keys("python3.100days@gmail.com")
email_input.send_keys(Keys.ENTER)

sign_up = driver.find_element(By.TAG_NAME, value="button")
sign_up.click()


# In order to send a key that is not a letter, number or symbol --we use another Selenium Package called "Keys"
# Keys contains a bunch of keyboard constants, like "Enter" to trigger the "Return/Enter" key and trigger the "send_keys" action




# closes the entire browser
driver.quit()
