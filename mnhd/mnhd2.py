sum = 0
maytinh = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
} 
n = input("Nhap hang may tinh : ")
num = int(input("So luong may : "))
maytinh[n]=num
maytinh["DELL"] = 10
maytinh["MACBOOK"] = 2
print(maytinh)
print("so luong macbook la",maytinh["MACBOOK"])
for key in maytinh :
    sum = sum + maytinh[key]
print(sum)