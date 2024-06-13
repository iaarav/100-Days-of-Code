from art import logo
import os


def clear():
    os.system("clear")  # for macOS

print("Welcome to the silent bidding simulator!!")
print(logo)

isRunning = True
dictionaryOfPeople = {}
maxBid = 0

while isRunning:
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))

    dictionaryOfPeople[bid] = name

    wantToRun = input("Are there any other bidders?? Enter \"yes\" or \"no\": ").lower()
    clear()

    if bid>maxBid:
        maxBid = bid

    if wantToRun == "no":
        isRunning = False

print(f"The Highest Bidder is {dictionaryOfPeople[maxBid]} with the highest bid of ${format(maxBid, ",")}")
