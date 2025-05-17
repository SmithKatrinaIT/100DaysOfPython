"""
    Concept: Advance Arguments
    -- *args: allows unlimited arguments
        -- returns a tuple
        -- also referred to as 'positional unlimited arguments" because the position of the data in the tuple matters
        -- can reference the index or position of the tuple of arguments
            -- e.g args[1]
        -- **kwargs: keyword arguments or a dictionary
            -- allows keywords and values
"""

# Keyword arguments
def my_function(a, b, c):
    #Do this with a
    #Do this with b
    #Do this with c
    pass
#Arguments with Default Values
def my_function2(a=1, b=2, c=3):
    #Do this with a
    #Do this with b
    #Do this with c
    pass

# Unlimited Arguments:
def add(*args):

    #accessing a position in the tuple
    print(args[1]) # should return 5
    sum = 0
    for n in args:
        sum += n
    return sum

# Unlimited Keyword arguments (kwargs)
def calculate( **kwargs):
    print(kwargs)

    #loop thru the kwargs
    for key, value in kwargs.items():
        print(key)
        print(value)

def calculate2(n, **kwargs):
    # kwargs provides more flexibility when dealing with an unlimited number of arguments
    n += kwargs["add"]  # get the value of the dictionary key "add"
    n *= kwargs["multiply"]  # gets the value of the dictionary key "multiply"
    print(n)

# *args
print(add(3, 5, 6, 3, 5, 8, 1, 9))

# **kwargs
print(calculate(add=3, multiply=5))
# returns {'add': 3, 'multiply': 5 } <-- a dictionary

print(calculate2(2, add=4, multiply=5))
#should return n as 30