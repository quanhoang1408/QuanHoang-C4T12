print("dang ky tai khoan")
a1 = input("nhap tai khoan : ")
while True :
    a2 = input("nhap mat khau cua ban : ")
    if len(a2)>8 :
        if a2.isalpha() or a2.isdigit() :
            print("mat khau can co ca chu va so")
        else :
            b = input("nhap lai mat khau :")
            if a2==b :
                while True :
                    a3 = input("Nhap email: ")
                    if "@" and "." not in a3 :
                        print("wrong email")
                    else :
                        print("ok")
                        break
                break
            else :
                print("mat khau khong trung khop")
    else :
        print("password have at least 8 characters")