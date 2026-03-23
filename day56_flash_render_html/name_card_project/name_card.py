#Flask Minimal Application (structure))
from flask import Flask, render_template

#create the Flask application
app = Flask(__name__)


#create the home route of the applicaiton
@app.route("/")
def home():
	return render_template("starter.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)