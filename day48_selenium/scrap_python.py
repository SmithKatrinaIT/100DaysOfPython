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

PYTHON_URL = "https://python.org"

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

#returns a Selenium object so you need to access the text by calling the .text method on the object
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times)):
	events[n] = {
		"time": event_times[n].text,
		"name": event_names[n].text
	}

print(events)

# closes a single tab you have open
# driver.close()

# closes the entire browser
driver.quit()
