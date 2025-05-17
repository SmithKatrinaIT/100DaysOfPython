"""
Lesson 4 : Variables
 -- variables do not have a identifier in front of it like other programming languages
 -- naming variables:
    should be readable and be initiative as to what value is stored within them
    cannot start with a number but can contain numbers
    must be one unit (no spaces), best practice is to separate compound words with an underscore (_)
    should not use Python reserve words like "print", "input"
"""

# There are two variables, a and b from input)
a = input("Enter a value for 'a' ")
b = input("Enter a value for 'b' ")
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
print("You entered " + a + " for a")
print("You entered " + b + " for b")

temp = a
a = b
b = temp

print("a is now " + a)
print("b is now " + b)
