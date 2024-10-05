"""
Project 12: Number Guessing Game (Day 12 Concepts)
 -- Global Scope, Local Scope
"""

from game_art import logo
import random

print(logo)


'''Course Code Improvements -- creates a game() for better flow'''
# use Global variables
EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, attempts):
    """Checks answer against guess and returns the remaining number of attempts the user has left to guess the correct number."""
    if guess > answer:
        print("Too High!")
        return attempts - 1
    elif guess < answer:
        print("Too Low!")
        return attempts -1
    else:
        print(f"You got it! The answer was {answer}")

def number_of_attempts():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


# Start of Game
def game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 101)
    attempts = number_of_attempts()

    # safety check
    print(f"Pssst, the correct answer is {answer}\n")
    guess = 0

    while guess != answer:

        # display the number of attempts the user has to start with or is left with
        print(f"You have {attempts} attempts remaining to guess the number.")

        # Let user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of attempts
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses. You lose")
            return
        elif guess != answer:
            print("Guess Again.")


game()


'''My working code'''
# choose a random number to guess
# random_guess_number = random.randint(1, 101)


# # Returns the number of allowed guesses based on level of difficulty chosen by user
# def number_of_attempts(difficulty):
#
#     if difficulty == 'easy':
#         return 10
#     else:
#         return 5
#
#
# # Start of the Game - starting message and difficulty selection
# print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
# level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#
# # track the number of attempts; if wrong reduce this number by 1
# attempts = number_of_attempts(level_of_difficulty)
#
# guess_correctly = False
#
# # Repeat the guessing functionality if they get it wrong
# while not guess_correctly or attempts == 0:
#     guess = int(input("Make a guess: "))
#
#     if guess == random_guess_number:
#         guess_correctly = True
#         print(f"You got it! The answer was {random_guess_number}")
#
#     elif guess != random_guess_number:
#         guess_correctly = False
#         if guess < random_guess_number:
#             print("Too Low.")
#         else:
#             print("Too High")
#         attempts -= 1
#         print(f"You have {attempts} remaining to guess the number.")
#         print("Guess Again.")





