"""
Lesson 16: Average Height: (Day 5 concepts)
 -- Loops, Range, and Code Blocks
 -- For Loop: execute the same line of code multiple times
    -- Note indention is very important to escape the loop
"""

# Input a Python list of student heights
student_heights = input("Enter height in inches for everyone - (Note: separate values with a space only): ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
num_students = 0
for height in student_heights:
    num_students = num_students + 1
    total_height += height
average_height = total_height / num_students

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {round(average_height)}")

