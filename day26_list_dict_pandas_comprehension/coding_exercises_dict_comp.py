"""
    -- Syntax:
        -- Example 1: new_dict = {new_key:new_value for item in list}
            -- basic use: create a new dictionary from a list of key/value pairs
        -- Example 2: new_dict = {new_key:new_value for (key, value) in dict.items()}
            -- advance use - create a dictionary from values in an existing dictionary
"""
"""
    Coding Exercise: Dictionary Comprehension 1 -
    -- You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates
       the number of letters in each word.
    -- Try Googling to find out how to convert a sentence into a list of words.  *

    *Do NOT** Create a dictionary directly.
    -- Try to use Dictionary Comprehension instead of a Loop. To keep this exercise simple, count any punctuation following a word with no whitespace
       as part of the word. Note that "Swallow?" therefore has a length of 8.
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split()
result = {word_dict: len(word_dict) for word_dict in words_list}
print(result)

"""
    Coding Exercise: Dictionary Comprehension 2
    -- You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts
       it into degrees Fahrenheit. 
    -- To convert temp_c into temp_f use this formula:  (temp_c * 9/5) + 32 = temp_f
"""
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)

"""
    Coding Exercise: 
"""



