"""
Lesson 26 - Debugging Leap Year determination - (Day 13 concepts)
 -- Debugging
"""

# Which year do you want to check?
#year = input("Which year do you want to check? ") # error; not converting to a number for below comparison
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")