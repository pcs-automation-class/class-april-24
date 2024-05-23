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


# def abc(a, b, c):
#     return a + b - c
#
# text_to_print = abc(a=10, b=2, c=2)
# print(text_to_print)


# def func(a, b):
#     assert a == b, "a not equal b in this test"
#
# func(a=1, b=4)


# def func(a, b):
#     assert [], "a not equal b in this test"

# func(a=1, b=2)