while True:
    n = input("Nhap password:")
    if n.isalpha():
        print("again")
    elif len(n) <9:
        print("again")
    else :
        if n.isupper():
            print("again")
        elif n.islower():
            print("again")
        else :
            print("ok")
            break
