from coffee_machine import *
from coffee_data import *

coffee_machine = CoffeeMachine(resources, data)

on = True
while on:
    coffee_machine.show_menu()
    print("-" * 15, "\n")
    choice = coffee_machine.take_order()

    if choice != 'off' and choice != 'maintenance':
        can_make = coffee_machine.check_resources(choice)
        if can_make:
            coffee_machine.take_payment(choice)
    elif choice == 'off':
        break
