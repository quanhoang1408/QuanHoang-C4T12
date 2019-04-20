list = ['blue', 'green', 'red']
print(*list, sep=", ")
n = input("New color")
list.append(n)
print(*list, sep=", ")