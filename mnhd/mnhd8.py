character= {
    "name" : "light",
    "age" : 17,
    "streghth" : 8,
    "defense" : 10,
    "backpack" : ["shield","breadloaf"],
    "gold" : 100,
    "level" : 2
}
print(character)
skill1 ={
    "Name" : "Tackle",
    "Minimum level" : 1,
    "Damage" : 5,
    "Hit rate" : 0.3
}
skill2 = {
    "Name": "Quick attack",
    "Minimum level": 2,
    "Damage": 3,
    "Hit rate": 0.5
}
skill3 = {
    "Name" :"Strong kick",
    "Minimum level":4,
    "Damage" :9,
    "Hit rate" :0.2
}
skill=[skill1,skill2,skill3]
for i in range(3):

    print(i+1,skill[i])
n = int(input("choose the skill u want"))
if n<3:
    print("ok")
else :
    print("your level is not enough")
