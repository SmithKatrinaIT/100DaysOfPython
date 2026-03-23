"""
	CONCEPT: URL Building and Templating with Jinja
	-- Jinja: templating language for Python
		-- already bundled with the Flask framework
		-- modelled after the Django's templates
		-- Accepts specific syntax to render Python code from the HTML file

			Jinja (Gen-Ga) Syntax:
				-- Double Curly braces expression:  {{ something }}
					-- will evaluate the expression inside and render it to the page
				-- Percent Symbol: {% something %}
					-- used for inserting control flow statements (if/else statements, for loops)
						-- used when specifying code that spans multiple lines
					-- With "for loops": end the code block with `endfor` keyword: {% endfor %}
					-- With "if/else" statements: end the code block with `endif` keyword

	-- URL building:
		-- Allows for directing a user to a specific page (or api endpoint) within the website/web app
		-- Build out the href of a link with the `url_for` keyword expression: (i.e. href={{ url_for('nameOfFunction') }}
			-- url_for(func) takes in the name of a function or endpoint route to redirect the user to
				-- Example: href="{{ url_for('get_blog') }}" -- get_blog is the name of the function for the app.route(/blog) page/endpoint
		-- Can pass keyword arguments as well to  url_for() expression
			-- example: <a href="{{ url_for('get_blog', num=3) }}"
"""
import requests
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
	date_year = datetime.datetime.now().year
	return render_template("starter.html", year=date_year)

@app.route("/guess/<name>")
def age_guess(name):
	gender_url = f"https://api.genderize.io?name={name}"
	gender_response = requests.get(gender_url)
	gender_data = gender_response.json()
	gender = gender_data["gender"]


	age_url = f"https://api.agify.io?name={name}"
	agify_response = requests.get(age_url)
	agify_response.raise_for_status()
	age_result = agify_response.json()
	age = age_result["age"]

	return render_template("guess.html", person_name=name, person_gender=gender, person_age=age)


@app.route("/blog")
def blogs():
	headers = {
		"Content-type": "application/json",
	}

	# Used myjson.online instead of npoint (it was blocked by ISP)
	blog_bin_url = "https://api.myjson.online/v1/records/f9fd64cd-0481-46e6-addb-9e3fd0fc92d2"
	response = requests.get(blog_bin_url, verify=False, headers=headers )
	all_posts = response.json()

	return render_template("blog.html", posts=all_posts["data"])

@app.route("/blog/<num>")
def get_blog(num):
	headers = {
		"Content-type": "application/json",
	}

	print(f'The number passed in from the url_for link in the html file: {num}')

	blog_bin_url = "https://api.myjson.online/v1/records/f9fd64cd-0481-46e6-addb-9e3fd0fc92d2"
	response = requests.get(blog_bin_url, verify=False, headers=headers )
	all_posts = response.json()

	return render_template("blog.html", posts=all_posts["data"])


if __name__ == "__main__":
	app.run(debug=True)

