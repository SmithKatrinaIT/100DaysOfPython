"""
    Concept: Creating GUIs using Tkinter to read and react to our Python code
    -- This lesson extends the Password Manager project using JSON
    -- Searching the Json file to see if theirs an entry already
    	-- Will be able to update an existing entry or add a new one

    NOTE:  This code is void of previous lesson comments to focus on the "search" functionality"
    -- refer to the main.py for the starting code if necessary


"""
import json
from tkinter import *  # specifying the (*) will import all tkinter classes, but not individual modules
from tkinter import messagebox
import pandas
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
			   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for letter in range(randint(8, 10))]
	password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
	password_numbers = [choice(numbers) for num in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)

	password = "".join(password_list)

	# print(f"Your password is: {password}")
	password_input.insert(0, password)
	pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	password = password_input.get()
	website = website_input.get()
	email_user = emailUser_input.get()

	# create a data dictionary to hold the json data to write to the json file
	new_data = {
		website: {
			"email": email_user,
			"password": password
		}
	}

	if len(password) <= 0 or len(website) <= 0 or len(email_user) <= 0:
		messagebox.showwarning(title="Oops", message="Please don't leve any fields empty")
	else:
		try:
			with open("data.json", "r") as file:
				# read old data
				data = json.load(file)
		except FileNotFoundError: # "try" failed, so need to create and write simultaneously to the file with the "w" write flag
			with open("data.json", "w") as file:
				json.dump(new_data, file, indent=4)
		else: # the "try" succeeded, so continue with program requirements
			# update old data with new data
			data.update(new_data)

			with open("data.json", "w") as file:
				json.dump(data, file, indent=4)
		finally: # regardless of the "try" passing or exception caught, clear the input fields with the "finally" clause
			password_input.delete(0, END)
			website_input.delete(0, END)

# ---------------------------- SEARCH JSON FILE ----------------------- #
def search_json_file():
	website = website_input.get()
	try:
		with open("data.json", "r") as file:
			# read old data
			data = json.load(file)
	except FileNotFoundError: # "try" failed, so need to create and write simultaneously to the file with the "w" write flag
		messagebox.showerror(title="Error", message=f"Sorry, {website} no entry found.")
	else:

		if website in data:
			print("entry found")
			messagebox.showinfo(title=website, message=f" Email: {data[website]['email']}\n{data[website]['password']}")
		else:
			messagebox.showerror(title="Error", message=f"Sorry, {website} entry was not found. Try adding it now.")

# ---------------------------- UI SETUP ------------------------------- #

# WINDOW SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# CANVAS SETUP
canvas = Canvas(window, width=200, height=200, highlightthickness=2, highlightbackground="black", bd=5, relief="solid")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, pady=(0, 20))

# LABEL(S) SETUP
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

emailUser_label = Label(text="Email/Username:")
emailUser_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, )

# INPUT FIELDS SETUP
website_input = Entry(width=22)
website_input.grid(column=1, row=1)
website_input.focus()

emailUser_input = Entry(width=40)
emailUser_input.grid(column=1, row=2, columnspan=2)
emailUser_input.insert(END, "yourEmailAddress@example.com")

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

# BUTTON SETUP
search_btn = Button(text="Search", width=13, bg="blue", fg="black", command=search_json_file)
search_btn.grid(column=2, row=1)

generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

#add_btn = Button(text="Add", width=38, command=save_to_file)

# using json.dump(), json.load() and json.update()
add_btn = Button(text="Add", width=38, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

# REQUIRED!! - GUI WINDOW LOOP:
window.mainloop()
