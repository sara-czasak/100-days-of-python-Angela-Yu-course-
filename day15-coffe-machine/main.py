from functions import *
import time
from coffee_data import *

print("*** WELCOME TO THE COFFEE MACHINE ***")
print('-' * 30)
on = True

while on:

    choice = input("What would you like to order?\nE - espresso\nL - latte\nC - cappuccino\n").lower()
    print('-' * 30)
    valid = False
    while not valid:
        if choice == 'e':
            print('Wait one moment while I check resources...')
            time.sleep(2)
            valid = True
        elif choice == 'l':
            print('Wait one moment while I check resources...')
            time.sleep(2)
            valid = True
        elif choice == 'c':
            print('Wait one moment while I check resources...')
            time.sleep(2)
            valid = True
        elif choice == 'm':
            print('Wait one moment while I check resources...')
            time.sleep(2)
            valid = True
        elif choice == 'off':
            print('Turning off...')
            time.sleep(2)
            print('*** BYE ***')
            valid = True
        else:
            print("*** CHOICE NOT RECOGNIZED ***")
            choice = input("What would you like to order?\nE - espresso\nL - latte\nC - cappuccino\n").lower()
    if choice == 'm':
        print("*** MAINTENANCE MODE ENGAGED ***")
        print_report(resources)
    elif choice == 'off':
        break
    else:
        coffee_name, coffee_ingredients, coffe_price = get_order_data(choice)
        feedback = check_resources(coffee_ingredients, coffee_name)
        # for i in feedback:
        #     print(i)
        print('-' * 30)
