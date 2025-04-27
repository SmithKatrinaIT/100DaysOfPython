"""Exercise: Build a U.S. States Quiz Game using Pandas and Turtle Libraries"""

import turtle
from turtle import Turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Quiz Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

t = Turtle()
t.penup()

#-270.0 -189.0

""" Bonus Info: How to extract x,y coordinates on mouse click to get the coordinates on the U.S. States map image fro the quiz game
    --Note: a csv file was provided with this challenge that has the state coodinates as long a you don't adjust the size of the image
"""
def get_mouse_click_coor(x,y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


""" U.S. State Quiz """

# Get the names of the states and create a Python List data structure with it
data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
states_x_coor_list = data.x.to_list()
states_y_coor_list = data.y.to_list()


""" My solution: Quiz/Game ends with a wrong guess """
# # Establish game controls
# game_over = False
# # Keep track of correct guesses
# num_correct_guesses = 0
# # Save correct guesses in a List
# correct_guesses = []

""" Course solution: Quiz/Game ends with 'Exit' control """
guessed_states = []


#while not game_over: # my solution control

while len(guessed_states) < 50:

    # creates a popup modal on the screen. Takes in a title and a prompt
    # answer_state = screen.textinput(title=f"{num_correct_guesses}/50 States Correct", prompt="Enter your guess").capitalize()   #.title() used by instructor

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Enter your guess").title()  # .title() used by instructor

    #breakout of loop control
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)

        # states to learn: create a csv of the states user didn't guess as a learning tool
        # My solution: this also works and shorter code
        # missed_states = list(set(states_list) - set(guessed_states))

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break

    # Check if user named the state correctly
    if answer_state in states_list:
        # num_correct_guesses += 1
        # correct_guesses.append(answer_state)
        guessed_states.append(answer_state)

        data_state = data[data.state == answer_state]

        """  My solution: Note returns a warning about casting Panda series data to int()
            #state_coor_x = data_state.x  
            #state_coor_y = data_state.y
            #t.goto(int(state_coor_x), int(state_coor_y)) 
        """
        t.goto(data_state.x.item(), data_state.y.item())
        t.write(answer_state, font=('Courier', 14, 'bold'))

    """ Not necessary in course requirements """
    # else:
    #     t.goto(-200,-50)
    #     t.write("GAME OVER", font=('Courier', 80, 'bold'))
    #     t.goto(-250, -100)
    #     t.write(f"You named {num_correct_guesses} states correctly.", font=("Courier", 30, 'normal'))
    #     game_over = True

#print(f"total correct guess: {num_correct_guesses}")


# states_to_learn_dataframe = pandas.DataFrame(states_to_learn)
# states_to_learn_dataframe.to_csv("states_to_learn.csv")


#TODO: Write correct guesses onto the map


# alternative way to keep the screen open
turtle.mainloop()
