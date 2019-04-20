list = [99,939,9230,2344,1408]
print(*list)
i =0
n = int(input("Kiem tra so nay co trong day k : "))
while True :
    if n == int(list[i]) :
        print("Found position", i+1)
        break
    elif i <4 :
        i = i+1
    else :
        print("no")
        break
    
        
