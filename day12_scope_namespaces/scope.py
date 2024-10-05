"""
Concept: Scope - accessibility of a variable or function
 -- Local scope: access within a function only
 -- Global scope: access to a variable or function anywhere in the script/program (any part of the program/script) can use it
 -- Namespace: anything you name has a namespace; and it's valid in certain scope
 -- NOTE: no such thing as Block scope; like other programming languages (if, while, for loops)
 -- Global keyword: use when you want to use (modify) a Globally scoped variable inside a function
    -- Bad practice to modify global variable in a function; prone to bugs
    -- Instead utilize 'return' statements to modify a global variable
    -- Exception to the Rule: Global Constants; a variable who's value you never what to change/modify
    -- Syntax for Global Constants - variable name should be in all uppercase letters
"""

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)  # cannot access 'potion_strength' outside the function because it was not declared outside the function

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)  # able to use 'player_health' within the function because it was declared outside (or globally) the function

# Namespace -


# Block scope - not a concept in Python
game_level = 3
enemies = ["Skeletion", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]


# this is valid Python code to access 'new_enemy' outside the 'IF BLOCK' of code
print(new_enemy)


# Scope Issue - should never name you Local scoped variables the same name as your Global scoped variables

enemies = 1  # Global scope variable

def increase_enemies1():
  enemies = 2  # Local scope variable; it is not the same as the above variable with the same name
  print(f"enemies inside function: {enemies}")  # prints out 2

increase_enemies1()
print(f"enemies outside function: {enemies}")  # prints out 1

# use the 'global' key word to explicitly let the function modify the globe scoped variable
def increase_enemies2():
  global enemies # modifying global variable within the function
  enemies += 1
  print(f"enemies inside function: {enemies}")  # prints out 2

increase_enemies2()
print(f"enemies outside function: {enemies}")  # prints out 2


# use the 'return' statement modify the globe scoped variable instead of using the 'global' keyword
def increase_enemies3():
  print(f"enemies inside function: {enemies}")  # prints out 2
  return enemies + 1 # return the global variable and increase it by 1

enemies = increase_enemies3()
print(f"enemies outside function: {enemies}")  # prints out 2
