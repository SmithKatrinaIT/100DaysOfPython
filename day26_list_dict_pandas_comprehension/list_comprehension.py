""" Concept: List Comprehension
    -- Simplifies working with Python Sequences:
        -- List, Range, String, Tuple
    -- Can be a simple List Comprehension or a Conditional List Comprehension
        -- With Conditional List Comprehension, if the conditional is not met, the new_item won't get created in the new_list
    -- Syntax: simple
        -- new_list = [new_item for item in list]
            -- new_list: is the list to create
            -- new_item: the new item or expression to add to the new list
            -- for: keyword
            -- item: variable of the item in the list being iterated over (this can be called any acceptable variable name)
            -- in: keyword
            -- list: the list to iterate over
    -- Syntax: conditional
        -- new_list = [new_item for item in list if test]
            -- new_item, for, item, in, list: are the same above
            -- if: keyword
            -- test: the conditional expression.
    -- Example: Syntax for a string list
        -- name = "Katrina"
        -- letters_list = [letter for letter in name]
            Result: ["K", "a", "t", "r", "i", "n", "a"]
    -- Example:
        -- numbers = [1, 2, 3]
        -- new_numbers = [num +1 for num in numbers]
            Result: [2, 3, 4]
"""

#native way to add items to a list
numbers = [1, 2, 3]  # list to iterate over

new_list = []  # new list to be created and have items be added
for num in numbers:  # num is the variable
    add_1 = num + 1  # `num +1` is the expression of item to add to the new list
    new_list.append(add_1)  # item appended to the new list

# Using List Comprehension
new_list_comp = [n + 1 for n in numbers]
# Should Result In: [2, 3, 4]
print(f"New Numbers: {new_list_comp}")

# Challenge: loop through a range[1,5] and double the values
new_range = [num * 2 for num in range(1, 5)]
# Should Result In: [2, 4, 6, 8]
print(f"New Range: {new_range}")

# Using List Conditional List Comprehension
names = ["John", "Katrina", "Jace", "Kia", "Kemahni", "Dawn", "Angie", "Tasha", "Pete"]
short_names = [name for name in names if len(name) < 5]
# Should Result In: ["John", "Jace", "Kia", "Dawn", "Pete"
print(f"Short Names: {short_names}")

#Challenge: create a new list of names whos length is greater than 5 and capitalize all the letters in the name -- using the `names` list above
long_names = [name.upper() for name in names if len(name) > 4]
# Should Result In: ["KATRINA", "KEMAHNI", "ANGIE", "TASHA"]
print(f"Capitalized Long Names: {long_names}")
