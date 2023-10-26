def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

user_input = int(input("Enter the number: "))

print("Number | Divisors")
print("-" * 15)

for i in range(1, user_input + 1):
    divisors = [str(j) for j in range(1, i + 1) if i % j == 0]
    print(f"{i} | {', '.join(divisors)}")

print("\nPrime numbers:")
prime_numbers = [str(i) for i in range(1, user_input + 1) if is_prime(i)]
print(", ".join(prime_numbers))