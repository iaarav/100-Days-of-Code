import random

from flask import Flask

app = Flask(__name__)
randomnumber = random.randint(0, 9)


def makeBold(function):
    def wrapperFunction():
        return f"<h1>{function()}</h1>"

    return wrapperFunction


@app.route('/')
@makeBold
def homePage():
    return ("Guess a number between 0 to 9"
            "<br><br><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>")


@app.route('/<int:number>')
def guessingNumber(number):
    if randomnumber > number:
        return "<h1>Too Low, try again!</h1>" \
               "<br><br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    elif randomnumber < number:
        return "<h1>Too High, try again!</h1>" \
               "<br><br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif randomnumber == number:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<br><br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
