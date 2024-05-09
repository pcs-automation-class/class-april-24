# Calculator

print("Welcome to calculator")
result = None
while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Enter operation: ")
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero!")
            continue
        else:
            result = first_number / second_number
    else:
        print("Invalid operation")
    print(result)
    continue_input = input("Do you want to continue? (yes/no): ")
    if continue_input == "yes":
        continue
    if continue_input == "no":
        print("Exiting the program...")
    else:
        print("Invalid input! Please enter a valid option.")


