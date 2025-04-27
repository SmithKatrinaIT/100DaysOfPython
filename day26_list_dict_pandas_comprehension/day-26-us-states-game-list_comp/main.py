"""Exercise: Build a U.S. States Quiz Game using Pandas and Turtle Libraries"""

import turtle
from turtle import Turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


""" U.S. State Quiz """

# Get the names of the states and create a Python List data structure with it
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    # creates a popup modal on the screen. Takes in a title and a prompt
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Enter your guess").title()  # .title() used by instructor

    #breakout of loop control
    if answer_state == "Exit":
        # missing_states = []
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        # Using List Comprehension instead of the above code
        missing_states = [state for state in states_list if state not in guessed_states]

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # Check if user named the state correctly
    if answer_state in states_list:

        # Create a new `turtle` that will write to the correct state to the screen
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        guessed_states.append(answer_state)
        data_state = data[data.state == answer_state]
        t.goto(data_state.x.item(), data_state.y.item())

        # Write correct guesses onto the map
        t.write(answer_state, font=('Courier', 14, 'bold'))
