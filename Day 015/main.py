# ==========================================
# Day 015 - Project: Coffee Machine
# ==========================================

from menu import MENU
from menu import resources


def print_resources():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")


def check_resources(drink, available_res):
    for i in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][i] > available_res[i]:
            return [False, i]
    return [True, ""]


def get_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def update_resources(drink, available_res):
    for i in MENU[drink]["ingredients"]:
        available_res[i] -= MENU[drink]["ingredients"][i]
    available_res["money"] += MENU[drink]["cost"]


choice = ""
resources["money"] = float(0)
has_res = True
coins = 0
while choice != "off":
    print("What would you like?")
    choice = input("Espresso / Latte / Cappuccino: ").lower()
    if choice == "report":
        print_resources()
    elif choice == "off":
        break
    else:
        has_res, message = check_resources(choice, resources)
        if has_res:
            coins = get_coins()
            current_cost = MENU[choice]["cost"]
            if coins >= current_cost:
                if coins > current_cost:
                    your_change = coins - current_cost
                    print(f"Please take your change ${round(your_change, 2)}")
                update_resources(choice, resources)
                print("Enjoy your drink!")
            else:
                print("Sorry, you don't have enough money. Returning money ...")
        else:
            print(f"Sorry there is no enough {message}")

