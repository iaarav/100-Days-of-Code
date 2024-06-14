from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

isRunning = True

while isRunning:
    choice = input(f"What do you want to order?? {Menu.get_items()}")

    if choice == "off":
        isRunning = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = Menu.find_drink(order_name=choice)

        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
            moneyMachine.make_payment(drink)
