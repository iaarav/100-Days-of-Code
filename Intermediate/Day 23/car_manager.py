import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.carMoveDistance = STARTING_MOVE_DISTANCE
        self.cars = []

    def createCars(self):
        if random.randint(1, 5) == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-280, 280))

            self.cars.append(car)

    def moveCars(self):
        for car in self.cars:
            car.forward(-self.carMoveDistance)

    def levelUp(self):
        self.carMoveDistance += MOVE_INCREMENT
