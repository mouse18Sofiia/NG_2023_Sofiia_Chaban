#We ask the user to enter a number
user_input = int(input("Enter a number: "))

# We display the table header
print("Number | Dividers")
print("-" * 15)

# We go through the numbers from 1 to the entered number (inclusive)
for number in range(1, user_input + 1):
    # We find all the divisors of the number number
    divisors = [str(divisor) for divisor in range(1, number + 1) if number % divisor == 0]
    
    # Output the number and its comma-separated divisors
    print(f"{number} | {', '.join(divisors)}")
    # We derive all "Simple" numbers
print("Simple numbers:")
for number in range(2, user_input + 1):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number)