cat = []
mouse = input("Enter an item : ")
for dog in mouse:
    if dog.isdigit():
        cat.append(int(dog)) 
print("Your list is :" , (cat) )