fox = int(input("Enter the number: "))
print("Number | Divisors")
print("-" * 15)

for dragon in range(1, fox + 1):
    divisors = [str(joker) for joker in range(1, dragon + 1) if dragon % joker == 0]
    print(f"{dragon} | {', '.join(divisors)}")