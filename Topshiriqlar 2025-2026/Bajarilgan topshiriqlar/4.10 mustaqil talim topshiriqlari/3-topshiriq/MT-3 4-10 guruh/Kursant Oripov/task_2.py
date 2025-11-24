def geometrik_orta(sonlar):
    kopaytma = 1
    for s in sonlar:
        kopaytma *= s
    return kopaytma ** (1 / len(sonlar))
n = int(input("Ro'yhat nechta elementdan tashkil topgan? n = "))
sonlar = []
for i in range(n):
    qiymat = float(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(qiymat)
natija = geometrik_orta(sonlar)
print("Geometrik o'rta:", natija)
