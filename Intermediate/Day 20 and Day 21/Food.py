import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")

        self.goto(
            random.randint(-270, 270),
            random.randint(-270, 270)
        )

    def refreshFood(self):
        self.clear()
        self.goto(
            random.randint(-270, 270),
            random.randint(-270, 270)
        )
