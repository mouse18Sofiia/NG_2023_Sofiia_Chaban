minions = {'a', 'e', 'i', 'o', 'u'}
banana = input("Your text:")
vowels = set(letter for letter in banana if letter in minions)
print("Your vowels:")
print(" ".join(vowels))