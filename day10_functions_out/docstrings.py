"""
Concept: Docstrings
 -- Documentation describing the function, its parameters, arguments, and expected return (if provided)
 -- docstrings start and end with 3 double quotes (\""") and must be the first line after the colon (:) of the function declaration
 -- NOTE: the 3 double quotes cann also be used for multi-line comments
"""


def format_name(f_name, l_name):
    """
      Take a first and last name and format it to return the title case version of the name.
    """
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} and {formatted_l_name}"


# hovering over the function call -- you can see the 'documentation' provided about the function structure
format_name("Katrina", "Smith")