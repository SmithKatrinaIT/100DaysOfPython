"""
Lesson 19: FizzBuzz Game (Day 5 concepts)
 -- Loops, Range, and Code Blocks
 -- For Loop with Range function and 'step' argument
"""

# Write your code here 👇
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)