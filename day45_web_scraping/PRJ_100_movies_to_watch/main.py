import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")

# get the h3 tag with class of title
movie_titles = soup.find_all(name="h3", class_="title")
movie_title_list = [title.text.split(" ", 1)[1] for title in movie_titles]
reversed_movie_list = movie_title_list[::-1]


with open('movies.txt', mode="w", encoding="utf8") as file:
	num = 1
	for movie in reversed_movie_list:
		file.write(f"{num}: {movie}\n")
		num += 1





