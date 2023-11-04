# We create an empty list to store numbers from the entered characters
el = []

# We ask the user to enter characters
user_input = input("Enter an item: ")

# We go through each character in the entered line
for nn in user_input:
    # We check whether the symbol is a number
    if nn.isdigit():
        # If it is a number, we convert it to an integer and add it to the "el" list
        el.append(int(nn))

# We display the list of numbers that were entered
print("Your list is:", el)