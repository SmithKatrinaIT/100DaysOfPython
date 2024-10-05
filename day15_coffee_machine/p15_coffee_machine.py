"""
Project 15: Digital Coffee Machine
 -- All Concepts: Using IDE - PyCharm
"""
from coffee_art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# TODO: Print report of all coffee machine resources
resources = {
    "water": 300,
    "milk": 300,
    "coffee": 50
}


# TODO: Check resources are sufficient to make drink order
def check_resources(coffee_ingredients):
    """Returns True if there's enough resources to make the order and False if there are not enough of a resources"""
    for item in coffee_ingredients:
        if coffee_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


# TODO: Process coins
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes: ")) * .10
    total += int(input("How many nickels?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


# TODO: Check transaction
def check_transaction(money_received, drink_cost):
    """Return True when the payment is accepted and False if it is not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Insufficient funds. Money refunded.")
        return False


# TODO: Print Report
def print_report():
    return f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g"


# TODO: Make Coffee
def make_coffee(drink_choice, order_ingredients):
    """Deduct the required ingredients from the resources and make the drink"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_choice} ☕️ Enjoy!")


profit = 0
is_on = True
print(logo)
while is_on:


    # TODO: Prompt user by asking "hat would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Sorry, that was an invalid selection.")
