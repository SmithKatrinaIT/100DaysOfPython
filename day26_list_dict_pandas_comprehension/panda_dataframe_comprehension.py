""" Concept: Pandas Dataframe Comprehension
    -- how to iterate of Panda Dataframes
    -- Pandas have built-in methods to convert data to dictionaries and lists and more
    --
"""
import pandas

student_dict = {
    "students": ["Katrina", "John", "Zakia", "Jace", "Kemahni"],
    "score": [56, 76, 98, 72, 80]
}

# Python native Looping of dictionaries
for (key, value) in student_dict.items():
    print(key)
    print(value)


#Looping Pandas Dataframe - using Pandas loops
student_dataframe = pandas.DataFrame(student_dict)

#can loop using normal dictionary looping but the data may not be what you are expecting (due to table format of Dataframes)
for (key, value) in student_dataframe.items():
    print(key) # prints the column names (no problem)
    print(value) # prints the indices and the column value as a row of data


# looping the ROWS in the dataframe using Pandas looping method --> .iterrows()
for (index, row) in student_dataframe.iterrows(): # get the row index, and the data in the row
    print(index)
    print(row) # Panda Series
    print(row.students)
    print(row.score)  # get the score in the iterated row



