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
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
turtle.colormode(255)
timmy.speed("fast")

"""
    Used to extract 30 RGB colors values from an image
    Extracted colors then saved to a list
"""
# colors = colorgram.extract("image.jpg", 30)
# color_options = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_options.append(new_color)

color_list = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]

# TODO: 10 x 10 random color grid
timmy.penup()
timmy.setheading(215)
timmy.forward(300)
timmy.setheading(0)
timmy.hideturtle()

number_of_dots = 100


def draw_hirst(space_between_dots, dots_in_grid):
    for i in range(dots_in_grid):
        for j in range(dots_in_grid):
            timmy.dot(15, random.choice(color_list))
            timmy.forward(space_between_dots)

        # move back to beginning of line
        timmy.setheading(90)
        timmy.forward(space_between_dots)
        timmy.setheading(180)
        timmy.forward(space_between_dots * dots_in_grid)
        timmy.setheading(0)



# for dot_count in range(1, number_of_dots + 1):
#     timmy.dot(15, random.choice(color_list))
#     timmy.forward(50)
#
#     if dot_count % 10 == 0:
#         timmy.setheading(90)
#         timmy.forward(50)
#         timmy.setheading(180)
#         timmy.forward(500)
#         timmy.setheading(0)

draw_hirst(50, 10)
#print(timmy)

# Control screen behavior

screen = Screen()
screen.exitonclick()