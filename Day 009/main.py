#==========================================
# Day 009 - Project: Secret Auction
#==========================================

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


selection = ""
offers = {}

while selection != "no":
    cls()
    name = input("Type your Name: ")
    offer = int(input("Type your Offer: $"))
    offers[name] = offer
    selection = input("Is there another person? (yes/no): ")

cls()
max_name = ""
max_offer = 0
for offer in offers:
    if offers[offer] > max_offer:
        max_offer = offers[offer]
        max_name = offer
print(f"The winner is {max_name} with a bid of ${max_offer}")