x = input("Enter a list of numbers separated by : ")
list  = x.split()
for num in list:
    if int(num) %2 ==0 :
        print(num , end=" ")