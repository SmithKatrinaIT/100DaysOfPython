"""
Project 7: hangman (Day 7 Concepts)
 -- More of -> For and While Loops, Range, Randomisation,
"""


import random
from hangman_words import word_list
from hangman_art import stages, logo

# print the game logo
print(logo)

# use a custom module that contains a list of words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# Create blanks for the letters in the chosen_word
display = []
for _ in range(word_length):
    display += "_"

# starting display
# print(display)
print(f"{" ".join(display)}")

# number of lives
lives = 6

# play while loop
end_of_game = False
while not end_of_game:

    # Prompt user for a letter to guess
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # check (loop) if user guessed the correct letter in the chosen_word at a specific position
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    # Join all the elements in the list and turn it into a String
    print(f"{" ".join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won")

    print(stages[lives])

    # end of while loop

