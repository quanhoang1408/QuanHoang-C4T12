maytinh = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30
} 
maytinh["TOSHIBA"] = 10
maytinh["DELL"] = maytinh["DELL"] + 10
maytinh["MACBOOK"] = 2
maytinh["FUJISU"] = 15
maytinh["ALIENWARE"] = 5
print(maytinh)
n = input("Nhap may ban muon mua:")
number = int(input("So luong : "))
maytinh[n] = maytinh[n] - number
print(maytinh)
nn = input("Nhap may va so luong tren cung 1 dong cach nhau boi :")
list = nn.split(":")
a = list[0]
b = list[1]
maytinh[a]= maytinh[a] - int(b)
print(maytinh)