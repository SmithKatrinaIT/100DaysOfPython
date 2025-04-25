"""
Concept: Files, Directories, Paths
 -- `open()`: from Python builtins; ships automatically with Python
    -- if using `open()` alone, also need to 'close()' the file to free up resources; avoid memory leaks
 -- `with open() as varibleName`: eliminates the need to remember to use 'close()' to close the resources
 -- mode: specify the mode of operaton: 
    -- 'r' == read <-- readOnly mode
    -- 'w' == write <-- used alone will override the existing text in the file. Will also create the
                        specified file if not already created.  So no need to create beforehand
    -- 'a' == append <-- this will appead new text to last line of the file
 -- `write()`: write to the file
"""

# using open() alone
file = open("my_file.txt")
content = file.read()
print(content)

file.close()


# using `with open() as variableName`
with open("my_file.txt") as file:
    content = file.read()
    print(content)
    

# using write() to write to the file
with open("my_file.txt", mode='w') as file:
    file.write("Some new text to add to the file")
    
# using write() in 'a' - append mode to write to the file
with open("my_file.txt", mode='a') as file:
    file.write("\nAppended text to add to the file")   
   
# using write() to write to and create a file
with open("new_file.txt", mode='w') as file:
    file.write("Some text to add to a newly created file")
   