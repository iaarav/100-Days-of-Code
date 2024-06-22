from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.score = 0
        self.highscore = 0

        with open("scores.txt") as scores:
            self.highscore = int(scores.read())

        self.color("white")
        self.penup()
        self.goto(-280, 270)

        self.writeScore()

    def writeScore(self):
        self.clear()
        self.setx(0)
        self.write(f"SCORE: {self.score} High Score: {self.highscore}", align="center",
                   font=("Times New Roman", 24, "normal"))

    def writeMessage(self, message):
        self.clear()
        self.write(message, align="center", font=("Times New Roman", 24, "normal"))

    def increaseScore(self):
        self.score += 1
        self.writeScore()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        with open("scores.txt", mode= "w") as file:
            file.write(f"{self.highscore}")

        self.score = 0
        self.writeScore()
