def calculator(a, operator, b):
    if a == "" or b == "" or operator == "":
        return "I'm sorry, I didn't catch that.."
    match operator:
        case "+":
            return f"{float(a)} + {float(b)} = {float(a) + float(b)}"
        case "-":
            return f"{float(a)} - {float(b)} = {float(a) - float(b)}"
        case "*":
            return f"{float(a)} * {float(b)} = {float(a)* float(b)}"
        case "/":
            return f"{float(a)} / {float(b)} = {float(a) / float(b)}"

print("*** WELCOME TO THE CALCULATOR ***")


calculate = True

while calculate:
    print(calculator(a=input("Enter first number: "), operator=input("Enter the operator (+, -, *, /): "), b=input("Enter the second number: ")))
    again = input("Would you like to calculate again? (y/n): ").lower()
    if again == "y":
        calculate = True
    else:
        calculate = False