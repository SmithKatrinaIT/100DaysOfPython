"""
Lesson 14: Banker Roulette Randomisation and Data Structure - Lists
 -- Import random module
 -- use square brackets ([]) to create a list
 -- use square brackets after the list variable to get the volue at the specified index
    -- list.append(x) - adds an item at the end of a list
    -- list.extend(iterable) - extend list by appending all the items from the iterable
"""


import random
from typing import List

# using Lists
names_list: list[str] = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# using Random module
num_items = len(names_list)
rand = random.randint(0, num_items - 1)
print(f"{names_list[rand]} is going to buy the meal today!")



