import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

playerTurtle = Player()
carManager = CarManager()
scoreBoard = ScoreBoard()

screen.listen()

screen.onkey(playerTurtle.move, "Up")

game_is_on = True
while game_is_on:
    scoreBoard.writeScore()
    carManager.createCars()
    carManager.moveCars()
    time.sleep(0.1)
    screen.update()

    for car in carManager.cars:
        if playerTurtle.distance(car) < 20:
            game_is_on = False
            scoreBoard.writeMessage("GAME OVER")

    playerTurtle.onFinished(scoreBoard.increaseScore)


screen.exitonclick()