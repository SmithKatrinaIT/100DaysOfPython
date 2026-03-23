"""
	Concept: Web scraping with Selenium

	-- Webdriver: interacts with a specified browser
	-- Selenium goes beyond Beautiful Soup in that it can scrape websites that use more complex languages than HTML
		-- ANGULAR, REACT, JAVASCRIPT
		-- It also eliminates the need to use the "requests" library to get the browser information

	-- Selenium Locator stratergies: https://www.selenium.dev/documentation/webdriver/elements/locators/
		-- documentation on what html selectors (locators) to use to extract elements
"""


from selenium import webdriver
from selenium.webdriver.common.by import By

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


