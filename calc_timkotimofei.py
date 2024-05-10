#Calculator

class Calculator:

    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def divide(self, a, b):
        print(a / b)


while True:
    calc = Calculator()
    a = int(input("Enter a first number:"))
    b = int(input("Enter a second number:"))
    operator = input("Enter operator:")
    if operator == "+":
        calc.add(a, b)
    elif operator == "-":
        calc.subtract(a, b)
    elif operator == "*":
        calc.multiply(a, b)
    elif operator == "/":
        calc.divide(a, b)
    else:
        print("Invalid operator")
    choice = input("Do you want to continue?(y/n)")
    if choice == "n":
        print("Thank you for using Calculator")
        break