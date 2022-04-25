#!/usr/bin/env python3
"""A program to determine whether a given year is a leap year"""

# capture the year entered by the user
year = int(input('Enter the year you want to check: '))

# create boolean to determine if leap year
isLeap = False

# determine if leap year
# is clearly divisible by 4
if year % 4 == 0:
    # except if it can be exactly divided by 100
    if year % 100 == 0:
        # except if it can be exactly divided by 400
        if year % 400 == 0:
            isLeap = True
    else:
        isLeap = True

if isLeap:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
