"""
	CONCEPT: Working with REST APIs and Natural language Processing

		-- Project: Build an exercise tracking program using Python and Google Sheets

"""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

GENDER = "female"
WEIGHT_KG = 63.0493
HEIGHT_CM = 154.94
AGE = 53



# retrieve sensitive data from environments file
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
SHEETY_AUTH = os.environ.get("SHEETY_BASIC_AUTH")

headers = {
	"x-app-id": NUTRITIONIX_APP_ID,
	"x-app-key": NUTRITIONIX_API_KEY,
	"Content-type": "application/json",
}

exercise_text = input("Tell me which exercise(s) you did: ")
natural_language_data = {
	"query": exercise_text,
	"gender": GENDER,
	"weight_kg": WEIGHT_KG,
	"height_cm": HEIGHT_CM
}
natural_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=natural_language_endpoint, json=natural_language_data, headers=headers)
result = response.json()


""" Sheety API: Save API response data to Google Sheets using Nutrition Natural Language Processing. """

# Sheety VARS
sheet_project_id = os.environ.get(("SHEETY_API_PROJECT_ID"))
sheety_project_name = "workoutTracking" # needs to be camel case
sheety_sheet_name = "sheet1" # name of sheet inside Sheety.  It should make Google Sheets, but if not use Sheety name.

# sheety_get_endpoint = "https://api.sheety.co/564b30e84d1795124417ee77f75acef1/workoutTracking/sheet1"

sheety_endpoint = f"https://api.sheety.co/{sheet_project_id}/{sheety_project_name}/{sheety_sheet_name}"

today = datetime.now().strftime("%Y%m%d")
time_now = datetime.now().strftime("%X")


for exercise in result["exercises"]:
	sheet_data = {
		"sheet1": { # this need to be the singular form of the Sheet name (i.e. Sheet Name is "workouts", json object should be "workout"
			"date": today,
			"time": time_now,
			"exercise": exercise["name"].title(),
			"duration": exercise["duration_min"],
			"calories": exercise["nf_calories"]
		}
	}

	#sheet_response = requests.post(url=sheety_endpoint, json=sheet_data) # without Authentication set
	sheet_response = requests.post(url=sheety_endpoint, json=sheet_data, auth=(os.environ.get("SHEETY_USERNAME"), os.environ.get("SHEETY_PASSWORD")))
	print(sheet_response.text)