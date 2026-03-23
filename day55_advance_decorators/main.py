"""
	CONCEPT: Understanding backend website development with Flask

	-- Flask: popular web development framework
		-- Framework is like a library in that its a package of pre-written code you can leverage in your program/application
		-- With libraries, you are in full control when to or not to call a method from that library
		-- With a framework, you have to abide by its rules. You have to use its architecture. You don't call (method call) the code, the framework calls you
        -- Framework for building websites and APIs in Python

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

	-- Variable Rules: adding variable sections to a URL by marking sections with <variable_name
		-- function then receives the <variable_name> as a keyword argument

	    -- Converter:<variable>: converts the variable into the specified data type (i.e. string, int, float, path, uuid)

    -- Decorators with *args and **kwargs
        -- allow for passing arguments to the "wrapped" function
        -- must specify the position of the argument (i.e. arg[2])


    CHALLENGE EXAMPLE

    # TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned: {result}")

        return result
    return wrapper

    
# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1,2,3)


"""

# Flask Minimal Application (structure)
from flask import Flask

app = Flask(__name__) # special attribute: Creates the main app for my website, and name it after this file


#custom decorator chanllenge
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper(*args):
        return "<u>" + func(*args) + "</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
def bye_world():
    return "Bye!"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/username/<name>")
def greeting(name):
    return f"Hello {name}!"



#Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__": # common why to run a Flask application
    app.run() # allows me to use the normal IDE run/stop features instead of `flask run` and setting the Flask environment variable in the terminal