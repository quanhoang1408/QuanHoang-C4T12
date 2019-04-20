items = ['pho', 'com rang', 'mi xao']
print(items)
new_item = input("Nhap mon moi vao : ")
items.append(new_item)
print(items)
print(items[0])
print(*items, sep=", ")
#update
items[0] = "kho ga"
print(*items)
#update w input
i = int(input("Nhap vi tri"))
n = input("Nhap mon moi :")
items[i] = n
print(*items)
items.pop[1]
items.remove(0)
print(items)