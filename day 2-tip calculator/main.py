print("*** WELCOME TO THE TIP CALCULATOR! ***")

def calculate_bill(total, tip, people):
    total_with_tip = total + ((tip * total) / 100)
    split_bill = total_with_tip / people
    return split_bill

bill_total = float(input("What is your total bill?\n$"))

tip_percent = int(input("What percentage tip would you like to leave?\n15 / 20 / 22\n"))

people = int(input("How many people are splitting the bill?\n"))

result = calculate_bill(bill_total, tip_percent, people)
print(f"Each of you needs to pay ${result:.2f}$")