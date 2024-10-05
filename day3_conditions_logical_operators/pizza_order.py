
"""
Exercise: Control Flow with if/else and Conditional Operators
 -- if/else statement
"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input('What size pizza do you want? "S", "M", or "L"')
add_pepperoni = input('Do you want pepperoni? "Y" or "N"')
extra_cheese = input('Do you want extra cheese? "Y" or "N"')

# Your code below this line 👇
cost = 0

if extra_cheese.lower() == 'y':
    cost += 1

if add_pepperoni.lower() == 'y':
    if size.lower() == 'l' or size.lower() == 'm':
        cost += 3
    else:
        cost +=2
if size.lower() == 's':
    cost += 15
elif size.lower() == 'm':
    cost += 20
else:
    cost += 25

print(f"Your final bill is: ${cost}.")
