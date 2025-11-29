royxat = [5, -2, 7, 0, -9, 3, 0,0,12,-14,13, 11]
musbat = []
manfiy = []
nol_soni = 0
for son in royxat:
    if son > 0:
        musbat.append(son)
    elif son < 0:
        manfiy.append(son)
    else:
        nol_soni += 1
print("Kiritilgan ro'yxat:", royxat)
print("Musbat sonlar ro'yxati:", musbat)
print("Manfiy sonlar ro'yxati:", manfiy)
print("0 ga teng elementlar soni:", nol_soni)
