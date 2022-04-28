#!/usr/bin/env python3
from click import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}
print(logo)

new_bid = True

while new_bid:
    name = str(input('What is your name? '))
    bid = int(input('What is your bid? $'))

    bidders[name] = bid

    more = str(input('Are there other bidders? Enter "yes" or "no" \n'))
    if more == 'no':
        new_bid = False
    else:
        clear()

highest_bid = 0
winner = ""
for bid in bidders:
    bid_amount = bidders[bid]

    if bid_amount > highest_bid:
        highest_bid = bidders[bid]
        winner = bid

print(f'The winner is {winner} with a bid of ${highest_bid}')
