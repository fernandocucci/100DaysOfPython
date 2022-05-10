# ==========================================
# Day 011 - Project: Black Jack
# ==========================================
import random
import os

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def deal_card(cant, current_cards):
    for _ in range(cant):
        card = random.choice(cards)
        current_cards.append(card)

    return current_cards


def sum_cards(cards):
    sum_value = 0
    for c in cards:
        if (c == 'J') or (c == 'Q') or (c == 'K'):
            sum_value += 10
        elif (c == 'A'):
            sum_value += 11
        else:
            sum_value += int(c)
    if sum_value > 21 and ('A' in cards):
        total_a = cards.count('A')
        sum_value -= 10 * total_a
    return sum_value


keep = "y"

while keep == "y":

    cls()
    user_cards = []
    house_cards = []

    house_cards = deal_card(2, house_cards)
    user_cards = deal_card(2, user_cards)

    print(f"House first card is: {house_cards[0]}")
    user_score = sum_cards(user_cards)
    print(f"Your cards are: {user_cards}, current score: {user_score}")
    while user_score < 21:
        want_another = input("Do you want another card? (y/n): ")
        if want_another == 'y':
            user_cards = deal_card(1, user_cards)
            user_score = sum_cards(user_cards)
            print(f"Your Cards are: {user_cards}, current score: {user_score}")
        else:
            break

    if user_score > 21:
        print("You lost! - Your score is over 21")
    else:
        house_score = sum_cards(house_cards)
        while house_score < 17:
            house_cards = deal_card(1, house_cards)
            house_score = sum_cards(house_cards)

        print(f"House cards were: {house_cards}, final score: {house_score}")
        if house_score <= 21 and house_score >= user_score:
            print("House wins")
        else:
            print("You win")

    keep = input("Do you want to play again? (y/n): ")
