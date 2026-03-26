from coffee_machine import *
from coffee_data import *

coffee_machine = CoffeeMachine(resources, data)

on = True
while on:
    coffee_machine.show_menu()
    choice = coffee_machine.take_order()
    print(choice)
    coffee_machine.check_resources(choice)
    break