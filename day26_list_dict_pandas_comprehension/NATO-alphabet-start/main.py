student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Create a dictionary in this format:   {"A": "Alfa", "B": "Bravo"}

nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_dict = input("Enter a word: ").upper()
phonetic_list = [nato_dict[letter] for letter in word_dict]

print(phonetic_list)

