u = str(input("nhap username:"))
p = str(input("nhap password:"))
if u == "techkids" :
    if p == "codethechange" :
        print("Welcome, superuser")
    else : 
        print("invalid password")
else : 
    print("You are not superuser")