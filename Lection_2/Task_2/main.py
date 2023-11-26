list_of_numbers = []
user_input = input("Enter an item: ")
for symbol in user_input:
    if symbol.isdigit():
        list_of_numbers.append(int(symbol))
print("Your list is:", list_of_numbers)