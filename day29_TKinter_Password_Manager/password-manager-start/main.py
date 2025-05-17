"""
    Concept: Creating GUIs using Tkinter to read and react to our Python code
    -- POPUPS: user Standard Dialogs and Message Boxes
    -- messagebox is a TKinter module and not a class, therefore it needs to be imported along with all the classes (*)
    -- Pyerclip: allows you to save strings to the clipboard of your computer
    	-- it is cross-platform Python module to copy and paste clipboard functions
    	-- must import the module using "import pyperclip"
    	-- Use pyperclip.copy(): copy text to clipboard
    	-- Use pyperclip.paste(): paste the copied text from clipboard
"""

from tkinter import *  # specifying the (*) will import all tkinter classes, but not individual modules
from tkinter import messagebox
import pandas
from random import choice, randint, shuffle
import pyperclip



LOGO_FRAME_BORDER_COLOR = "black"
LOGO_FRAME_BORDER_THICKNESS = 3
my_pass_data = {}
NO = "No"
YES = "Yes"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
			   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	""" Re-write using LIST COMPREHENSION and importing specific modules to shorten the original Random Password Generator code """

	# nr_letters = random.randint(8, 10)
	# nr_symbols = random.randint(2, 4)
	# nr_numbers = random.randint(2, 4)
	# password_list = []
	#
	# for char in range(nr_letters):
	# 	password_list.append(random.choice(letters))
	#
	# for char in range(nr_symbols):
	# 	password_list += random.choice(symbols)
	#
	# for char in range(nr_numbers):
	# 	password_list += random.choice(numbers)

	password_letters = [choice(letters) for letter in range(randint(8, 10))]
	password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
	password_numbers = [choice(numbers) for num in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)


	# Shorten code by using the .join() method
	# password = ""
	# for char in password_list:
	# 	password += char

	password = "".join(password_list)

	# print(f"Your password is: {password}")
	password_input.insert(0, password)
	pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


# USING PANDAS AND CSV
def save_to_csv():
	password = password_input.get()
	website = website_input.get()
	emailUser = emailUser_input.get()
	global my_pass_data
	my_pass_data = {
		"website": [website],
		"emailUser": [emailUser],
		"password": [password]
	}
	my_pass_dataframe = pandas.DataFrame(my_pass_data)
	print(my_pass_dataframe)
	my_pass_dataframe.to_csv("my_pass.csv")


def save_to_file():
	password = password_input.get()
	website = website_input.get()
	email_user = emailUser_input.get()

	if len(password) <= 0 or len(website) <= 0 or len(email_user) <= 0:
		empty_entry_message = "Please don't leve any fields empty"
		messagebox.showwarning(title="Oops", message=empty_entry_message)
	else:
		# USER INPUT CONFIRMATION POPUP
		confirm_message = f"These are the details entered:\nEmail: {email_user}\nPassword: {password}\n"
		is_ok = messagebox.askokcancel(website, confirm_message)

		if is_ok:
			global my_pass_data
			with open("my_pass_file", "a") as file:
				file.write(f"{website} | {email_user} | {password}\n")
				print(f"{website} | {email_user} | {password}")
			password_input.delete(0, END)
			website_input.delete(0, END)


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
website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

emailUser_input = Entry(width=40)
emailUser_input.grid(column=1, row=2, columnspan=2)
emailUser_input.insert(END, "yourEmailAddress@example.com")

password_input = Entry(width=22, show="*")
password_input.grid(column=1, row=3)

# BUTTON SETUP
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=38, command=save_to_file)
add_btn.grid(column=1, row=4, columnspan=2)

# REQUIRED!! - GUI WINDOW LOOP:
window.mainloop()
