"""
Concepts: Class inheritance
 -- Class that are related. Inheriting class attributes and methods from a generic class to a more specific class
 -- Establish Class Inheritance
    -- The class to be inherited goes in parenthesis after the class declaration
        class Fish(Animal) <-- Fish class is inheriting from the Animal class
    -- [Recommended by not strictly required] Call the 'super().__init__() method in the sub-class (inheriting class) constructor
        -- def __init__(self):
               super().__init__()
"""
import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)