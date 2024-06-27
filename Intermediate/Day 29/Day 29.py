from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random


def passGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passLetters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    passNumbers = [random.choice(numbers) for _ in range(random.randint(2, 6))]
    passSymbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    passList = passLetters + passNumbers + passSymbols

    random.shuffle(passList)
    passworrd = "".join(passList)

    passInput.delete(0, END)
    passInput.insert(0, passworrd)
    pyperclip.copy(passworrd)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def writeData():
    global websiteInput, emailInput, passInput

    emailIn = emailInput.get()
    passwordIn = passInput.get()
    websiteIn = websiteInput.get()

    if not len(passwordIn) == 0 and not len(websiteIn) == 0:
        messagebox.askokcancel(title=websiteIn,
                               message=f"These are the credentials for {websiteIn} \n\n"
                                       f"Email id/ Username: \n\n"
                                       f"{emailIn} \n\n"
                                       f"Password: \n{passwordIn}\n\n"
                                       f"Do you want to save it???")

        with open("passwords.txt", mode="a") as file:
            file.write(f"{websiteIn} | {emailIn} | {passwordIn} \n")

        websiteInput.delete(0, END)
        passInput.delete(0, END)

    else:
        messagebox.showinfo(message="oops, try filling all the fields before adding")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

# Logo
canvas = Canvas(height=200, width=200, bg="white", highlightthickness=False)

logo = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=logo)

canvas.grid(column=3, row=3)

# Labels
website = Label(text="Website: ", bg="white", fg="black")
website.grid(column=2, row=4)

password = Label(text="Password: ", bg="white", fg="black")
password.grid(column=2, row=6)

email = Label(text="Email/Username: ", bg="white", fg="black")
email.grid(column=2, row=5)

# Inputs
websiteInput = Entry(bg="white", width=35, highlightbackground="white", fg="black")
websiteInput.grid(column=3, row=4, columnspan=2)
websiteInput.focus()

emailInput = Entry(bg="white", width=35, highlightbackground="white", fg="black")
emailInput.grid(column=3, row=5, columnspan=2)
emailInput.insert(0, "thecodeteen21@gmail.com")  # Your Email Here

passInput = Entry(bg="white", width=17, highlightbackground="white", fg="black")
passInput.grid(column=3, row=6, columnspan=1)

# Buttons
generatePassword = Button(text="Generate Password", bg="white", fg="black", highlightbackground="white",
                          command=passGenerator)
generatePassword.grid(column=4, row=6, columnspan=1)

add = Button(text="Add", bg="white", fg="black", highlightbackground="white", width=36, command=writeData)
add.grid(column=3, row=7, columnspan=2)

window.mainloop()
