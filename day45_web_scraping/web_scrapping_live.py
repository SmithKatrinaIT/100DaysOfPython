"""
	CONCEPTS: WEB SCRAPING WITH BEAUTIFUL SOUP
	-- Web scraping is the process of extracting data from websites
	-- Beautiful Soup is a Python library that makes it easy to scrap data from websites
	-- Beautiful Soup object can be created by passing in the HTML source code of the website
	   -- two ways to parse the HTML: lxml and html.parser

"""
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# gets singular elements from the soup
yc_title_tag = soup.find(name="a")
yc_title_link = yc_title_tag.get("href")
yc_points = soup.find(name="span", class_="score").text

# find_all() method returns a list of all the elements that match the specified tag
articles = soup.find_all(name="a")
articles_texts = []
articles_links = []
for article in articles:
	articles_texts.append(article.text)
	articles_links.append(article.get("href"))

article_points = [int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_points)
largest_index = article_points.index(largest_number)

print(f"{articles_texts[largest_index]}: {articles_links[largest_index]}")





