sum = 0
bangluong =[
    {
    "name" :"huy",
    "role" : "waiter" ,
    "hours" : 12,
    "salary per hour" :0.8
},
    {
    "name": "tung",
    "role" : "cook",
    "hours" : 24,
    "salary per hour" :1.5
},
 {
    "name" : "mduc",
    "role" :"manager" ,
    "hours" : 20,
    "salary per hour" :2
},
    {
    "name" : "don",
    "role" :"waiter" ,
    "hours" : 12,
    "salary per hour" :0.9
},
    {
    "name" : "hduc",
    "role" :"waiter" ,
    "hours" : 14,
    "salary per hour" :0.7
}
]
bangluong[0]= {
    "name" : 'huyen',
    'role' : 'waitress',
    "hours": 14,
    "salary per hour" : 1

}
print(bangluong)
for item in bangluong:
    luong = item["hours"]*item["salary per hour"]
    item["luong"]=luong
    print (item)
    sum = sum + item["luong"]
print("so tien phai tra", sum)