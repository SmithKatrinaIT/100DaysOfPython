
#for each name in invited_names.txt



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#the string in the starting_letter to replace with the names extracted from the invited_names file
PLACEHOLDER = "[name]"

# `with open()` without any mode "reads" the file line by line (no need for a for loop)
with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
    print(names)



with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()

        # Replace the [name] placeholder with the actual name.
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as invite_letter:
            invite_letter.write(new_letter)

