"""
Concept: Dictionaries
 -- Dictionaries: allow for grouping together and tagging related pieces of information
 -- Each dictionary has a "key" and a "value" (mush like the 'map' data structure in other languages.
 -- Key: is like the word in the dictionary and its also got an associated value - the Value
 -- Value: Is the 'key's associated value - much like the definition of a word in the dictionary
 -- Syntax: {Key: Value}
    -- to add more than one "element" to the dictionary, separate the {Key: Value} pairs with a comma (,)
    --Fetch 'Key' and it value
      -- dictionary_name["Key"] - the dictionary name followed by square brackets containing the key name
"""

# declare a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Extract the Key and Value (an item/element) from the Dictionary
print(programming_dictionary["Bug"])

# Add new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Declaring an empty dictionary
empty_dictionary = {}

# Wiping out the contents of an existing dictionary; re-declare it as an empty dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary; redefine the Key's currently store value
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing) # only prints out the Key; unexpected results

for key in programming_dictionary:
    print(key)  # only prints out the Key Name
    print(programming_dictionary[key])  # prints out the value associated with the key




