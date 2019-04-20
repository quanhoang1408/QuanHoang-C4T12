sum=0
maytinh = {
    "HP" : 20,
    "DELL" : 60,
    "MACBOOK" : 12,
    "ASUS" : 30
} 
maytinh["TOSHIBA"] = 10
maytinh["MACBOOK"] = 2
maytinh["FUJITSU"] = 15
maytinh["ALIENWARE"] = 5
price ={
"HP": 600,
"DELL": 650,
"MACBOOK": 12000,
"ASUS": 400,
"ACER": 350,
"TOSHIBA": 600,
"FUJITSU": 900,
"ALIENWARE": 1000
}
for key in maytinh:
    gia = int(maytinh[key])*int(price[key])
    sum = sum + gia
    print(key,gia)
print("Tong gia tri kho la:", sum)