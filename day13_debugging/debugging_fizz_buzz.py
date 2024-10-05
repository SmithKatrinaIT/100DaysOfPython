"""
Lesson 27 - Debugging FizzBuzz - (Day 13 concepts)
 -- Debugging
"""

target = int(input("Enter in a number: "))
for number in range(1, target + 1):
  #if number % 3 == 0 or number % 5 == 0: # error; conditional should be 'and' not 'or'
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  #if number % 3 == 0: #error should be elif statements not if statements
  elif number % 3 == 0:
    print("Fizz")
  #if number % 5 == 0: #error should be elif statements not if statements
  elif number % 5 == 0:
    print("Buzz")
  else:
    #print([number]) # error when using 'if' instead of 'elif' - it prints the number as well as the 'fizzBuzz' statements; also printing index and not the actual number
    print(number)