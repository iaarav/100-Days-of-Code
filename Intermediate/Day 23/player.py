from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)

    def reset(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def onFinished(self, fun):
        if self.ycor() == FINISH_LINE_Y:
            self.reset()
            fun()
