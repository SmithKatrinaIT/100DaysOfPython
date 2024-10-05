"""
Concepts: Loops, Range
 -- For Loop: execute the same line of code multiple times
    -- Note indention is very important to escape the loop
    -- Syntax: for item in list_of_items:
 -- Range function with For Loop: Used to generate a range of numbers to loop through
    -- Syntax: for number in range(a, b, <step>):
    -- NOTE: 'b' in NOT included in the range; so if you need 'b' you have to add one to 'b' value
              Range function steps through all the numbers from start to end and increases by 1
              'step' value is optional; To increase the count by a different number; use the 'step' parameter to specify the value to skip by
"""

# For Loop
list_of_items = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]

for item in list_of_items:
    # Do something to each item
    print(item)

# Range function with Loops: Used to generate a range of numbers to loop through/iterate over (absent of an existence of a list)
print("Using range function in For Loop")
for number in range(1, 10):
    print(number)

print("\nUsing 'step' value of 2 in range function in For Loop")
# Range functions using the skip to only print out every other number in the range
for number in range(2, 11, 2):
    print(number)