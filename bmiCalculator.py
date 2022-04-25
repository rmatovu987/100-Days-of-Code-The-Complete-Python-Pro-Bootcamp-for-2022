#!/usr/bin/env python3
"""A program that interprets the BMI based on user's weight and height"""

# capture the user's height and weight
height = float(input('Enter your height in m:'))
weight = float(input('Enter your weight in kg: '))

# calculate the user's bmi
bmi = weight / (height * height)

# interpret the bmi index
if bmi < 18.5:
    print('You are underweight')
elif bmi < 25:
    print('You have a normal weight')
elif bmi < 30:
    print('You are overweight')
elif bmi < 35:
    print('You are obese')
else:
    print('You are clinically obese')
