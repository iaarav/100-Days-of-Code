print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!!")
print("Your Mission is to find the treasure!!!")

choice1 = str(input("You're at a crossroads, where do you want to go? Enter \"left\" or \"right\": ")).lower()
if choice1 == "left":
    choice2 = str(input("You find a lake. What do you want to do? Enter \"swim\" or \"wait\": ")).lower()

    if choice2 == "wait":
        choice3 = str(input("The lake disappears!! \nThree new magical doors appear in front of you."
                            "Which one would you choose? \nEnter \"Yellow\", \"Blue\" or \"Red\": ")).lower()

        if choice3 == "yellow":
            print("YOU FOUND THE TREASURE AND WON THE GAME!!!")
        else:
            print("An Anomaly chops you into two pieces with a burning blade!! Game Over.")
    else:
        print("You were eaten by THE TOAD KNIGHT. Game Over.")
else:
    print("You fell prey to carnivorous flies. Game Over.")
