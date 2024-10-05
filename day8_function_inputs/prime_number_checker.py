"""
Lesson 21: Prime Number Checker - determines if a number argument is prime or not - (Day 8 Concepts)
 -- Concept: Functions with Inputs
"""


# Write your code below this line 👇
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
