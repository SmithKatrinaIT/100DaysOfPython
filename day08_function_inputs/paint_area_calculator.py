"""
Lesson 20: Paint Area Calculator - calculate the number of paint cans required to pain a surface area(Day 8 Concepts)
 -- Concept: Functions with Inputs
"""

# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
  coverage = math.ceil((height * width) / cover)
  print(f"You'll need {coverage} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.


# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)