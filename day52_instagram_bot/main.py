import os
from dotenv import load_dotenv

from day52_instagram_bot.insta_follower import InstaFollower


# Load ENV variables
load_dotenv("../.env")

SIMILAR_ACCOUNT = "healthyminutemeals"
INSTAGRAM_USER = os.environ.get("INSTA_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTA_PASSWORD")
INSTAGRAM_URL = "https://www.instagram.com"



bot = InstaFollower()


bot.login(INSTAGRAM_USER, INSTAGRAM_PASSWORD, INSTAGRAM_URL)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()

