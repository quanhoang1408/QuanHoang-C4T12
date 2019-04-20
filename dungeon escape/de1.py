keyy= 0
map = {
    "size x" : 4,
    "size y" : 4,
}
player = {
    'x': 1,
    'y':2
}
key = {
    'x': 2,
    'y':2
}
door = {
    'x': 3,
    'y':3
}
for y in range(4):
        for x in range(4):
            if x==player['x'] and y==player['y'] :
                print("P",end=" ")
            elif x==key['x'] and y==key['y'] :
                print("K",end=" ")
            elif x==door['x'] and y==door['y'] :
                print("E", end=" ")
            else :
                print("_",end=" ")
        print()
while True :
    n= input("nhap buoc di cua ban w/a/s/d: ")
    if n == "w":
        if player['y']>0 and player['y']<4 :
            player['y'] = player['y'] -1
    if n == "a" :
        if player['x']>0 and player['x']<4 :
            player['x']=player['x'] -1
    if n == "s" :
        if player['y']>-1 and player['y']<3:
            player['y'] = player['y'] +1
    if n == "d" :
        if player['x']>-1 and player['x']<3 :
            player['x'] = player['x'] + 1
    if player['x'] ==2 and player['y']==2 :
        #key co the thay doi
        print("you have got a key!")
        keyy = keyy +1
        while True :
            for y in range(4):
                for x in range(4):
                    if x==player['x'] and y==player['y'] :
                        print("P",end=" ")
                    elif x==door['x'] and y==door['y'] :
                        print("E", end=" ")
                    else :
                        print("_",end=" ")
                print()
            na= input("nhap buoc di cua ban w/a/s/d: ")
            if na == "w":
                if player['y']>0 and player['y']<4 :
                    player['y'] = player['y'] -1
            if na == "a" :
                if player['x']>0 and player['x']<4 :
                    player['x']=player['x'] -1
            if na == "s" :
                if player['y']>-1 and player['y']<3:
                    player['y'] = player['y'] +1
            if na == "d" :
                if player['x']>-1 and player['x']<3 :
                    player['x'] = player['x'] + 1
            if player['x']==3 and player['y']==3 and keyy==1 :
                for y in range(4):
                    for x in range(4):
                        if x==player['x'] and y==player['y'] :
                            print("P",end=" ")
                        else :
                            print("_",end=" ")
                    print()
                print("ez game :))")
                break
        break
    if player['x']==3 and player['y']==3 and keyy==0:
        print("find the key first")
    for y in range(4):
        for x in range(4):
            if x==player['x'] and y==player['y'] :
                print("P",end=" ")
            elif x==key['x'] and y==key['y'] :
                print("K",end=" ")
            elif x==door['x'] and y==door['y'] :
                print("E", end=" ")
            else :
                print("_",end=" ")
        print()
    if player['x'] ==2 and player['y']==2 :
        #key co the thay doi
        print
