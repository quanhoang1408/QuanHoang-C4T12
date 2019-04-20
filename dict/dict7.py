sc = {
    "name" : "full name is Lionel Andrés Messi Cuccittini ",
    "age" : "is now 31",
    "description" : "is a soccer star",
    "nationality" : "was born in argentina",
    "danh hieu" : "won many prizes, trong do co qua bong vang 2010 2011 2012 2015" ,
    "family" : "has one wife and a son"
}
while True :
    n = input("what do you want to know about lionel messi : ")
    a = n.lower()
    if a in sc.keys():
        print("Messi",sc[a])
    else :
        print("we dont have this in4")