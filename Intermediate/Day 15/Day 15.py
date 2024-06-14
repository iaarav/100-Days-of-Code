import os
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

sufficientResourcesAvailable = True


def clear():
    os.system("clear")


def coffeeCheckerAndMaker(coffee):
    global sufficientResourcesAvailable
    global resources
    missingResources = []
    missingResources.clear()

    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        missingResources.append("water")

    if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
        missingResources.append("milk")

    if resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        missingResources.append("coffee")

    if not missingResources:
        sufficientResourcesAvailable = True
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    else:
        sufficientResourcesAvailable = False
        print(f"Sorry, sufficient {", ".join(missingResources)} not present.")


def processingCoins(coffee):
    global sufficientResourcesAvailable, resources

    if sufficientResourcesAvailable:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        cost = MENU[coffee]["cost"]
        moneyEntered = quarters * 0.01 + dimes * 0.05 + nickels * 0.1 + pennies * 0.25
        moneyReturned = 0

        if moneyEntered >= cost:

            print("Your Transaction has been successful")

            resources["money"] += MENU[coffee]["cost"]

            if moneyEntered > cost:
                moneyReturned = round(float(moneyEntered - cost), 2)

                print(f"Here is {moneyReturned} in change.")

            print("Here's your coffee ☕️ Enjoy!!")

        else:
            print("Sorry that's not enough money. Money Refunded.")


def showReport():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources["milk"]} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: {resources["money"]} usd")


def coffeeMaker():
    machineIsRunning = True

    while machineIsRunning:
        clear()

        choice = str(input("What would you like? (espresso, latte, cappuccino)\n")).lower()

        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            coffeeCheckerAndMaker(choice)
            processingCoins(choice)
        elif choice == "report":
            showReport()
        elif choice == "off":
            machineIsRunning = False
        else:
            print("Invalid Input. Try again.")

        time.sleep(5)


coffeeMaker()
