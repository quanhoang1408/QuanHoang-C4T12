ten = ['hbt','hk','bd','hd','tx']
max=0
min=10000
sodan = [1456,3400,2300,1200,9900]
for i in range(5):
    if int(sodan[i])>max :
        max =int(sodan[i])
        max_ten = ten[i]
for n in range(5):
    if int(sodan[n])<min :
        min = int(sodan[n])
        min_ten = ten[n]
print(max,max_ten,min,min_ten)
