"""
Lesson 8: Check if number is odd or even with if/else statement
"""
# Which number do you want to check?
number = int(input("Enter a number between 1 - 100"))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number = float(number)
if(number % 2 == 0):
  print("This is an even number.")
else:
  print("This is an odd number.")
