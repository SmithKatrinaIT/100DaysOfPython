"""
Lesson 13: Heads or Tails
Concepts: Random Module - used to create random numbers - (Day 4 concepts)
 -- Modules are a file containing Python definitions and statements.
 -- A module can define functions, classes, and variables.
 -- A module can also include runnable code
 -- random Methods/functions:
    -- randrange(start, stop, step): Returns a randomly selected integer from range
    -- randint(a, b): returns a random integer between a and b (both inclusive)
"""
# modules have to be imported; usually at the top of the script
import random
from typing import List

coin = random.randint(0, 1)

if coin == 1:
    print("Heads")
else:
    print("Tails")

print("\n*****************************************\n")

# using Lists
names_list: list[str] = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
print(f"Original List of names: {names_list}")

names_list.append("Stacy")
print(f"Append the name 'Stacy' to the list: {names_list}")

names_list.extend(["Katrina", "John", "Kia", "Kemahni", "Kajahn"])
print(f"Extend the original List with 5 additional names: {names_list}")


# IndexError:  list index out of range; occurs when you try to call a value at a specific index that doesn't exist

print(f"Number of names in the list: {len(names_list)}")
# print(names_list[11]) # throws IndexError because names_list only goes up to index 10 although there are 11 items in the list


# Off by One Errors: when you store the number of items in a list in a variable, then use that variable incorrectly
num_items = len(names_list)
# print(names_list[num_items]) # also throws Index Error; lists start at index zero (0) not 1


# Nested Lists
#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# separate out original list; then store these 2 list inside 1 list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
veggies = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, veggies]
print(dirty_dozen)

# random.choice() returns a randomly selected element from a specified sequence (string, a range, a list, a tuple, or any other kind of squence
mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))