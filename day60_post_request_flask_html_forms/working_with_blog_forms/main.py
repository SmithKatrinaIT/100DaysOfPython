"""
	CONCEPT: Bootstrap Toolkit (CSS framework)
		-- used to layout and format websites with ease and cut down on the amount css code written manually
		-- One of the most popular External CSS layout systems
			-- pre-build css files that allow the user to specific a specific class to pick up the style in their application
			-- made popular because of its 12 column grid layout structure built on flex box principles
"""
import os

import requests
from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv

# Load ENV variables
load_dotenv("../.env")

SENDER_EMAIL = os.environ.get("TEST_EMAIL")
SENDER_PASSWORD = os.environ.get("TEST_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")
SMTP_ADDRESS = os.environ.get("SMTP_ADDRESS")

headers = {
	"Content-type": "application/json",
}

# Used myjson.online instead of npoint (it was blocked by ISP)
blog_bin_url = "https://api.myjson.online/v1/records/665d3c45-a672-48ea-9a1d-fc1383ff52af"
response = requests.get(blog_bin_url, verify=False, headers=headers)
all_posts = response.json()

post_array = []
for post in all_posts["data"]:
	post_array.append(post)


app = Flask(__name__)

@app.route("/")
def home():

	return render_template("index.html", posts=all_posts['data'])


@app.route("/about")
def about_page():
	return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
	if request.method == "POST":
		contact_form_data = request.form
		# print(contact_form_data['name'])
		# print(contact_form_data['email'])
		# print(contact_form_data['phone'])
		# print(contact_form_data['message'])

		# the object used to connect to smtp server
		with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
			# method of sending email securely - encrypted
			connection.starttls()

			# login to email
			connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)

			#Construct message
			msg_subject = "Site Contact Submission"
			contents = (f"Subject: {msg_subject}\n\n"
						f"The following individual wants to connect!\n\n"
						f"Name: {contact_form_data['name']}\n\n"
						f"Email: {contact_form_data['email']}\n\n"
						f"Phone Number: {contact_form_data['phone']}\n\n"
						f"Message: {contact_form_data['message']}")

			# send email
			connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=TO_EMAIL, msg=f'Subject: {msg_subject}\n\n{contents}')
			print("Email sent successfully")
		return render_template("contact.html", msg_sent=True)

	return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:num>")
def get_post(num):

	print(f'The number passed in from the url_for link in the html file: {num}')

	requested_post = None
	for blog_post in all_posts["data"]:
		if blog_post["id"] == num:
			requested_post = blog_post
	return render_template("post.html", selected_post=requested_post)



if __name__ == "__main__":
	app.run(debug=True)

