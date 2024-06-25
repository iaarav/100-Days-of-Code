from tkinter import *

kilometer = 0.0

window = Tk()

window.title("Miles to Kilometer")
window.config(padx=20, pady=20)

milesInput = Entry()
milesInput.grid(column=3, row=3)


def updatekm():
    global kilometer
    miles = float(milesInput.get())
    kilometer = miles * 1.60934
    kilometerOutput.config(text=kilometer)


milesLabel = Label(text="miles")
milesLabel.grid(column=4, row=3)

isEqualLabel = Label(text="is equal to ")
isEqualLabel.grid(column=2, row=4)

kilometerOutput = Label(text=kilometer)
kilometerOutput.grid(column=3, row=4)

kmLabel = Label(text="km")
kmLabel.grid(column=4, row=4)

calculateButton = Button(text="Calculate", command = updatekm)
calculateButton.grid(column=3, row=5)

window.mainloop()
