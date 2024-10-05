"""
Concepts: Tuples and Importing Modules
 -- Turtle Module: used here to demonstrate Modules and Tuples.  It's a geometric drawing tool widely used to demonstrate Python OOP concepts
    -- It uses Tkinter for the underlying graphics
 -- Tuples
    -- Immutable data structure in Python. The values can not be modified
    -- syntax: (1,2,3) <-- an ordered list that uses parenthesis
    --
"""
import random
import turtle
from turtle import Turtle, Screen
from random import Random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")


color_list = ["light sky blue", "red", "green", "yellow", "purple", "pink", "orange", "black", "brown", "salmon",
              "coral", "lavender", "goldenrod", "navy"]

# reformated random color; import colormode from 'turtle' module
# colormode used to set the color in ('r, g, b') format <-- which in Python is a tuple
# 255 - gives all possible color combinations
turtle.colormode(255)

direction = [0, 90, 180, 270]

def random_color_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk():
    timmy.width(10)
    timmy.speed(8)
    for i in range(200):
        # timmy.color(random.choice(color_list))
        # timmy.color(random.randint(0, 255), random.randint(1, 255), random.randint(1, 255))
        timmy.color(random_color_tuple())
        timmy.setheading(random.choice(direction))
        timmy.forward(20)


random_walk()

# Control screen behavior
screen = Screen()
screen.exitonclick()
