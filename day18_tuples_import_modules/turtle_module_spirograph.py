"""
Concepts: Tuples and Importing Modules
 -- Turtle Module: used here to demonstrate Modules and Tuples.  It's a geometric drawing tool widely used to demonstrate Python OOP concepts
    -- It uses Tkinter for the underlying graphics
 -- working with Turtle module to create a Spirograph using circles
"""
import random
import turtle
from turtle import Turtle, Screen
from random import Random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
turtle.colormode(255)
timmy.speed("fastest")

def random_color_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

# modified code from lesson
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color_tuple())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(3)

# My semi-working code
# for _ in range(40):
#     timmy.color(random_color_tuple())
#     timmy.circle(100)
#     timmy.left(10)


# Control screen behavior
screen = Screen()
screen.exitonclick()