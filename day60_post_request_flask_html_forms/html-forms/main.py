"""
	CONCEPT: Capturing Form Data using Flask and HTML
		--
"""

from flask import Flask, render_template, request



app = Flask(__name__)

@app.route("/")
def home():

	return render_template("index.html")


@app.route("/login", methods=["POST"])
def login_data():

	user_obj = {
		'username': request.form['username'],
		'password': request.form['password']
	}

	return render_template("login.html", user=user_obj)



# RUN APP

if __name__ == "__main__":
	app.run(debug=True)