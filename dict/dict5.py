sc = {
    "name" : "Messi",
    "age" : 31,
    "description" : "soccer star",
    "nationality" : "argentina"
}
print(sc)
check = input("type key :")
if check in sc.keys() :
    print("True")
else : 
    print("False")