"""
Concepts: Understanding the Turtle coordinate system
 -- Turtle Module: used here to demonstrate High Order Functions and Event Listeners.  It's a geometric drawing tool widely used to demonstrate Python OOP concepts


"""
import random
import turtle
from turtle import Turtle, Screen
from random import Random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: " )
colors = ["red", "green", "yellow", "purple", "blue", "orange"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

# modified code
for index in range(0,6):
    timmy = Turtle(shape='turtle')
    timmy.color(colors[index])
    timmy.penup()
    timmy.goto(-230, y_positions[index])
    all_turtles.append(timmy)


is_race_on = False
if user_bet:
    is_race_on = True


random.randint(0, 10)
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



# ----------------------------------------

def create_turtle(color, x, y):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x, y)

# create_turtle(colors[0], -225, 0)
# create_turtle(colors[1], -225, -50)
# create_turtle(colors[2], -225, -100)
# create_turtle(colors[3], -225, 50)
# create_turtle(colors[4], -225, 100)



screen.exitonclick()
