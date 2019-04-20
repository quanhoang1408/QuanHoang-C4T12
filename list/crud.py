quan = ['soccer', 'basketball', 'swimming', 'jogging']
while True :
    x = input("enter C or U or R or D : ")
    if x == "C" :
        xc = input("nhap mon the thao ban yeu thich : ")
        quan.append(xc)
        print(*quan,sep=", ")
    elif x == "R" :
        so_phan_tu = len(quan)
        if so_phan_tu == 0 :
            print("Khong co phan tu nao")
        else :
            for i in range(so_phan_tu) :
                print(quan[i])
    elif x == "U" :
        vi_tri = int(input("Nhap vi tri ban muon thay the: "))
        vi_tri_thay_doi = vi_tri -1
        so_phan_tu = len(quan)
        tru_so_phan_tu = 0 - so_phan_tu
        if vi_tri > so_phan_tu :
            print("khong du so phan tu")
        elif vi_tri < tru_so_phan_tu :
            print("khong du so phan tu")
        else :
            mon_the_thao_moi = input("Nhap thu ban muon thay: ")
            quan[vi_tri_thay_doi] = mon_the_thao_moi
            print(*quan,sep=", ")
    elif x == "D" :
        vi_tri = int(input("Nhap vi tri ban muon xoa: "))
        vi_tri_xoa = vi_tri -1 
        so_phan_tu = len(quan)
        tru_so_phan_tu = 0 - so_phan_tu
        if vi_tri > so_phan_tu :
            print("khong du so phan tu")
        elif vi_tri < tru_so_phan_tu :
            print("khong du so phan tu")
        else :
            quan.pop(vi_tri_xoa)
            print(*quan,sep=", ")


