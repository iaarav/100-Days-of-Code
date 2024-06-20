import time
from ssnake import Snake
from turtle import Screen
from Food import Food
from scoreboard import ScoreBoard

screen = Screen()

isPlaying = True

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME!!")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while isPlaying:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refreshFood()
        score.score += 1
        score.writeScore()
        snake.extend()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        isPlaying = False
        score.writeMessage("GAME OVER")

    for segment in snake.snakeParts[1::1]:
        if snake.head.distance(segment) < 10:
            isPlaying = False
            score.writeMessage("GAME OVER")

screen.exitonclick()
