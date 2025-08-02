import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 36.778259
MY_LONG = -119.417931
SENDER_EMAIL = "python3.100days@gmail.com"
PASSWORD = "chzv hgzr xwqc cziv"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if is_iss_overhead() and is_night():
        ## BONUS: run the code every 60 seconds--get the code to run every 60 seconds with 'time' module
        time.sleep(60)
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=SENDER_EMAIL,
            msg="Subject: Look Up!\n\nThe ISS is overhead in the sky.")

# BONUS: run the code every 60 seconds.





