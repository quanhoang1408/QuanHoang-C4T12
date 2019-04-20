ten = [99,98,97,4423,43,25]
n = int(input("Nhap diem moi:"))
ten.append(n)
ten.sort(reverse=True)
for index, item in enumerate(ten):
    if index < 5 :
        print(index+1,".",item)
    else :
        break