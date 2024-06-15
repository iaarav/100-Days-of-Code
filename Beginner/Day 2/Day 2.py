print("Welcome to the Tip Calculator!!")

billAmount = float(input("What is the total amount of the bill?? \n"))
tipPercent = int(input("What is the percentage of tip you want to give?? \n10,12 or 15?? \n"))
numberOfPeople = int(input("Enter the number of people you want to split it amongst? \n"))

tipAmount = (tipPercent / 100) * billAmount
totalAmount = tipAmount + billAmount
amountPerPerson = str(round((totalAmount / numberOfPeople), 2))

print("Each person should give: $" + amountPerPerson)
