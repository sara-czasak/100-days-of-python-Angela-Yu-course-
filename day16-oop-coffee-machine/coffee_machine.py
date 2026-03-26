


class CoffeeMachine:
    def __init__(self, resources, menu):
        self.resources = resources
        self.menu = menu
        print(self.menu)
        print(self.resources)


    def show_menu(self):
        print("*** MENU ***")
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


    def update_resources(self):
        pass


    def take_payment(self):
        pass


    def print_report(self):
        pass


    def get_order_data(self):
        pass