first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation: ")
result = None

# Add loop and ask to continue or quit
if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    result = first_number / second_number
else:
    print("Invalid operation")

print(result)


# Convert C -> F , F -> C, miles -> km, km -> miles
# 1. C -> F ,
# 2. F -> C,
# 3. miles -> km,
# 4. km -> miles
