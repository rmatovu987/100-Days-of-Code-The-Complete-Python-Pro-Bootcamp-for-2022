#!/usr/bin/env python3
"""An automatic order pizza program to calculate the bill"""


# capture customer order
print('Welcome to Python Pizza Deliveries!🤠')
size = input('Which size of pizza do you want? S, M, or L: ')
add_pepperoni = input('Do you want pepperoni? Y or N: ')
extra_cheese = input('Do you want extra cheese? Y or N: ')

# determine the cost
total_bill = 0

if size == 'S':
    total_bill += 15
elif size == 'M':
    total_bill += 20
elif size == 'L':
    total_bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        total_bill += 2
    elif size == 'L' or size == 'M':
        total_bill += 3

if extra_cheese == 'Y':
    total_bill += 1

print(f'Your total bill is ${total_bill}')
