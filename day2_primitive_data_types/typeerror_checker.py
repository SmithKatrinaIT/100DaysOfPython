"""
Concept: Solving for TypeErrors
"""

# use 'type(arg) function for any piece of data you want to check its data type
num_char = len(input("What is your name? "))

# this will throw a TypeError because 'num_char' is a number and not a string
# print("Your name has " + num_char + " characters")

print(type(num_char))

# # Type Conversion
# # -- use str(arg) to convert number to string
# # -- use int(arg) or float(arg) to convert a string that is a number value to the appropriate number data type
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters") # does not throw typeError

a = str(123)
print(type(a))

b = float(123)
print(type(b))

# what data type will this produce
print(70 + float(100))
print(str(70) + str(100))
