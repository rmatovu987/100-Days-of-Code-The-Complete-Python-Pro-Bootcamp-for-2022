#!/usr/bin/env python3
"""A program that interprets the BMI based on user's weight and height"""

# capture the user's height and weight
height = float(input('Enter your height in m:'))
weight = float(input('Enter your weight in kg: '))

# calculate the user's bmi
bmi = round(weight / height ** 2)

# interpret the bmi index
if bmi < 18.5:
    print(f'Your bmi is {bmi}. You are underweight')
elif bmi < 25:
    print(f'Your bmi is {bmi}. You have a normal weight')
elif bmi < 30:
    print(f'Your bmi is {bmi}. You are overweight')
elif bmi < 35:
    print(f'Your bmi is {bmi}. You are obese')
else:
    print(f'Your bmi is {bmi}. You are clinically obese')
