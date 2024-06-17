from turtle import Turtle, Screen

t = Turtle()


def moveForward():
    t.forward(10)


def moveBackward():
    t.forward(-10)


def moveClockwise():
    t.right(5)
    t.forward(10)


def moveAnticlockwise():
    t.left(5)
    t.forward(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen = Screen()
screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "s")
screen.onkey(moveClockwise, "d")
screen.onkey(moveAnticlockwise, "a")
screen.onkey(clear, "c")

screen.exitonclick()
