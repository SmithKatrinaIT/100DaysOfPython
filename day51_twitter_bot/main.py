import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

PROMISED_DOWN = 150
PROMISED_UP = 200
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_URL = "https://x.com/login"
SPEED_TEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
	def __init__(self):
		self.up = 0
		self.down = 0
		self.wait_number = 10
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(options=self.chrome_options)
		self.wait = WebDriverWait(self.driver, self.wait_number)

	def get_internet_speed(self):
		self.driver.get(SPEED_TEST_URL)
		self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "js-start-test"))).click()

		self.timer_countdown(45)
		# self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "notification-dismiss"))).click()

		# Find download and upload speed
		download_speed_element = self.driver.find_element(By.CLASS_NAME, "download-speed")
		upload_speed_element = self.driver.find_element(By.CLASS_NAME, "upload-speed")

		# wait till the download speed element is visible

		self.wait.until(ec.visibility_of(download_speed_element))
		# print(f"Download Speed: {download_speed_element.text}")
		self.down = int(download_speed_element.text)

		# wait till the upload	 speed element is visible
		self.wait.until(ec.visibility_of(upload_speed_element))
		# print(f"Upload Speed: {upload_speed_element.text}")
		self.up = int(upload_speed_element.text)

		# close the speedtest page
		self.driver.close()

		return self.up, self.down

	def timer_countdown(self, t):
		while t > 0:
			# Format the time as minutes:seconds (e.g., 01:00)
			mins, secs = divmod(t, 60)
			timer = '{:02d}:{:02d}'.format(mins, secs)

			# Print the timer on the same line and overwrite previous output
			print(f"Timer:{timer}")

			# Pause for 1 second and Decrement the time
			time.sleep(1)  # Pause the program for 1 second
			t -= 1

		# After the loop finishes
		print('\nTime is up! Restarting the program...')

	def login_twitter(self):
		self.driver.get(TWITTER_URL)
		wait = WebDriverWait(self.driver, 105)
		time.sleep(5)

		try:
			email = wait.until(ec.element_to_be_selected(By.NAME, "text"))
			email.send_keys(TWITTER_EMAIL)
			email.send_keys(Keys.ENTER)
			time.sleep(3)

			password = wait.until(ec.element_to_be_clickable(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'))
			password.send_keys(TWITTER_PASSWORD)
			password.send_keys(Keys.ENTER)

			time.sleep(2)

		except Exception as e:
			print(f"Unable to sign in: {e}")



		# email = self.driver.find_element(By.NAME, 'text')
		# email.send_keys(TWITTER_EMAIL)
		# email.send_keys(Keys.ENTER)
		#password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

		# email.send_keys(TWITTER_EMAIL)
		# password.send_keys(TWITTER_PASSWORD)
		# time.sleep(2)
		# password.send_keys(Keys.ENTER)





bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()

# bot = InternetSpeedTwitterBot()
# bot.driver.get(SPEED_TEST_URL)

bot.login_twitter()


# bot.get_internet_speed()

