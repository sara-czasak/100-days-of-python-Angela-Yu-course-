


class CoffeeMachine:
    def __init__(self, resources, menu):
        self.resources = resources
        self.menu = menu


    def show_menu(self):
        print("\n*** MENU ***")
        for i in self.menu:
            print(f"{i[0].capitalize()} - {i.capitalize()}")


    def take_order(self):
        choice = input("Choose an option: ").lower()
        if not choice.startswith(('off', 'm', 'e', 'c', 'l')):
            print("Invalid choice. Please try again.")
            choice = input("Choose an option: ").lower()
        if choice == 'off':
            choice = 'off'
        elif choice.startswith('m'):
            choice = 'maintenance'
            self.print_report()
        elif choice.startswith('e'):
            choice = 'espresso'
        elif choice.startswith('c'):
            choice = 'cappuccino'
        elif choice.startswith('l'):
            choice = 'latte'
        return choice


    def check_resources(self, choice):
        feedback = []
        missing = []
        water_needed = self.menu[choice]['ingredients']['water']
        milk_needed = self.menu[choice]['ingredients']['milk']
        coffee_needed = self.menu[choice]['ingredients']['coffee']
        if water_needed <= self.resources['water']:
            feedback.append(True)
        else:
            feedback.append(False)
            missing.append('water')
        if milk_needed <= self.resources['milk']:
            feedback.append(True)
        else:
            feedback.append(False)
            missing.append('milk')
        if coffee_needed <= self.resources['coffee']:
            feedback.append(True)
        else:
            feedback.append(False)
            missing.append('coffee')
        if False in feedback:
            for i in missing:
                print(f"Machine is out of {i}..")
            return False
        else:
            return True


    def update_resources(self, choice):
        self.resources['water'] -= self.menu[choice]['ingredients']['water']
        self.resources['milk'] -= self.menu[choice]['ingredients']['milk']
        self.resources['coffee'] -= self.menu[choice]['ingredients']['coffee']
        self.resources['money'] += self.menu[choice]['cost']


    def take_payment(self, choice):
        price = self.menu[choice]['cost']
        print(f"Please pay ${price:.2f} for {choice}.")

        pennies = int(input("Pennies: ")) * 0.01
        nickels = int(input("Nickels: ")) * 0.05
        dimes = int(input("Dimes: ")) * 0.10
        quarters = int(input("Quarters: ")) * 0.25
        paid = pennies + nickels + dimes + quarters

        if paid >= price:
            print(f"Processing payment of ${paid:.2f}.")
            print(f"Here is your change: {paid-price:.2f}.")
            self.update_resources(choice)
        else:
            print(f"I'm sorry, {paid:.2f} is not enough.")


    def print_report(self):
        print("\n*** MAINTENANCE MODE ON ***")
        print('-' * 15)
        for i in self.resources:
            print(f"{i}: {self.resources[i]}")
        print('-' * 15, "\n")
