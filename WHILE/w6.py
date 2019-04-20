
print("""
How many legs a spider have?
    1. None
    2. 4 legs
    3. 8 legs
    4. 12 legs""")
x = input("Your answer : ")
while True :
    if x == "3":
        print("You are correct")
        break
    elif x == "4":
        print("Wrong, the answer is 3")
        break
    elif x == "1":
        print("Wrong, the answer is 3")
        break
    elif x == "2":
        print("Wrong, the answer is 3")
        break
    else:
        y = input("The answer must be 1,2,3 or 4, enter again :")
        if y == "3":
            print("You are correct")
            break
        elif y == "4":
            print("Wrong, the answer is 3")
            break
        elif y == "1":
            print("Wrong, the answer is 3")
            break
        elif y == "2":
            print("Wrong, the answer is 3")
            break
