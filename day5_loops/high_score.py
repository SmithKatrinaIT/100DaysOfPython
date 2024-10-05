"""
Lesson 17: High Score (Day 5 concepts)
 -- Loops, Range, and Code Blocks
 -- For Loop: execute the same line of code multiple times
    -- Note indention is very important to escape the loop
"""

# Input a list of student scores
student_scores = input("Enter in a list of whole numbers (Note: separate values by a space only): ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if(score >= highest_score):
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
