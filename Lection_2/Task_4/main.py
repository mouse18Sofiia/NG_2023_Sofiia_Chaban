minions = {'a', 'e', 'i', 'o', 'u'}
ans = set()
s = input("Your text:")
for letter in s:
  if letter in minions:
       ans.add(letter)
print(("Your vowels:"))
for letter in ans:
 print( letter, end = ' ')
print()