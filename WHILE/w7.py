
while True :
    n = input("enter your password:")
    if n.isalpha():
        print("again")
    elif n.isdigit():
        print("again")
    else :
        print("ok")
        break