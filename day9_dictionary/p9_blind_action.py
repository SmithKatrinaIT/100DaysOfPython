"""
Project 9: Blind Action - (Day 9 Concepts)
 -- Nested Lists, Dictionaries
"""

from auction_art import logo
import os
import time

print(logo)

# declare empty dictionary
bids = {}

# while loop control
bidding_finished = False

# function to add additional bidders
def bidder(new_name, new_bid):
    bids[new_name] = new_bid


# function to loop through the dictionary to find the winner of the auction (highest bid)
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bid in bidding_record:
        bid_amount = bidding_record[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} with a bid of {highest_bid}. Congratulations!!!")


# control loop - continue auction if more people want to bid
while not bidding_finished:
    valid_option = False
    name = input("What is your name: ")
    bid_price = int(input("What is your bid: $"))
    bids[name] = bid_price
    #other_bidders = int(input("Are there other people who want to bid? \nEnter 1 for 'Yes' or 2 for 'No': "))

    while not valid_option:
        other_bidders = input("Are there other people who want to bid? \nEnter 1 for 'Yes' or 2 for 'No': ")

        if other_bidders != "1" and other_bidders != "2":
            print(f"You've entered an invalid option. Please try again\n")
            valid_option = False

        if other_bidders == "1":
            valid_option = True
            os.system('clear')
            print(logo)

        if other_bidders == "2":
            valid_option = True
            bidding_finished = True
            highest_bidder(bids)




