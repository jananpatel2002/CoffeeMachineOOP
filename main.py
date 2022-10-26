from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def run_program():
    choice = input("What would you like? " + menu.get_items() + " ").lower()
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
        run_program()
    elif choice == 'off':
        return
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
            run_program()
        else:
            run_program()


run_program()
