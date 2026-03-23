"""
	CONCEPT: Web Scraping
"""

import requests
from bs4 import BeautifulSoup


URL = "https://www.billboard.com/charts/hot-100/"

requested_year = input("What year would you like to travel? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"{URL}{requested_year}"

headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.3"
}

response = requests.get(url=billboard_url, headers=headers)
billboard_soup = BeautifulSoup(response.text, "html.parser")
billboard_songs = billboard_soup.select("li ul li h3")
billboard_songs_list = [song.getText().strip() for song in billboard_songs]
print(billboard_songs_list)



