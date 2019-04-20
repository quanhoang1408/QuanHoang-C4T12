import random
listt = ['cho','meo']
x =random.choice(listt)
shuffled = list(x)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print(shuffled)
n = input("nhap kq:")
if n == x  :
    print("Dung")
else : 
    print("Sai")