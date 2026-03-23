import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait


class InstaFollower:

	def __init__(self):
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_experimental_option("detach", True)
		self.driver = webdriver.Chrome(options=self.chrome_options)

	def retry(self, func, tries=7, delay=3, description=None):
		"""
			-- A decorator that will retry a function if it fails
			-- Use it as a decorator with parameters: @retry(tries=3, delay=3)
		"""
		for i in range(tries):
			print(f"Trying {description}. Attempt {i + 1} of {tries}...")
			try:
				return func()
			except (TimeoutError, TimeoutException, NoSuchElementException, Exception):
				if i == tries - 1:
					raise
				time.sleep(delay)

	def login(self, username, password, url):
		self.driver.get(url)
		wait = WebDriverWait(self.driver, 10)

		wait.until(ec.element_to_be_clickable((By.NAME, "username"))).send_keys(username)
		wait.until(ec.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
		time.sleep(2)
		try:

			wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
			wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div'))).click()

			print("Login successful!")

		except Exception as e:
			print(f"{e}: Couldn't login")


	def find_followers(self, account_to_mimic):
		time.sleep(5)
		self.driver.get(f"https://www.instagram.com/{account_to_mimic}/followers/")
		print(f"Redirected to {account_to_mimic}'s page")
		time.sleep(5)

		followers_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/div/section[2]/div[1]/div[3]/div[2]/a")

		try:
			followers_link.click()
			time.sleep(2)
			print(f"Finding followers of {account_to_mimic}...")

		except NoSuchElementException as e:
			print(f"{e}: can't find follower link")

		follower_modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

		if follower_modal:
			scroll_script = "arguments[0].scrollTop = arguments[0].scrollHeight"
			print("Follower popup displayed....continuing")

			for i in range(5):
				self.driver.execute_script(scroll_script, follower_modal)
				time.sleep(2)

			while True:
				last_height = self.driver.execute_script(scroll_script, follower_modal)
				self.driver.execute_script(scroll_script, follower_modal)
				time.sleep(2)
				new_height = self.driver.execute_script(scroll_script, follower_modal)

				if new_height == last_height:
					break

	def follow(self):
		followers_list = self.driver.find_elements(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
		follow_buttons = self.driver.find_elements(By.TAG_NAME, "button")

		if len(follow_buttons) == 0:
			print("Can't find follow button")
			return

		else:
			for button in follow_buttons[1::]:  # skip first button it:
				if button.text == "Follow":
					button.click()
					time.sleep(1)
				for item in followers_list:
					print(f"Following {item.text}...")

