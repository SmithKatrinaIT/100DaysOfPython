"""
Lesson 6: BMI Calculator to see if someone is over, under weight (Day 2 concepts)
 -- datatypes, typeError, mathematical operators
"""

# 1st input: enter height in meters e.g: 1.65)
print("This program will calculate your BMI using US customary system\n****************************************\n")
height = input("Enter height in inches: ")
# 2nd input: enter weight in inches e.g: 61
weight = input("Enter weight in pounds: ")

height = float(height)
weight = int(weight)
bmi = 703 * (weight / (height ** 2))
bmi = int(bmi)
print(f"Your BMI is: {bmi}")
