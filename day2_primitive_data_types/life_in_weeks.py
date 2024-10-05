"""
Lession 7: Life in Weeks calculator
 -- string manipulation, f-strings
"""

age = input("What is your age? ")
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
