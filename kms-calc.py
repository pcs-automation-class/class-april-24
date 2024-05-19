while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation: ")
    result = None

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
    print(result)

    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input == "y":
        continue
    if continue_input == "n":
        print("Quit")
    break

while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation: ")
    result = None

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
    print(result)

    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input == "y":
        continue
    if continue_input == "n":
        print("Quit")
    break