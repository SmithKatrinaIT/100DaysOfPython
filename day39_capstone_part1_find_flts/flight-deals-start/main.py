"""
    Capstone Project - Flight Club Project
        -- Using Python, Google Sheets, and the Flight Search API
        -- Find your next flight from anywhere in the world

        Required APIs:
            -- Google Sheets API -Sheety
            -- Amadeus Flight Offers API
            -- Amadeus Airport Codes by City API
                https://test/api.amadeus.com/v1/references/locations/cities
                https://test/api.amadeus.com/v1/references/locations/airports/by-city?apikey=YOUR_API_KEY
            -- Amadeus Flight Search API
            -- Twilio API
            -- OWM API

        Google Sheet URL: https://docs.google.com/spreadsheets/d/1-YeZsBA3Ja07DE35XeX6YJJYlnw-3Qu0B3grQXMeSkE/edit?gid=0#gid=0

        Datetime Module: using strftime()
        -- allows for formating a datatime output in a specific manner
        -- utilize placeholder formate codes (syntax) to formate the data
        -- Reference: https://www.w3schools.com/python/python_datetime.asp
            -- Examples:
            -- %a == short version of a week day (Wed, Tue, Fri)
            -- %d == day of the month (01-31)
            -- %m == Month as a number (01-12)
            -- %Y == Full Year (2025)
            -- %H == Hour (military - 00-23)
            -- %I == hour (12hr clock)
            -- %M == Minute (00-59)
            -- %X == Local version of time (17:41:00)
"""
import os
import time
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../../.env")

# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_sheety_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()


# Set your origin airport
ORIGIN_CITY_IATA = "ATL"


# ====== Update the Airport Codes in Google Sheet ==============
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    pprint(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_sheety_data()


# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)


    # ===================== Send SMS if flight prices are lower than the price on the Google Sheet ===============

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )

        # SMS not working? Try whatsapp instead.
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only ${cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.leave_date} until {cheapest_flight.return_date}."
        )




