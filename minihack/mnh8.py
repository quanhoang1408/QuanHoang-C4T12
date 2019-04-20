n = int(input("so canh ban muon ve"))
angle = 360/n
from turtle import *
speed(-1)
shape("turtle")
color("green")
for i in range(n):
    forward(100)
    right(angle)
mainloop()