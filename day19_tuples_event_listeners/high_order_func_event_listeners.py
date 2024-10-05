"""
Concepts: High order functions and event listeners
 -- Turtle Module: used here to demonstrate High Order Functions and Event Listeners.  It's a geometric drawing tool widely used to demonstrate Python OOP concepts
    -- It uses Tkinter for the underlying graphics
 -- Higher Order Functions
    -- Functions that can work with another function
    -- event listeners require a 'function' call to trigger once the event happens
        -- When using a 'Higher Order function' as an input -- you drop the parenthesis (); it will automatically be invoked when the function calling the H.O Function gets executed
        -- example
            def add(n1, n2):
                return n1 + n2

            def calculator(n1, n2, func): <-- calculator is the higher order function bc it takes in another function
                return func(n1, n2) <-- 'func' get replaced with the name of the function passed in

            calculator(2, 3, add) <-- calculator function with then 'add' the 2 and 3

 -- Events Listeners
    -- actions the user can take with their keyboard or mouse
    -- Listener: we used the 'screen' object  to listen to events
    -- To BIND the keystroke to event in the code, use event listeners


"""
import random
import turtle
from turtle import Turtle, Screen
from random import Random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")



# Control screen behavior
screen = Screen()


def move_forward():
    timmy.forward(10)

def move_back():
    timmy.backward(10)

def move_counter_clockwise():
    timmy.left(45)


def move_clockwise():
    timmy.right(-45)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


# Listen to user events
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear)


screen.exitonclick()
