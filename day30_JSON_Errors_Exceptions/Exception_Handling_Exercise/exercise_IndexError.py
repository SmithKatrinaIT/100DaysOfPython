fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
""" This exercise will throw a IndexError if not caught"""
def make_pie(index):

	try:
		fruit = fruits[index]
		print(fruit + " pie")
	except IndexError:
		print("Fruit pie")

make_pie(4)