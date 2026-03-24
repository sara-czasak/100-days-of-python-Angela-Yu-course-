def calculator(a, b, operator):
    if a == "" or b == "" or operator == "":
        return "I'm sorry, I didn't catch that.."
    match operator:
        case "+":
            return f"{int(a)} + {int(b)} = {int(a) + int(b)}"
        case "-":
            return f"{int(a)} - {int(b)} = {int(a) - int(b)}"
        case "*":
            return f"{int(a)} * {int(b)} = {int(a) * int(b)}"
        case "/":
            return f"{int(a)} / {int(b)} = {int(a) / int(b)}"

print("*** WELCOME TO THE CALCULATOR ***")
print(calculator(a=input("Enter first number"), b=input("Enter the second number: "), operator=input("Enter the operator (+, -, *, /): "),
))