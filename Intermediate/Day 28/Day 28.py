import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    global timer, reps, marks
    window.after_cancel(timer)
    canvas.itemconfig(timerText,text = "00:00")
    timerLabel.config(text="Timer")
    checkMarks.config(text="")
    reps = 0
    marks = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #

def startTimer():
    global reps, marks
    reps += 1

    if reps in [1, 3, 5, 7]:
        checkMarks.config(text=marks)
        timerLabel.config(text="WORK", fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps in [2, 4, 6]:
        marks += "✅"
        checkMarks.config(text=marks)
        timerLabel.config(text="SHORT BREAK", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        marks += "✅"
        checkMarks.config(text=marks)
        timerLabel.config(text="LONG BREAK", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        reps = 0
        marks = ""


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timerText, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        startTimer()

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timerLabel = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timerLabel.grid(column=2, row=0)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomatoImage = PhotoImage(file="tomato.png")
canvas.create_image(103, 110, image=tomatoImage)
timerText = canvas.create_text(106, 132, text="00:00", font=(FONT_NAME, 36, "bold"))
canvas.grid(column=2, row=2)

startButton = Button(text="Start", highlightbackground=YELLOW, command=startTimer)
startButton.grid(column=1, row=4)

resetButton = Button(text="Reset", highlightbackground=YELLOW, command=resetTimer)
resetButton.grid(column=4, row=4)

checkMarks = Label(text="", bg=YELLOW, font=(FONT_NAME, 30))
checkMarks.grid(column=2, row=5)
window.mainloop()
