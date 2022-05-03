#!/usr/bin/env python3
import random
from typing import List

from click import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def calculate_score(cards: List) -> int:
    """Takes a list of cards and returns the sum"""

    if len(cards) == 2 and 10 in cards and 11 in cards:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def deal_cards() -> int:
    """Returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(user, computer):
    """Compares the user score and computer score"""
    if user == computer:
        return "Draw 🤕"
    elif computer == 0:
        return "Lose, opponent has Blackjack 🥴"
    elif user == 0:
        return "Win with a Blackjack 🤩"
    elif user > 21:
        return "You went over. You lose 🤨"
    elif computer > 21:
        return "Opponent went over. You win 🥳"
    elif user > computer:
        return "You win 🥳"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    # instantiate the cards lists
    user_cards = []
    computer_cards = []
    isGameOver = False

    # Deal the user and computer 2 cards
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    # user continues taking cards
    while not isGameOver:
        # calculate the scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            isGameOver = True
        # Ask user if they want to draw another card
        else:
            draw = str(input('Do you want to draw another card? Type "yes" or "no" '))
            if draw == 'no':
                isGameOver = True
            else:
                user_cards.append(deal_cards())

    # Computer takes cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))

    while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
        clear()
        play_game()


play_game()
