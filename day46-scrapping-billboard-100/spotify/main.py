"""
	CONCEPT: Web Scraping
"""
import os
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../../.env")
client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIFY_REDIRECT_URI")
spotify_username = os.environ.get("SPOTIFY_USERNAME")
scope = "playlist-modify-private"

SPOTIFY_PLAYLISTS = []
SPOTIFY_PLAYLIST_ID = 0


# retrieve sensitive data from environments file
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    show_dialog=True))

current_user = sp.current_user()
user_id = sp.current_user()["id"]
# print(user_id)
# print(current_user)

""" ========================  Get Billboard song list ============================== """

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
#print(billboard_songs_list)

spotify_track_uri_list = []

for song in billboard_songs_list:
    song_uri = sp.search(q=song, type="track")
    spotify_track_uri_list.append(song_uri["tracks"]["items"][0]["uri"])

#print(spotify_track_uri_list)

new_playlist = sp.user_playlist_create(user=user_id, public=False, collaborative=False, name=f"{requested_year} Billboard 100", description="Playlist created using webscraping and python3")
sp.playlist_add_items(playlist_id=new_playlist["id"], items=spotify_track_uri_list, )





