tudien = {
    'dog' : 'cho',
    'cat' : 'meo',
    'hat' : 'mu',
    'mother' : 'me',
    'father' : 'bo'
}
check = input("nhap tu ban muon tra")
if check in tudien.keys() :
    print (tudien[check])
else :
    print("our dictionary do not have this word :))")