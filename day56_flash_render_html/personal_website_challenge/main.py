"""
	CONCEPT: Rendering static files and downloadable html templates for a Flask application

	--Code Nugget:
		-- Edit a HTML file from the browser using ChromeDeveloper tools
			-- Command:
				document.body.contentEditable=true

				**** allows user to edit the html file in the inspect tool (delete, add, modify)
				--editing in the browser is a temporatory change
				-- you can stay the .htm file and upload to your files served on the server for the changes to be effective

"""

#Flask Minimal Application (structure))
from flask import Flask, render_template

#create the Flask application
app = Flask(__name__)


#create the home route of the applicaiton
@app.route("/")
def home():
	return render_template("starter.html")


if __name__ == "__main__":
    app.run(port=5001, debug=True)