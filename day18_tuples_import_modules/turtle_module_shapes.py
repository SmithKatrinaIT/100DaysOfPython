"""
Concepts: Tuples and Importing Modules
 -- Turtle Module: used here to demonstrate Modules and Tuples.  It's a geometric drawing tool widely used to demonstrate Python OOP concepts
    -- It uses Tkinter for the underlying graphics
 -- Modules
    -- Basic Import syntax: import moduleName
    -- Best Practice Import syntax: from moduleName import thing_in_the_module
    -- Import all syntax: import moduleName import *
        -- the asterix imports every thing_in_the_module; not best practice
            as a developer may not be able to tell where a piece of code
            is derived from
            i.e. using choice([1,2,3]) instead of random.choice([1,2,3])
    -- Aliasing Modules: used when Module name is quite long:
        -- Alias Name syntax: import turtle as t
        -- ie. tim = t.Turtle()

    -- Installing Modules: some modules (like Turtle) are pre-package in python standard library code;
        they are therefore ready to use with any project out of the gate;
        For modules not already bundled with Python, you have to install them from Python Packages (hosted
        on the internet.  This allows you to only add the packages you need.
        --When a package is installed it is stored in the virtual environment (.venv) on a project
            by project bases.
"""
import random
from turtle import Turtle, Screen
from random import Random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon

# triangle
# for _ in range(3):
#     timmy.forward(150)
#     timmy.right(360/3)
#
# # square
# for _ in range(4):
#     timmy.forward(150)
#     timmy.right(360/4)
#
# # pentagon
# for _ in range(5):
#     timmy.forward(150)
#     timmy.right(72)
#
# # hexagon
# for _ in range(6):
#     timmy.forward(150)
#     timmy.right(360/6)
#
# # heptagon
# for _ in range(7):
#     timmy.forward(150)
#     timmy.right(360/7)
#
# # octagon
# for _ in range(8):
#     timmy.forward(150)
#     timmy.right(360/8)
#
# # nonagon
# for _ in range(9):
#     timmy.forward(150)
#     timmy.right(360/9)
#
# # decagon
# for _ in range(10):
#     timmy.forward(150)
#     timmy.right(360/10)

# reformated code into a function

color_list = ["light sky blue", "red", "green", "yellow", "purple", "pink", "orange", "black", "brown", "salmon", "coral", "lavender", "goldenrod", "navy"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides

        timmy.forward(100)
        timmy.right(angle)


for shape_sides in range(3, 11):  # 11 range value is not inclusive; so for loop will create shapes upto decagon (10 sides)
    timmy.color(random.choice(color_list))
    draw_shape(shape_sides)

# Control screen behavior
screen = Screen()
screen.exitonclick()