"""
Concept: Files, Directories, Paths
 -- `open()`: from Python builtins; ships automatically with Python. Returns a File Object
    -- if using `open()` alone, also need to 'close()' the file to free up resources; avoid memory leaks
 -- `with open() as variableName`: eliminates the need to remember to use 'close()' to close the resources
 -- mode: specify the mode of operation:
    -- 'r' == read <-- readOnly mode
    -- 'w' == write <-- used alone will override the existing text in the file. Will also create the
                        specified file if not already created.  So no need to create beforehand
    -- 'a' == append <-- this will append new text to last line of the file
    -- 'x' == create <-- create the specified file, returns an error if the file exists
    -- 't' == text <-- default and does not need to be specified
    -- 'b' == binary <-- used for binary files like images
 -- `fileObj.read()`: read the contents of the file (each line --- no need for a for loop)
 -- `fileObj.read(5): specify a number parameter, it reads part of the file. reads first 5 characters of the file
 -- `write()`: write to the file
 -- `fileObj.readlines(): reads one line at a time
"""

# using open() alone
#file = open("my_file.txt")
# file = open("/Users/ksmith12/Desktop/my_file.txt")  #using file absolute paths
file = open("../../../../../Desktop/my_file.txt")  #using file relative paths
content = file.read()
print(content)

file.close()


# using `with open() as variableName`
# `with open() as variableName`: eliminates the need to remember to use 'close()' to close the resources
#with open("my_file.txt") as file:
with open("/Users/ksmith12/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)
    

# using write() to write to the file -- will create the file if it doesn't exist already
#with open("my_file.txt", mode='w') as file:
with open("/Users/ksmith12/Desktop/my_file.txt", mode='w') as file:
    file.write("Some new text to add to the file")
    
# using write() in 'a' - append mode to write to the file
#with open("my_file.txt", mode='a') as file:
with open("/Users/ksmith12/Desktop/my_file.txt", mode='a') as file:
    file.write("\nAppended text to add to the file")   
   
# using write() to write to and create a file -- will create the file if it doesn't exist already
with open("new_file.txt", mode='w') as file:
    file.write("Some text to add to a newly created file")
   