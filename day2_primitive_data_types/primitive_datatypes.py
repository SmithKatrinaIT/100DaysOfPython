"""
Concept: Data types
 -- strings: string of characters
 -- integer (int): whole numbers
 -- float: decimal numbers, int
 -- boolean: True or False <-- not case is important true is not the same a True in Python
"""

# -- Subscripting: use brackets ([]) to get the character at a specific index (counting from zero) of a string
some_string = "Hello World"
char_index_value = some_string[6]
print(char_index_value)
print("Hello"[4])

# --get the number of characters in a string use len(arg) function
print(len(some_string))

# -- quotes around numbers is still a string
print("123" + "456")

# -- number data types do not use quotes
print(5 + 8)

# booleans are used to evaluate truthiness -- where a statement/value is True or False
a = True
b = False
print(a)
print(b)

# Type Conversion
# -- use str(arg) to convert number to string
# -- use int(arg) or float(arg) to convert a string that is a number value to the appropriate number data type

# Data Type exercise
two_digit_number= input("Enter a two-digit number ")
num1 = two_digit_number[0]
num2 = two_digit_number[1]
print(int(num1) + int(num2))

