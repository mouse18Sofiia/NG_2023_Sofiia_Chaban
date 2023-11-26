import math
FirstN = float(input("Enter the number one: "))
SecondN = float(input("Enter the number two: "))
match input('Choose an action\n/,*,+,-,root,power\n'):
      case "/":
            print(FirstN/SecondN)
      case"*":
            print(FirstN*SecondN)
      case"+":
            print(FirstN+SecondN)
      case "-":
            print(FirstN-SecondN)
      case "power":
            print(FirstN**SecondN)
      case "root":
            print(FirstN**(1/SecondN))
      case _:
            print("Values isn't validity")