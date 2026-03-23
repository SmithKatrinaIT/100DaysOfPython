"""
	CONCEPT: ADDING HTML FILES TO THE APPLICATION
		-- how to render html in the Flask application
		-- Always refer to the official documentation when in doubt
			-- Create an HTML file
				-- NOTE: HTML file must be in a directory/folder called `templates` for Flask to pick it up
			-- Use `render_template()` method
				-- import render_template method from the Flask framework
				-- call the method for the function


		--Render static files: images, css files, etc


"""


# Flask Minimal Application (structure)
from flask import Flask, render_template

#create the Flask application
app = Flask(__name__)


#create the home route of the applicaiton
@app.route("/")
def home():
	# return "Hello World"
	return render_template("starter.html")



# Run the application code --common way to run a Flask application using ide instead of using the commandline/script
if __name__ == "__main__":
    app.run(port=5001, debug=True)