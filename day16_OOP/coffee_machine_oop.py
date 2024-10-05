"""
Concept: Classes and Packages: OOP
 -- using predefined and pre-constructed classes recreate the coffee_machine project with OOP principles

"""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(choice):
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

