import os
import random
from art import logo

number = random.randint(1, 100)
guessedTheNumber = False


def setDifficulty():
    difficulty = input("Choose a difficulty: Easy or Hard: ").lower()
    if difficulty == "easy":
        calculate(10)
    elif difficulty == "hard":
        calculate(5)
    else:
        print("Invalid Input")


def calculate(attempts):
    global guessedTheNumber
    for n in range(attempts):
        print(f"You have {attempts - n} attempts remaining.")
        guess = int(input("Make a guess: "))

        if number == guess:
            guessedTheNumber = True
            break

        elif guess > number:
            print("Too High, try again")
            print()

        elif guess < number:
            print("Too Low, try again")
            print()

    if guessedTheNumber:
        print("You guessed the number!! Congratulations")
    else:
        print("You Lost")


os.system("clear")
print(logo)
print()
print("Welcome to the Number Choosing Game!!")
setDifficulty()
