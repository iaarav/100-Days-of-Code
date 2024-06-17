import random
import time
from turtle import Screen, Turtle


def moveRandomSteps(t):
    t.forward(random.randint(0, 10))


userWon = False
raceIsRacing = False

screen = Screen()
screen.setup(500, 500)

userColor = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race?? enter a color: ")

colors = ["red", "orange", "blue", "black", "cyan", "pink"]
xCoordinate = -220
yCoordinate = 160
turtles = []

time.sleep(2)

for i in range(6):
    t = Turtle()
    t.shape("turtle")
    t.penup()

    t.color(colors[i])
    t.goto(x=xCoordinate, y=yCoordinate)
    t.pendown()
    yCoordinate -= 60

    turtles.append(t)

if userColor:
    raceIsRacing = True

while raceIsRacing:

    for turtle in turtles:
        moveRandomSteps(turtle)

        if turtle.xcor() > 230:
            raceIsRacing = False
            index = turtles.index(turtle)

            if turtle.pencolor() == userColor:
                userWon = True


if userWon:
    print("You have won!! Congratulations")
else:
    print("You lost")

screen.exitonclick()