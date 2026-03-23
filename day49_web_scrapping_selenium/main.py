"""
	Concept: Use Selenium to interact with the Cookie Clicker game
	-- Day 49 Gym Booking Automation Challenge

"""
import os
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

# Create Chrome Profile and create account manually. Put YOUR email and password here:
GYM_USERNAME = os.environ.get("GYM_USERNAME")
GYM_PASSWORD = os.environ.get("GYM_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)

# Create a folder for the Chrome Profile Selenium will use every time
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# include double -- for command line argument to Chrome
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = ""
wait = ""

try:
	driver = webdriver.Chrome(options=chrome_options)

except Exception as e:
	print(f"{e}. please run this code again.")

else:
	# Navigate to site
	driver.get(GYM_URL)
	driver.implicitly_wait(5)

# --------------------------------------------------------------------------------------

# -----------------------------  Step 2 - Automated Login ------------------------------
wait = WebDriverWait(driver, 5)

# Click login button to go to login page
login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

# Fill in login form
email = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email.clear()
email.send_keys(GYM_USERNAME)

password = driver.find_element(By.ID, "password-input")
password.clear()
password.send_keys(GYM_PASSWORD)

driver.implicitly_wait(5)

try:
	# Submit Login Information
	submit_login_btn = driver.find_element(By.ID, value="submit-button")
	submit = WebDriverWait(driver, 4).until(
		ec.presence_of_element_located((By.ID, "submit-button")))
	submit.click()
	print("Credentials submitted successfully")

except Exception as e:
	print(f"{e}: Could not login.")
# --------------------------------------------------------------------------------------


# ---  Step 3 & 4 - Book the upcoming Tuesday class. Check if booked, waitlisted, or need to join the waitlist ---------

already_booked = 0
class_booked = 0
join_waitlist = 0
processed_classes = []

try:

	# find all class cards
	classes = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

	for card in classes:
		# Get the day title from the parent day group
		day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
		day_title = day_group.find_element(By.TAG_NAME, "h2").text


		# Check if this is Tuesday
		if "Tue" in day_title or "Thu" in day_title:
			#Check if this is a 6pm class
			time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
			if "6:00 PM" in time_text:
				# Get class name
				class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

				# Find and click the book button
				button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

				# Track the class details
				class_info = f"{class_name} on {day_title}"


				# Check if already b
				if button.text == "Booked":
					print(f"✔ Already booked: {class_name} on {day_title}")
					already_booked += 1
					processed_classes.append(f"[Booked] {class_info}")
				elif button.text == "Waitlisted":
					print(f"✔ Already on the Waitlist: {class_name} on {day_title}")
					already_booked += 1
					processed_classes.append(f"[Waitlisted] {class_info}")
				elif button.text == "Book Class":
					button.click()
					print(f"✔ Booked: {class_name} on {day_title}")
					class_booked += 1
					processed_classes.append(f"[New Booking] {class_info}")
					time.sleep(1)
				elif button.text == "Join Waitlist":
					button.click()
					print(f"✔ On the Waitlist: {class_name} on {day_title}")
					join_waitlist += 1
					processed_classes.append(f"[New Waitlist] {class_info}")
					time.sleep(1)
				else:
					print(f"❌ Unknown state: {class_name} on {day_title}")

	# tue_class = WebDriverWait(driver, 4).until(ec.presence_of_element_located((By.ID, "class-card-hiit-2025-12-09-0900")))
	# book_hitt_button = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, "book-button-hiit-2025-12-09-0900")))
	# book_hitt_button.click()
	# print("HIIT class booked")

except Exception as e:
	print(f"{e}: Can't find class")

# --------------------------------------------------------------------------------------

# -----------------------------  Step 5 - Print summary ------------------------------

class_summary = (f"\n---- BOOKING SUMMARY ---- \n"
				 f"✔ Booked Classes {class_booked} \n"
				 f"✔ Waitlists joined: {join_waitlist} \n"
				 f"✔ Already booked/waitlisted: {already_booked} \n"
				 f"✔ Total Tuesday 6pm classes processed: {class_booked + already_booked + join_waitlist} \n")

print(class_summary)

print("\n--- DETAILED CLASS LIST ---")
for item in processed_classes:
	print(f"‣ {item}")

# --------------------------------------------------------------------------------------

# -----------------  Step 6 & - Verify Class Booking on "My Bookings page ----------------
my_bookings = driver.find_element(By.LINK_TEXT, "My Bookings")
my_bookings.click()

# Wait for page to load
wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

total_classes = already_booked + class_booked + join_waitlist

print(f"\n--- Total Tue/Thu 6pm classes booked: {total_classes} ---")
print(f"\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Count all the Tue/Thu 6pm classes
verified_classes = 0

# Find all the class cards both confirmed and waitlisted
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
	try:
		when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
		when_text = when_paragraph.text

		# Check if this is Tuesday or thursday
		if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
			class_name = card.find_element(By.TAG_NAME, "h3").text
			print(f"✔ Verified: {class_name}")
			verified_classes += 1
	except NoSuchElementException:
		pass

print("--- VERIFICATION RESULTS ---")
print(f"Expected: {total_classes} bookings.")
print(f"Found: {verified_classes} bookings.")

if total_classes == verified_classes:
	print("✔ All classes verified.")
else:
	print("❌ Not all classes verified.")


# --------------------------------------------------------------------------------------


# -----------------  Step 8 - Time Travel Assistance ----------------

# Manually log into using fake admin credentials
# Advance the time to +3 days
# log out of Selenium and re-run the script

# --------------------------------------------------------------------------------------

# Getting a SessionNotCreatedException?
# Remember to *Quit* Selenium's Chrome Instance before trying to click "run"
#driver.quit()