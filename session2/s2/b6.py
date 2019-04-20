a = float(input("nhap a"))
b = float(input("Nhap b"))
c = float(input("Nhap c"))
d = b*b - 4*a*c
if a == 0 :
    print("co nghiem vlvlvlvlvlvlvlvlvlvll")
    print(-c/b)
else :
    if d<0 :
        print("vo nghiem")
    elif d == 0 :
        print("nghiem kep")
        print(-b/2*a)
    else :
        print("co nghiem")
        print((-b-d**(1/2))/(2*a),(-b+d**(1/2))/(2*a))