vowels = {'a', 'e', 'i', 'o', 'u'}
user_input = input("Your text:")
vowels_in_text = set(letter for letter in user_input if letter in vowels)
print("Your vowels:")
print(" ".join(vowels_in_text))