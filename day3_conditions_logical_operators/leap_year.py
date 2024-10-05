"""
Lesson 10: Leap Year
 -- Control Flow with if/else and Conditional Operators
"""
# Which year do you want to check?
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
             print("Yes, a Leap year")
        else:
             print("No, not a leap year")
    else:
        print("Yes, a Leap year")
else:
    print("No, not leap year")
