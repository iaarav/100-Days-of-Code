import os
from game_data import *
from art import *
import random


def clear():
    os.system("clear")


playerIsWinning = True
score = 0


def HigherLower():
    global playerIsWinning
    while playerIsWinning:
        clear()
        print(logo)
        print(f"Your current score: {score}")
        choice1 = random.choice(data)
        choice2 = random.choice(data)

        if choice1 == choice2:
            choice2 = random.choice(data)

        print(f"COMPARE A: {choice1["name"]}, a {choice1["description"]} from {choice1["country"]}")
        print()
        print(vs)
        print()
        print(f"COMPARE B: {choice2["name"]}, a {choice2["description"]} from {choice2["country"]}")

        choiceOfPlayer = input("Who has more followers? Type \'A\' or \'B\'").lower()

        a = int(choice1["follower_count"])
        b = int(choice2["follower_count"])

        calculateResults(a, b, choiceOfPlayer)


def calculateResults(a, b, choiceOfPlayer):
    global score, playerIsWinning
    if a > b and choiceOfPlayer == "a":
        score += 1
        playerIsWinning = True
        print(f"You're right!! Your current score is {score}")
    elif b > a and choiceOfPlayer == "b":
        score += 1
        playerIsWinning = True
        print(f"You're right!! Your current score is {score}")
    else:
        playerIsWinning = False
        print(f"You're wrong!! Your current score is {score}")


HigherLower()
