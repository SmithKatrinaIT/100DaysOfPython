"""
	CONCEPT: REST - HTTP(S) Requests
		-- GET
		-- POST
		-- PUT
		-- DELETE

		TIME formats:
			-- strftime: formats a string to any format we need


"""
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

# retrieve sensitive data from environments file
USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH = "graph1"


""" ---- GET REQUEST ---- """
# Step 1: create user account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


""" ---- POST REQUEST ---- """
## POST REQUEST
# Step 2: create a pixel graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
	"id": GRAPH,
	"name": "walking",
	"unit": "Km",
	"type": "float",
	"color": "shibafu"
}

headers = {
	"X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Step 3: create a pixel on the graph
today = datetime.now()


post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
post_pixel_data = {
	#"date": "20250802",
	"date": today.strftime("%Y%m%d"),
	#"quantity": "9.45",
	"quantity": input("How many kilometers did you walk today? ")  # make the program more interactive
}

post_response = requests.post(url=post_pixel_endpoint, json=post_pixel_data, headers=headers)
# print(response.text)


""" ---- PUT REQUEST ---- """
# Step 4: Update (PUT) previous entry (pixel)
date = today.strftime("%Y%m%d")
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

update_pixel_data = {
	"quantity": "20.16"
}
# put_response = requests.put(url=put_pixel_endpoint, json=update_pixel_data, headers=headers)
# print(put_response.text)


""" ---- DELETE REQUEST ---- """
# Step 5: Delete previous entry (pixel)
date = today.strftime("%Y%m%d")
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)