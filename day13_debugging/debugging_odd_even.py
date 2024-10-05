"""
Lesson 25 - Debugging Odd or Even - (Day 13 concepts)
 -- Debugging
"""

number = int(input("Which number do you want to check? "))  # Which number do you want to check?

# if number % 2 = 0: # error; doing assignment not comparison
if number % 2 == 0:  # fix
    print("This is an even number.")
else:
    print("This is an odd number.")
