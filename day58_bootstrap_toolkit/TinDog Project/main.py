"""
	CONCEPT: Bootstrap Toolkit (CSS framework)
		-- used to layout and format websites with ease and cut down on the amount css code written manually
		-- One of the most popular External CSS layout systems
			-- pre-build css files that allow the user to specific a specific class to pick up the style in their application
			-- made popular because of its 12 column grid layout structure built on flex box principles
"""

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")




if __name__ == "__main__":
	app.run(debug=True)