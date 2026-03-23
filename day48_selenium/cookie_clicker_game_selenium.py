"""
	Concept: Use Selenium to interact with the Cookie Clicker game
	-- Day 48 ending challenge

"""


from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from selenium.webdriver.support.wait import WebDriverWait

# ====================== DEFINE FUNCTIONS ======================
def check_store():
	pass


COOKIE_CLICKER_URL = "https://ozh.github.io/cookieclicker/"

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(COOKIE_CLICKER_URL)

# Wait for the Cloudflare challenge to be solved. This might take a few moments.
print("Waiting for Cloudflare challenge to be solved...")
wait = WebDriverWait(driver, 60)  # Wait up to 60 seconds
wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
print("Cloudflare challenge passed. Proceeding with automation...")

# Add timer to allow for page loading and traversal
sleep(3)

print("looking for language selections")
try:

	# Must first select your preferred language before you can play the game
	language = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN") # threw an error
	print("Found language button....clicking")
	language.click()
	sleep(3)

except NoSuchElementException:
	print("Language selection not found")

# Wait for everything to settle
sleep(2)

# Find the cookie and click it
cookie = driver.find_element(By.ID, value="bigCookie")

# Get all store items (products 0-17)
item_ids = [f"product{i}" for i in range(18)]


# Set timers
wait_time = 15
timeout = time() + wait_time  # Check for purchases every 5 seconds
five_min = time() + 60 * 5  # Run for 5 minutes


while True:
	cookie.click()

	if time() > timeout:
		try:
			# Get current cookie count
			cookie_element = driver.find_element(By.ID, value="cookies")
			cookie_text = cookie_element.text
			cookie_count = int(cookie_text.split(" ")[0].replace(",", ""))

			# Find all available products in the store
			products = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

			# Find the most expensive item we can afford
			best_item = None
			for product in reversed(products):  # Start from most expensive (bottom of list)
				# Check if item is available and affordable (enabled class)
				if "enabled" in product.get_attribute("class"):
					best_item = product
					break

			# Buy the best item if found
			if best_item:
				best_item.click()
				print(f"Bought item: {best_item.get_attribute('id')}")

		except (NoSuchElementException, ValueError):
			print("Couldn't find cookie count or items")

		# Reset timer
		timeout = time() + wait_time

	# Stop after 5 minutes
	if time() > five_min:
		try:
			cookies_element = driver.find_element(by=By.ID, value="cookies")
			print(f"Final result: {cookies_element.text}")
		except NoSuchElementException:
			print("Couldn't get final cookie count")
		break

# closes the entire browser
driver.quit()