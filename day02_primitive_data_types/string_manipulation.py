"""
Concept: String/Data Manipulation
 -- altering the results of a specific data type for a particular use case
 -- round() function
 -- floor operator (//)
 == shorthand operations to manipulate data values: +=, -=, /=, *=
 == f-strings: allows for mixed data types to be included in a string/print statement
"""

# round a decimal number to a specified number of places
print(8/3) # yields 2.6666666666666665
print(int(8/3))  # yields 2 -- which converts to a whole number but does not round up/down

# Use the round() function to round a decimal value up or down
print(round(8 / 3))  # yields 3 -- automatically rounds to the nearest whole number

# Can Pass in the number of decimal places to round to as an argument to the function
print(8 / 3, 2)  # yields 2.67

# Use the floor operation (//) - double forward slashes. Floor operation will convert and round down to nearest whole number
print(8 // 3)  # yields 2

'''
Use f-strings when you need to concatenate different data types in a string. Alternative would be to convert all values to the SAME data type first/
f-strings require the character 'f' in front of the quotes of the string and to incase the variable (if not a string) in curly braces {}
e.g.
  -> score = 1
  -> print(" Your score is " + str(score) + "!")
'''

score = 0
score += 1
height = 61.5
isWinning = True

#
print(f" Your score is {score}. Your height is {height}. You are is {isWinning}")

