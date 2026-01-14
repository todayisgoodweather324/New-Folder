import sys
def add():
    """to validate two numbers"""
    discontinue = "q".lower()
    while True:
        try:
            user_input = input("Please type a number:\n")
            if user_input == discontinue:
                print("Bye")
                sys.exit()
            num1 = int(user_input)
            break
        except ValueError:
            print("Type digits.")
    while True:
        operator = input("What is the operator:\n")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            break
        elif operator == discontinue:
            sys.exit()
        else:
            print("The operator is not valid")

    while True:
        try:
            user_input = input("Please type another number:\n")
            if user_input == discontinue:
                print("Bye")
                sys.exit()
            num2 = int(user_input)
            break
        except ValueError:
            print("Only digits")
    return num1, num2, operator
numbers = add
while True:

    x, y, operator = numbers()# the name of the function has been changed
    if operator == "+":
        print(f"The result is {x + y}")
    elif operator == "-":
        print(f"The result is {x - y}")
    elif operator == "*":
        print(f"The result is {x * y}")
    elif operator == "/":
        print(f"The result is {x / y}")
    elif user_input == discontinue:
        print("Bye")
        sys.exit()
    else:
        print("Invalid input")
        continue