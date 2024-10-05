"""
Project 14: Higher or Lower Game - Who has the most followers
 --  All concepts
"""

from game_art import logo, vs
from game_data import data
import os
import random


def format_data(list_item):
    """Format the dictionary data into printable format"""
    name = list_item["name"]
    description = list_item["description"]
    country = list_item["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(choice, count_a, count_b):
    """Takes the user's choice/guess and the follower counts and returns True or False if the user choose correctly  or not."""
    if count_a > count_b:
        return choice == 'A'
    else:
        return choice == 'B'


def game():
    # get random dictionary entries from data list
    compare_b = random.choice(data)

    # keep track of user's score; to increase if guess is correct; ends the game when guess is incorrect
    score = 0

    # print the logo art above Dictionary A element
    print(logo)

    # while loop control
    incorrect_guess = False

    while not incorrect_guess:

        compare_a = compare_b
        compare_b = random.choice(data)
        if compare_a == compare_b:
            compare_b = random.choice(data)

        # Print first comparison - comparisonA
        print(f"Compare A: {format_data(compare_a)}.")

        # print the vs art  above Dictionary B element
        print(vs)

        # Print second comparison - comparisonB
        print(f"Against B: {format_data(compare_b)}.")

        # Ask user to select which option presented has the most follower using A or B
        guess = input(f"Who has more followers? Type 'A' or 'B': ").upper()

        # clear the screen and print the logo again
        os.system("clear")
        print(logo)

        # check if option A dictionary[follower_count] is higher or lower than option B
        answer = check_answer(guess, compare_a['follower_count'], compare_b['follower_count'])
        if answer:
            score += 1
            print(f"You are correct! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            incorrect_guess = True


game()

