from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 4. Check resources sufficient
# TODO 5. Process coins.
# TODO 6. Check transaction successful
# TODO 7. Make Coffee


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
    money = 0
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
            if c_menu.find_drink(prompt) and c_maker.is_resource_sufficient(prompt):
                purchase_amount = m_machine.process_coins()


coffee_machine()
