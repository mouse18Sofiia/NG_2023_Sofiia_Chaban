a = float(input("Enter the number а: "))
b = float(input("Enter the number b: "))
c = input('''What action do you want to take?:
    "+" = plus
    "-" = minus
    "*" = multiplication
    "/" = division
    "^" = raise to a power
''')
d = 0
match c:
    case "+":
        d = a + b
        print("Result :" f"{a} {c} {b} = {d}")
    case '-':
        d = a - b
        print("Result :" f"{a} {c} {b} = {d}")
    case '*':
        d = a * b
        print("Result :" f"{a} {c} {b} = {d}")
    case '/':
        d = a / b
        print("Result :" f"{a} {c} {b} = {d}")
    case '^':
        d = a ** b
        print("Result :" f"{a} {c} {b} = {d}")