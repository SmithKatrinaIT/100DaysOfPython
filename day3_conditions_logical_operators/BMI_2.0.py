"""
Lesson 9: BMI Calculator to see if someone is over, under weight (Day 3 concepts)
 -- if/else statement
"""

# 1st input: enter height in meters e.g: 1.65)
print("This program will calculate your BMI using US customary system\n****************************************\n")
height = float(input("Enter height in inches: "))
# 2nd input: enter weight in inches e.g: 61
weight = int(input("Enter weight in pounds: "))


# Your code below this line 👇
bmi = 703 * (weight / (height * height))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
