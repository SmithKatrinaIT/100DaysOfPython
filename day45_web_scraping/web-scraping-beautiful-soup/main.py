"""
	CONCEPTS: WEB SCRAPING WITH BEAUTIFUL SOUP
	-- Web scraping is the process of extracting data from websites
	-- Beautiful Soup is a Python library that makes it easy to scrap data from websites
	-- Beautiful Soup object can be created by passing in the HTML source code of the website
	   -- two ways to parse the HTML: lxml and html.parser

"""
from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
	contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())

# find_all() method returns a list of all the elements that match the specified tag
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
	print(tag.getText())
	print(tag.get("href"))


# find() method returns the first element that matches the specified tag
heading = soup.find(name="h1", id="name")
print(heading)

# when trying to find an class attribute you have to use class_ instead of class because class is a python keyword
heading = soup.find(name="h3", class_="heading")
print(heading)

# select_one() method returns the first element that matches the specified CSS selector
# select() method returns a list of all the elements that match the specified CSS selector
name = soup.select_one("#name")
print(name)

