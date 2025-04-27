""" Concept: Dictionary Comprehension
    -- Simplifies working with or creating dictionaries
    -- NOTE: Dictionary Comprehension uses CURLY BRACKETS instead of square (like lists)
    -- Syntax:
        -- Example 1: new_dict = {new_key:new_value for item in list}
            -- basic use: create a new dictionary from a list of key/value pairs
        -- Example 2: new_dict = {new_key:new_value for (key, value) in dict.items()}
            -- advance use - create a dictionary from values in an existing dictionary

        -- Syntax
            -- new_dict: is the dictionary to create
            -- new_key: the key variable to save in the new dictionary
            -- new_value: the value variable that correlates to the key variable to save in the new dictionary
            -- for: keyword
            -- item: variable of the item in the list being iterated over (this can be called any acceptable variable name)
            -- (key, value): split the items in the dictionary to iterate over, into a key (variable) and value (variable) pair
            -- in: keyword
            -- list: the list to iterate over
            -- dict.items(): all the items in the dictionary being iterated over
    -- Syntax: conditional
        -- new_dict = {new_key:new_value for item in list if test}
        -- new_dict = {new_key:new_value for (key, value) in dict.items() if test}
            -- new_key, new_value, (key, value), for, item, in, list, dict.items() are the same above
            -- if: keyword
            -- test: the conditional expression.
"""
import random

# Dictionary Comprehension: create a new dictionary with names of students and their scores
names = ["John", "Katrina", "Jace", "Kia", "Kemahni", "Dawn", "Angie", "Tasha", "Pete"]
student_dict = {name: random.randint(1, 100) for name in names}


passed_students = {student: score for (student, score) in student_dict.items() if score > 69}
print(student_dict)
print(passed_students)