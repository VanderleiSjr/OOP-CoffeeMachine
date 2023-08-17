from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
obj_coffee_maker = CoffeeMaker()
obj_money_machine = MoneyMachine()
while True:
    options = drink_menu.get_items()
    choice = input(f"What would you like? {options}\n")
    match choice:
        case "espresso" | "latte" | "cappuccino":
            drink = drink_menu.find_drink(choice)
            if obj_coffee_maker.is_resource_sufficient(drink) and obj_money_machine.make_payment(drink.cost):
                obj_coffee_maker.make_coffee(drink)
        case "off":
            print("Shutting down the machine")
            break
        case "report":
            obj_coffee_maker.report()
            obj_money_machine.report()
        case _:
            print("Wrong option or typing error")
