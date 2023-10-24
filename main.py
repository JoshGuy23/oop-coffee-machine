from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def command(choice):
    if choice == "off":
        return -1
    elif choice == "report":
        return 0
    else:
        return 1


def report(maker, machine):
    maker.report()
    machine.report()


def coffee_machine():
    running = True
    c_menu = Menu()
    c_maker = CoffeeMaker()
    m_machine = MoneyMachine()
    while running:
        prompt = input(f"What would you like? ({c_menu.get_items()}): ").lower()
        status = command(prompt)
        if status == -1:
            return
        elif status == 0:
            report(c_maker, m_machine)
        else:
            coffee = c_menu.find_drink(prompt)
            if coffee is not None:
                if c_maker.is_resource_sufficient(coffee) and m_machine.make_payment(coffee.cost):
                    c_maker.make_coffee(coffee)


coffee_machine()
