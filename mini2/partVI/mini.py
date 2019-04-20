sum=0
ten = ['hbt','hk','bd','hd','tx']
sodan = [1456,3400,2300,1200,9900]
dientich =[2,3,4,5,9]
matdo=[0]
for i in range(len(ten)) :
    n= int(sodan[i])/int(dientich[i])
    matdo.append(n)
matdo.remove(0)
print(matdo)
for n in matdo :
    sum = sum+n
average = sum/len(matdo)
print(average)
