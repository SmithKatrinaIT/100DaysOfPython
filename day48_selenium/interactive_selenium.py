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

WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(WIKI_URL)


# Hone in on anchor tag using CSS Selectors
active_editors = driver.find_element(By.CSS_SELECTOR, value="#articlecount ul li a") # value="#articlecount a" works as well
print(active_editors.text)

# Programmatically interact with a website as a normal user would do
# active_editors.click()

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()


# Send input to a field while interacting with the website using Selenium
# send_keys evaluates a String as the keyboard entry
search = driver.find_element(By.NAME, value="search")
search.send_keys("python")

# In order to send a key that is not a letter, number or symbol --we use another Selenium Package called "Keys"
# Keys contains a bunch of keyboard constants, like "Enter" to trigger the "Return/Enter" key and trigger the "send_keys" action
search.send_keys(Keys.ENTER)



# closes the entire browser
driver.quit()
