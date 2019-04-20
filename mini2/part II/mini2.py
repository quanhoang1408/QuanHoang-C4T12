list = ['blue', 'green', 'red']
print(*list, sep=", ")
n = input("Nhap mau hoac nhap so ban muon xoa: ")
if n.isdigit() :
    t = int(n)-1
    list.pop(t)
    print(*list,sep=", ")
else :
    list.remove(n)
    print(*list,sep=", ")