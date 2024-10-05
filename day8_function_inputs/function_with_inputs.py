"""
Concept: Functions with Inputs
 -- Functions are a handy way of taking a complex set of instructions and packaging them together inside a block of code that has a name given to it
 -- Inputs: data that is passed to the function for the code (instructions) to do something with that passed in data (input)
 -- Parameters: is the name of the data (a placeholder variable) -- it is a "reference" to the data passed in
 -- Arguments: is the actual data (value) passed into the function when the function is called
"""


def greet():
    print("Hello")
    print("How do your do?")
    print("Isn't the weather nice today?")


greet()


# Function that allows inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do your do {name}?")


greet_with_name("Katrina")


# Function with more than one parameter
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like {location}?")

greet_with("Jack Bauer", "Nowhere")


# Functional positional arguments using "key-word" arguments; which consists of the parameter name and an equal (=) sign followed by the argument (value)
# When using key-word arguments you can put the inputs in any order; they don't have to be in the same order as the function definition
# in the greet_with() function location is in position two
greet_with(location="London", name="John Smith")