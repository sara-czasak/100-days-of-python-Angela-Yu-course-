from coffee_data import *
import time


def get_order_data(choice):
    if choice == 'e':
        coffee_name = 'espresso'
        coffee_ingredients = data['espresso']['ingredients']
        coffee_price = data['espresso']['cost']
        return coffee_name, coffee_ingredients, coffee_price
    elif choice == 'l':
        coffee_name = 'latte'
        coffee_ingredients = data['latte']['ingredients']
        coffee_price = data['latte']['cost']
        return coffee_name, coffee_ingredients, coffee_price
    elif choice == 'c':
        coffee_name = 'cappuccino'
        coffee_ingredients = data['cappuccino']['ingredients']
        coffee_price = data['cappuccino']['cost']
        return coffee_name, coffee_ingredients, coffee_price


def check_resources(coffee_ingredients, coffee_name):

    user_feedback = []
    resource_feedback = []

    water_needed = coffee_ingredients['water']
    milk_needed = coffee_ingredients['milk']
    coffee_needed = coffee_ingredients['coffee']

    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']

    if water_needed < water_left:
        user_feedback.append("* WATER CHECK PASS")
        resource_feedback.append(True)
    else:
        user_feedback.append("* NOT ENOUGH WATER")
        resource_feedback.append(False)
    if milk_needed < milk_left:
        user_feedback.append("* MILK CHECK PASS")
        resource_feedback.append(True)
    else:
        user_feedback.append("* NOT ENOUGH MILK")
        resource_feedback.append(False)
    if coffee_needed < coffee_left:
        user_feedback.append("* COFFEE CHECK PASS")
        resource_feedback.append(True)
    else:
        user_feedback.append("* NOT ENOUGH COFFEE")
        resource_feedback.append(False)


    if False not in resource_feedback and take_payment(coffee_name):
        update_resources(coffee_ingredients)
    return user_feedback


def update_resources(coffee_ingredients):
    resources['water'] -= coffee_ingredients['water']
    resources['milk'] -= coffee_ingredients['milk']
    resources['coffee'] -= coffee_ingredients['coffee']


def take_payment(coffee_name):
    cost = data[coffee_name]['cost']
    print(f"*** {coffee_name.upper()} PRICE: ${cost} ***")
    print('-' * 30)
    print("*** PLEASE INCERT COINS ***")
    pennies = int(input("PENNIES: ")) * 0.01
    nickels = int(input("NICKELS: ")) * 0.05
    dimes = int(input("DIMES: ")) * 0.10
    quarters = int(input("QUARTERS: ")) * 0.25
    total_coins_incerted = pennies + nickels + dimes + quarters
    print('-' * 30)
    print(f"*** YOU ENTERED ${total_coins_incerted:.2f} ***")

    if total_coins_incerted < cost:
        print('-' * 30)
        print("*** NOT ENOUGH COINS ADDED! ***"
              f"*** YOU ARE ${cost - total_coins_incerted:.2f} SHORT ***")
        print('-' * 30)
        return False
    elif total_coins_incerted >= cost:
        print('-' * 30)
        print("Calculating change...")
        time.sleep(2)
        change = total_coins_incerted - cost
        print(f"*** YOUR CHANGE IS: ${change:.2f} ***")
        print("Dispensing coffee...")
        time.sleep(2)
        print(f"*** HERE IS YOUR {coffee_name.upper()}! ***\n"
              "*** ENJOY THE REST OF YOUR DAY! ***")
        resources['money'] += cost
        return True


def print_report(resources):
    print("-" * 30)
    print("*** REPORT ***")
    print(f"* Water: {resources['water']}")
    print(f"* Milk: {resources['milk']}")
    print(f"* Coffee: {resources['coffee']}")
    print(f"* Money: {resources['money']}")
    print("-" * 30)