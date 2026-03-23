"""
	CONCEPT: Understanding backend website development with Flask

	-- Full-stack: Frontend and backend technologies
		-- Frontend: HTML, CSS, Javascript
		-- Backend: programming languages like, Python, Java, Ruby, Pearl, etc
		-- Frameworks:
			-- prebuild code to help complete common functionality easily instead of creating the functionality from scratch each time

	--What is the Backend (laymen terms)
		-- 3 Components
			-- Client: user going onto the internet; the part that faces the user (laptop, desktop, phone, tablet, etc..)
			-- Server: powerful computer connected to the internet; always on, ready to send and receive requests
			-- Database: super spreadsheet of stored information about a website

	-- Flask: popular web development framework
		-- Framework is like a library in that its a package of pre-written code you can leverage in your program/application
		-- With libraries, you are in full control when to or not to call a method from that library
		-- With a framework, you have to abide by its rules. You have to use its architecture. You don't call (method call) the code, the framework calls you

		--Flask documentation: https://flask.palletsprojects.com/en/stable/
		    -- Create the development server by setting the FLASK_APP environment variable:
		    -- Point the file (code) to the FLASK_APP: `export FLASK_APP=main.py`
		        -- NOTE: MAKE SURE TO RUN/CREATE THE FLASK_APP in the right directory if working with multiple files and directories in your IDE
		    -- In the terminal run the command: flask run to start up the server

	-- @app.route: @ is a Python decorator
	    -- Decorator: a function that wraps another function and gives that function some additional functionality
	        -- How to create a decorator function
	            -- create a normal function (outer function)
	            -- create a nested function inside the 1st function (inner function)


	-- First-Class functions: Functions are first class functions; they can be passed around as arguments e.g int/string/float, etc
	    -- example:
	        def divide(n1, n2):
	            return n1 / n2

	        def calculate(cal_func, n1, n2):
	            return calc_func(n1, n2)

	        result = calculate(divide, 2, 3)
	        # `divide()` function is being passed to the `calculate()` function as an argument
	            -- note: when passing a function as an argument in another function - you leave off the parenthesis

	-- Nested Functions:
	    ex: def outer_func():
	            print("I'm outer")

	            def nested_func():
	                print("I'm inner")

	            nested_func() # this function can only be called withing the outer function
	            -- calling the outer function can be called outside the outer function and will result in the outer print statement and the nested function
	               print statement to execute

	-- Functions can be returned from other functions
	     ex: def outer_func():
	            print("I'm outer")

	            def nested_func():
	                print("I'm inner")

	         return nested_func

	    inner_func = outer_func() # prints "I'm outer"
	    inner_func() # prints "I'm inner"


"""

# Flask Minimal Application (structure)
from flask import Flask

app = Flask(__name__) # special attribute:

""" print(__name__) will return "__main__" 
Every Python file (module) has a variable called __name__.
If you run the file directly (e.g., python app.py), then __name__ is set to "__main__".
If the file is imported by another file (e.g., import app), then __name__ is set to the module’s actual name (e.g., "app").
__name__ is like the return address on a package.
Flask uses it to know where the app comes from, so it can find related files and report issues accurately.

"""
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__": # common why to run a Flask application
    app.run() # allows me to use the normal IDE run/stop features instead of `flask run` and setting the Flask environment variable in the terminal


