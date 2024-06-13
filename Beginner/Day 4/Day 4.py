import random
import sys
import dataModule as dM

ch = [dM.rock, dM.paper, dM.scissors]
computerChoice = random.randint(0, 2)
playerWin = False

print("What do you choose?")
playerChoice = int(input("Enter 0 for rock, 1 for paper, 2 for scissor:  "))

if playerChoice < 3 or playerChoice < 0:
    print(ch[playerChoice])
    print("The computer chose: ")
    print(ch[computerChoice])

    if playerChoice == computerChoice:
        print("It's a Draw!!")
        sys.exit(0)
    elif playerChoice == 0 and computerChoice == 2:
        playerWin = True
    elif playerChoice < computerChoice:
        playerWin = False
    if computerChoice == 0 and playerChoice == 2:
        playerWin = False
    elif playerChoice > computerChoice:
        playerWin = True

    if playerWin:
        print("You won!!")
    else:
        print("You Lost!!")

else:
    print("Invalid Input.")
