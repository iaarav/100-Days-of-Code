from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-280, 270)

        self.writeScore()

    def writeScore(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=("Times New Roman", 24, "normal"))

    def writeMessage(self, message):
        self.clear()
        self.home()
        self.write(message, align="center", font=("Times New Roman", 48, "normal"))

    def increaseScore(self):
        self.level += 1
        self.writeScore()
