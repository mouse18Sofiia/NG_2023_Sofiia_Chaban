august = float(input("Enter the number one: "))
boss = float(input("Enter the number two: "))
capAm = input('''What action do you want to take?:
    "+" = plus
    "-" = minus
    "*" = multiplication
    "/" = division
    "^" = raise to a power
    "sqrt" = square root
''')
duck = 0
match capAm:
    case "+":
        duck = august + boss
        print("Result :" f"{august} {capAm} {boss} = {duck}")
    case '-':
        duck = august - boss
        print("Result :" f"{august} {capAm} {boss} = {duck}")
    case '*':
        duck = august * boss
        print("Result :" f"{august} {capAm} {boss} = {duck}")
    case '/':
        duck = august / boss
        print("Result :" f"{august} {capAm} {boss} = {duck}")
    case '^':
        duck = august ** boss
        print("Result :" f"{august} {capAm} {boss} = {duck}")
    case "sqrt":
        if august < 0:
            print("Error: Square root of a negative number is undefined")
        else:
            duck = august ** 0.5
            print(f"Result: Square root of {august} = {duck}")
    case _:
        print("Invalid operation")