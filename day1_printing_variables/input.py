"""
Lesson 3: input() function - used to prompt user type in some text (string) that gets passed back into the program
-- use input() without any arguments will give the user a prompt to type in text from keyboard
-- use input("some string") will display the text before give the user a prompt to type in text
"""
"""
NOTE: Python does not allow mix data types to be concatenated in a print statement
must use 'f' string formating to use multiply data types in a print statement
"""
name = input("What is your name? ")

# len() function give you the number of letters are in a string
numOfLetter = len(name)

# This line of code will throw a "type" error --> print("There are " + numOfLetter + "letters in your name")
print(numOfLetter)
