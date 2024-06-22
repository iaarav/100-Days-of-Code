from scoreboard import ScoreBoard
from turtle import Turtle, Screen

snakeParts = []

SEGMENT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
moveDistance = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakeParts = []
        self.createSnake()
        self.head = self.snakeParts[0]

    def createSnake(self):w
        for coordinates in SEGMENT_POSITIONS:
            self.addSnake(coordinates)

    def addSnake(self, coordinates):

        newSegment = Turtle("square")
        newSegment.penup()
        newSegment.color("white")
        newSegment.goto(coordinates)
        self.snakeParts.append(newSegment)

    def extend(self):
        self.addSnake(self.snakeParts[-1].position())

    def reset(self):
        for snake in self.snakeParts:
            snake.goto(20000, 20000)

        self.snakeParts.clear()
        self.createSnake()
        self.head = self.snakeParts[0]

    def move(self):

        for i in range(len(self.snakeParts) - 1, 0, -1):
            position = (self.snakeParts[i - 1].xcor(), self.snakeParts[i - 1].ycor())
            self.snakeParts[i].goto(position)

        self.head.forward(moveDistance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
