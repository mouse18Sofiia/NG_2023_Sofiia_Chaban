file_name = input("Enter a file name: ")

# We initialize an empty dictionary to save the number of characters
character_count = {}

try:
    # Open the file for reading(r)
    with open(file_name, 'r') as file:
        # We read the contents of the file
        content = file.read()
        # We go through each character in the file content
        for char in content:
            # We add a symbol to the dictionary and increase the counter
            character_count[char] = character_count.get(char, 0) + 1

    # We output the result in the form of a dictionary
    print("Character count result:")
    for char, count in character_count.items():
        print(f"'{char}': {count}")

except FileNotFoundError:
    print(f"File'{file_name}' not found.")
except Exception as el:
    print(f"An error occurred: {str(el)}")