"""
Lesson 22 - Grading Program: interprets each students scores - (Day 9 Concepts)
 -- Dictionaries
"""


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# for name in student_scores:
#   if student_scores[name] >= 91:
#     student_grades[name] = "Outstanding"
#   elif student_scores[name] >= 81 and student_scores[name] < 91:
#     student_grades[name] = "Exceeds Expectations"
#   elif student_scores[name] >= 71 and student_scores[name] < 81:
#     student_grades[name] = "Acceptable"
#   elif student_scores[name] <= 71:
#     student_grades[name] = "Fail"

# BETTER WAY TO WRITE THE ABOVE BLOCK OF CODE; because if/else works like a waterfall; if the first condition is false - it checks next conditional in order
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
