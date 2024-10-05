from calc_art import logo


# Add function
def add(n1, n2):
    return n1 + n2


# subtract function
def subtract(n1, n2):
    return n1 - n2


# Multipy function
def multiply(n1, n2):
    return n1 * n2


# Divide function
def divide(n1, n2):
    return n1 / n2


# setting the dictionary keys' value to the above calculator functions
operations = {
    "+": add,  # function not a variable
    "-": subtract,
    "*": multiply,
    "/": divide
}

'''
 modified solution 
 -- introduces the concept of recurive funtion: a function that calls itself within the same function
    -- this allows the user to finish the first calculation and start an new one
 -- fixes use of decimal numbers entered by the user                 
'''


def calculator():
    print(logo)
    first_num = float(input("What is the first number?: "))
    finish_calculation = False
    answer = ""

    for symbol in operations:
        print(f" {symbol}")

    while not finish_calculation:
        operation_symbol = input("Pick an operation: ")
        next_num = int(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_num, next_num)
        print(f" {first_num} {operation_symbol} {next_num} = {answer}")
        response = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'e' to exit: ")

        if response == 'e':
            finish_calculation = True
        elif response == 'n':
            finish_calculation = True
            calculation_function()
        else:
            first_num = answer

    # print(f"Final calculation is: {first_num} {operation_symbol} {next_num} = {answer}")
    print(f"Result is: {answer}")


# call the function
calculator()

'''
 original solution
'''
# print(logo)
# first_num = int(input("What is the first number?: "))
# finish_calculation = False
# operation_symbol = ""
# next_num = 0
# answer = ""
#
# # printing out the operations for user to choose from
# for symbol in operations:
#     print(f" {symbol}")
#
# while not finish_calculation:
#     operation_symbol = input("Pick an operation: ")
#     next_num = int(input("What is the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(first_num, next_num)
#     print(f" {first_num} {operation_symbol} {next_num} = {answer}")
#     response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
#
#     if response == 'n':
#         finish_calculation = True
#     else:
#         first_num = answer
#
# #print(f"Final calculation is: {first_num} {operation_symbol} {next_num} = {answer}")
# print(f"Result is: {answer}")

# we create a new function here because the operations dictionary 'value' of a particular 'key' returns a function [add(), subtract(), multiply(), or divide()
#calculation_function = operations[operation_symbol]

# whatever function is returned from retrieving the 'value' from the operations dictionary will replace the 'calculation_function'
#answer = calculation_function(num1, num2)

#print(f" {num1} {operation_symbol} {num2} = {answer}")
