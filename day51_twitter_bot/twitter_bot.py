from selenium import webdriver

class InternetSpeedTwitterBot:
	def __init__(self):
		self.up = 0
		self.down = 0
		self.driver = webdriver.Chrome()

	def get_internet_speed(self):
		import speedtest
		st = speedtest.Speedtest()
		st.get_best_server()
		up = st.upload()
		down = st.download()
		return up, down

	def tweet_at_provider(self, up, down):
		import requests
		import os
		from twilio.rest import Client
		import twilio_credentials
		account_sid = twilio_credentials.account_sid
		auth_token = twilio_credentials.auth_token
		client = Client(account_sid, auth_token)
		api_key = os.environ.get("OWM_API_KEY")
		owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
		parameters = {
			"lat": 52.52,
			"lon": 13.41,
			"exclude": "current,minutely,daily",
			"appid": api_key
		}
		response = requests.get(owm_endpoint, params=parameters)
		response.raise_for_status()
		weather_data = response.json()
		twilio_number = "+12065174144"
		target_number = "+491512345678"
		wind_speed = weather_data["hourly"][0]["wind_speed"]
		wind_deg = weather_data["hourly"][0]["wind_deg"]
		wind_direction = weather_data["hourly"][0]["wind_deg"]
		if wind_speed > 25 or wind_deg > 45:
			message = client.messages.create(
				body="It's going to rain today. Remember to bring an ☔️",
				from_=twilio_number,
				to=target_number
			)
			print(message.status)

