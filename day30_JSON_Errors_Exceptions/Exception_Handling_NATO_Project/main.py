"""
	Concept: Adding Exception/Error Handling to Day 26 NATO Phonetic Alphabet Project
	-- Concept included list comprehension and Pandas
"""

import pandas

# Create a dictionary in this format:   {"A": "Alfa", "B": "Bravo"}
nato_dataframe = pandas.read_csv("../../day26_list_dict_pandas_comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

""" My solution: use a loop"""
done = False

# while not done:
#
# 	word = input("Enter a word: ").upper()
# 	try:
# 		phonetic_list = [nato_dict[letter] for letter in word]
# 	except KeyError:
# 		print(f"Sorry, only letters in the alphabet please.")
#
# 	else:
# 		print(phonetic_list)
# 		done = True


""" Instructor's solution was to use recursion """
def generate_phonetic():
	word = input("Enter a word: ").upper()
	try:
		phonetic_list = [nato_dict[letter] for letter in word]
	except KeyError:
		print(f"Sorry, only letters in the alphabet please.")
		generate_phonetic()
	else:
		print(phonetic_list)

generate_phonetic()