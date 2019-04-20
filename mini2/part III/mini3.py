input_string = input("Enter a list element separated by space ")
list  = input_string.split()
sum = 0
for num in list:
    sum = sum + int (num)
print("Sum = ",sum)