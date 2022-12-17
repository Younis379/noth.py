name = input("name:")

if not len(name) > 3:
    print("can't be less than three character")

elif len(name) > 10:
    print("can't be greater than ten characters")

else:
    print("welcome to the program")