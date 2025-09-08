import os
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../../.env")

# Globals - Google Sheet variables
GOOGLE_SHEET_PROJECT_NAME = "flightDeals"
GOOGLE_SHEET_NAME = "prices"

# Globals - SHEET variables
SHEETY_API_PROJECT_ID = os.environ["SHEETY_API_PROJECT_ID"]
SHEETY_FLT_DEALS_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_PROJECT_ID}/{GOOGLE_SHEET_PROJECT_NAME}/{GOOGLE_SHEET_NAME}"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._auth = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_sheety_data(self):
        # Make a GET request to the Google Sheets API.
        response = requests.get(url=SHEETY_FLT_DEALS_ENDPOINT, auth=self._auth)
        data = response.json()
        self.destination_data = data[GOOGLE_SHEET_NAME]

        return self.destination_data


    def update_sheety_data(self):
        # Make a PUT request to the Google Sheets API
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_FLT_DEALS_ENDPOINT}/{city["id"]}", json=new_data, auth=self._auth)
            pprint(response.text)
