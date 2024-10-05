"""
Concept: Functions with Outputs
 -- Functions are a handy way of taking a complex set of instructions and packaging them together inside a block of code that has a name given to it
 -- Outputs: allow for an output [a result] from executing the function - it returns something after completing its instructions (executions)
 -- outputs are identified by the keyword 'return' before stating what should be returned by the function [the result]
 -- Can have multiple 'return' statements or an empty 'return' statement in a function
    -- normally used to exit a conditional statement or exit a loop within a function
    -- Empty 'return' statements will return 'none' to the console meaning no value was set to return; so best practice is to return a meaningful message instead.
"""


def format_name(f_name, l_name):
    # str.title method will capitalize the first letter of every word in a string; str.capitalize() works as well
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} and {formatted_l_name}"


formatted_string = format_name("katrina", "smith")
print(formatted_string)


def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":

        # empty return
        return
    else:

        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"{formatted_f_name} and {formatted_l_name}"


# call the function in a print statement
print(format_name2(input("What is your first name? "), input("What is your last name?: ")))
