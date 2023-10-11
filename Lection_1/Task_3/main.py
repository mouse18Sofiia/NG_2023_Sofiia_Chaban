print("Hi! Please enter a number in degrees in °C or °F")
n1 = int(input("Your number is: "))
n2 = int(input("If your number is in °C, press 1, or if in °F, press 0: "))
if n2==1:
    print("This degree is in °F: {} ".format(n1*1.8+32))
if n2==0:
    print("This degree is in °C: {} ".format((n1-32)/1.8))