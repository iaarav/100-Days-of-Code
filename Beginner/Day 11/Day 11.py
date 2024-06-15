import os
import random
from art import logo

isPlaying = True
allCards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
yourCards = []
dealerCards = []


def randomCards(enteredList):
    enteredList.append(random.choice(allCards))


def scoreCalculator(cards):
    totalScore = 0

    for card in cards:
        if card == "A":
            if totalScore <= 10:
                totalScore += 11
            else:
                totalScore += 1
        elif card == "J" or card == "Q" or card == "K":
            totalScore += 10
        else:
            totalScore += int(card)

    return totalScore


def blackjack():
    yourCards = []
    dealerCards = []
    youAreUnder21 = True
    dealerIsUnder21 = True
    flag = True

    os.system("clear")
    print(f"{logo}\n")
    print("Welcome to the game of BlackJack!!")

    randomCards(yourCards)
    randomCards(yourCards)

    randomCards(dealerCards)

    print(f"Your cards are {yourCards} and your score right now is {scoreCalculator(yourCards)}")
    print(f"The Dealer's first card is {dealerCards}")

    while flag:
        wantCard = input("Do you want another card?? Type \"yes\" or \"no\": ")

        if wantCard == "yes":
            randomCards(yourCards)

            newScore = scoreCalculator(yourCards)

            print(f"Your cards are {yourCards} and your score right now is {newScore}")

            if newScore > 21:
                flag = False

        else:
            flag = False
            break

    while scoreCalculator(dealerCards) <= 17:
        randomCards(dealerCards)

    if scoreCalculator(dealerCards) > 21:
        dealerIsUnder21 = False
    if scoreCalculator(yourCards) > 21:
        youAreUnder21 = False

    print(f"The Dealer's Final Cards are {dealerCards}, and the dealer's final score is {scoreCalculator(dealerCards)}")

    if dealerIsUnder21 and youAreUnder21:
        if scoreCalculator(dealerCards) == scoreCalculator(yourCards):
            print("It's a Draw!! Better luck next time!!")
        if scoreCalculator(dealerCards) > scoreCalculator(yourCards):
            print("You lost the game!! Better Luck Next Time.")
        else:
            print("You won the game!! Congratulations.")

    elif not youAreUnder21:
        print("You lost the game!! Better Luck Next Time.")

    elif not dealerIsUnder21:
        print("You won the game!! Congratulations.")


while isPlaying:
    choice = input("Do you want to play a game of blackjack?? type \"yes\" or \"no\": ").lower()

    if choice == "yes":
        isPlaying = True
        blackjack()
    else:
        isPlaying = False
