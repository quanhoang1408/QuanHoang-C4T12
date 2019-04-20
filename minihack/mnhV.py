sum=0
import random
while True :
    x = random.randint(1,11)
    y = random.randint(1,11)
    z = random.choice(["+","-"])
    if z == "+":
        x1 = x+y
        e = random.randint(-1,1)
        x2 = x1+e
        print(x,z,y,"=",x2)
        n = input("t or f :")
        if e==0 :
            if n =="t":
                sum = sum+1
            else :
                print("Your score is",sum)
                break
        if e!=0 :
            if n =="f":
                sum = sum +1
            else :
                print("Your score is",sum)
                break

