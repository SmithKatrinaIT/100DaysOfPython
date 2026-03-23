import random
# Flask Minimal Application (structure)
from flask import Flask

app = Flask(__name__)


# Decorator functions
def center_align(func):
    def wrapper():
        return "<div style='text-align:center;'>" + func() + "</div>"
    return wrapper


# Application Endpoints - API Calls
@app.route("/")
@center_align
def home():
    return "<h1>Guess a number between 1 and 9:</h1>" \
           "<img style='width:250; height:250;' src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXFjdzUwaG85bGM1bzQweHZsY2w4NHhmaG9uYnNhNDgzMTExd3RqZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wH4rY2nPnEnp6/giphy.gif' alt='question marks gif'/>"

@app.route("/guess/<int:number>")
def guess_number(number):
    random_guess = random.randint(1, 10)

    if number > random_guess:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif number < random_guess:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
           "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
           "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"



# Run the application code
if __name__ == "__main__": # common why to run a Flask application
    app.run(port=5001, debug=True)




