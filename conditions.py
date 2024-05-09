age = int(input("Enter your age: "))

if not age >= 16:
    print("Price $10")
elif age >= 16 and age < 25:
    print("Price $15")
elif age>=25 and age < 50:
    print("Price $20")
else:
    print("Free")

# if a > b:
#     print("a is bigger than b")

# if a < b:
#     print("b is bigger than a")

# And
# First| Second | Result
# True | True   | True
# True | False  | False
# False| True   | False
# False| False  | False

# Or
# First| Second | Result
# True | True | True
# True | False| True
# False| True | True
# False| False| False

# Not
# Condition | Result
# not True | False
# not False | True

