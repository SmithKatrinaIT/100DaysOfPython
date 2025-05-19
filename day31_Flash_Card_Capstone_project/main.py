"""
	CAPSTONE PROJECT: Flash Card app
	-- Create a GUI using Tkinter
	-- Learn the most frequent words of a particular language (French or Spanish)
	-- NOTE: Instructor used french_words.csv, I have created a spanish_word.csv
	-- TKinter window.after(): used to delay execution of the program or execute a command in the background sometime in the future
		--Takes in an integer as milliseconds.
	-- TKinter window.after_cancel(): cancels the execution of a delayed command that was previously scheduled
		-- Takes in the "ID" --- the thing to be cancelled
	-- Must use window.after() and not time.sleep() because window.mainloop() is already a delayed loop - additional delayed loops cannot be created.
	-- Cannot create PhotoImage objects inside a function --- won't be able to

	NEW CONCEPT: Pandas to_dict(orient=records) parameter.
	-- orient=records: will give each columns values as a list of dictionaries (to include the column header as the key)
		-- Syntax: [{column:value, column, value}, {column:value, column:value}]
		-- Example:
			[{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}.....]

"""
# IMPORTS
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pandas
import time

# GLOBAL CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
word_dict = {}  # random word dictionary within the list of language_dict dictionary
timer = ""
language_dict = {}  # full dictionary of words to learn


# SETUP DATA DICTIONARY
try:
	updated_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("data/spanish_words.csv")
	language_dict = original_data.to_dict(orient="records")
else:
	language_dict = updated_data.to_dict(orient="records")


# def get_language_dict():
# 	language_dataframe = {}
# 	try:
# 		language_dataframe = pandas.read_csv("data/words_to_learn.csv")
# 	except FileNotFoundError:
# 		language_dataframe = pandas.read_csv("data/spanish_words.csv")
#
# 	else:
# 		pass
# 	finally:
# 		dict = language_dataframe.to_dict(orient="records")
# 		print(dict)
# 		return dict


# --------------------------------------------------- FUNCTIONS ---------------------------------------------------- #

# CREATE FLIP CARD - FRONT AND THE TIME DELAY TO FLIP THE CARD
def next_card():

	global word_dict, flip_timer

	# window.after_cancel() used to stop (cancel) the timer (flip_timer) count when button is clicked (again)
	window.after_cancel(flip_timer)

	# get ONE word dictionary from the list of dictionaries within language_dict
	word_dict = choice(language_dict)
	canvas.itemconfig(card_title, text="Spanish", fill="black")
	canvas.itemconfig(card_word, text=word_dict["Spanish"], fill="black")
	canvas.itemconfig(canvas_card, image=card_front_img)

	# Creates a timer a (variation of time.sleep()) -- to flip card to english translation after 3 seconds
	flip_timer = window.after(5000, func=flip_card)


	""" My way to originally solve for removing a word from the dictionary object and creating another file because instructor
	    originally used this same function in both buttons.  
	    -- this solution used lamdba in the button event to pass a arg to the button and capture which button was clicked using the same function reference """
	# Check which button was click, remove word from file if user knows the word, leave if they don't, then update unknown words to new file
	# if button_name == "right_btn":
	# 	language_dict.remove(word)
	# 	updated_dataframe = pandas.DataFrame(language_dict)
	# 	updated_dataframe.to_csv("data/words_to_learn.csv")


# CHANGE TO BACK OF CARD, CHANGE THE TRANSLATION TO ENGLISH, AND CHANGE THE TEXT FILL
def flip_card():

	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=word_dict["English"], fill="white")
	canvas.itemconfig(canvas_card, image=card_back_img)

# NOTE: this function replaced the new_card() function from previous steps in the capstone project
def is_known():
	language_dict.remove(word_dict)
	next_card()
	updated_dataframe = pandas.DataFrame(language_dict)

	# setting the index=False arg prevents system from adding the index number to the file
	updated_dataframe.to_csv("data/words_to_learn.csv", index=False)



# WINDOW SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=25, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# language_dict = get_language_dict()

# CANVAS WITH FRONT CARD SETUP
canvas = Canvas(width=900, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(450, 300, image=card_front_img)

# FRONT CARD TEXT
card_title = canvas.create_text(450, 200, text="Title", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(450, 325, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# CREATE WRONG BUTTON
wrong_img = PhotoImage(file="images/wrong.png")
# wrong_btn = Button(image=wrong_img, highlightthickness=0, command=lambda: next_card("wrong_btn")) # use with get_language_dict()
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

# CREATE RIGHT BUTTON
right_img = PhotoImage(file="images/right.png")
# right_btn = Button(image=right_img, highlightthickness=0, command=lambda: next_card("right_btn")) # use with get_language_dict()
right_btn = Button(image=right_img, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

# TODO CREATE FLIP MECHANISM


# ----------------------------------------------- FUNCTION CALLS / DEBUG / TEST ------------------------------------------ #
# FUNCTION CALLS
next_card()
# Program control - Windowloop
window.mainloop()
