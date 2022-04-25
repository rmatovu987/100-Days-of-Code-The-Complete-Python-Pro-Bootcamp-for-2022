#!/usr/bin/env python3
"""Create a love calculator"""

print('Welcome to the love calculator')

# capture the lovers' names
name1 = input('What is your name? ').lower()
name2 = input('What is their name? ').lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')
l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')

true = t + r + u + e
love = l + o + v + e

total = int(str(true) + str(love))

if total < 10 or total > 90:
    print(f'Your score is {total}. You go together like coke and mentos')
elif 40 < total < 50:
    print(f'Your score is {total}. You are alright together.')
else:
    print(f'Your score is {total}')
