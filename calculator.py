first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation or 'q' to quit: ")
result = None

while 1 == 1:
    if operation == "q":
        print("Exiting the calculator.")

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation")

    if result is not None:
        print("Result:", result)
