"""
Concept: Classes, Packages - Object Orient Programming (OOP)
 -- Classes: are blueprints of something (an object). It has specific attributes attributed to it
    -- Name of classes are always Capitalized
    -- Import class syntax: `from <class> import <Class>`
        -- NOTE:
            -- if you only specify `import turtle` you have to use dot notation to create a class object
            -- i.e.
                    import turtle
                    timmy = turtle.Turtle()
"""

from turtle import Turtle, Screen
import prettyTables

# Turtle object
timmy = Turtle()
timmy.shape('turtle')
timmy.color("green")
timmy.forward(100)


# screen object
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

'''
Object Attributes

 -- data
 -- use dot notation to get the object attribute
 -- i.e. car.speed <-- speed is the attribute
'''