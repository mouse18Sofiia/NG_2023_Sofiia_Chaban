FirstN = float(input("Enter the number one: "))
SecondN = float(input("Enter the number two: "))
operation = input('''What action do you want to take?:
    "+" = plus
    "-" = minus
    "*" = multiplication
    "/" = division
    "^" = raise to a power
    "sqrt" = square root
''')


def calculate_result(operation, x, y):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        if y == 0:
            print("Error: Division by zero")
            return None
        return x / y
    elif operation == "^":
        return x ** y
    elif operation == "sqrt":
        if x < 0:
            print("Error: Square root of a negative number is undefined")
            return None
        return x ** 0.5
    else:
        print("Invalid operation")
        return None

result = calculate_result(operation, FirstN, SecondN)
if result is not None:
    print(f"Result: {FirstN} {operation} {SecondN} = {result}")