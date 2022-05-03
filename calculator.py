#!/usr/bin/env python3


logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


# add
def add(a, b):
    return a + b


# subtract
def subtract(a, b):
    return a - b


# divide
def divide(a, b):
    return a / b


# multiply
def multiply(a, b):
    return a * b


# operation
def operate(a, operator, b):
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if operator not in ('+', '-', '/', '*'):
        print('Invalid operation selected!')
        return

    if operator == '/' and b == 0:
        print('Divisor cannot be zero')
        return

    print(f'{a} {operator} {b} = {operations[operator](a, b)}')


print(logo)
finished = False

while not finished:
    num1 = float(input("What's the first number? "))
    operation = str(input("What operation do you want to perform '+', '-', '*', '/'? "))
    num2 = float(input("What's the second number? "))
    operate(num1, operation, num2)

    fin = str(input('Do you want to continue calculating? Type "yes" or "no"   '))
    if fin == 'no':
        finished = True


