sum = 0
win = {
    "1" : """
        cau 1 : pewpew que o dau ? :)))
        A : Ha Noi
        B : Sai Gon
        C : Da Nang
        D : Hai Phong
        """,
    "2" : """
        cau 2 : world cup duoc bat dau tu nam nao ?
        A : 1930
        B : 1932
        C : 1980
        D : 1950
        """,
    "3" : """
        cau 3 : meo may doreamon so con gi nhat ?
        A : con bo
        B : con cho
        C : con chuot
        D : con nguoi
    """,
    "4" : """
        cau 4 : "avengers : endgame" ra mat nam bao nhieu ?
        A : 2018
        B : 2019
        C : 2020
        D : 2017"""
}
for key in win :
    print (win[key])
    answer = input("Nhap cau tra loi : ")
    if key == "1" :
        if answer == "D":
            print ("you got 1 point")
            sum = sum +1
        else :
            print("wrong answer")
    if key == "2" :
        if answer == "A" :
            print ("right!")
            sum = sum +1
        else :
            print ("wrong")
    if key == "3" :
        if answer == "C" :
            print("great !")
            sum = sum +1
        else :
            print("wrong ans")
    if key == "4" :
        if answer == "B" :
            print("dung")
            sum = sum +1
        else :
            print("sai")
print ("Tong diem cua ban la :",sum)
print("Ban da tra loi dung", sum*25,"%")