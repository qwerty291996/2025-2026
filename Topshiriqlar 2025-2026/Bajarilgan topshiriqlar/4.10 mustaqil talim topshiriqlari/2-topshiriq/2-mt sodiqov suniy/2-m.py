sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
yangi = sonlar[:]  
for i in range(1, len(sonlar)-1):
    yangi[i] = (sonlar[i-1] + sonlar[i+1]) / 2
print("Yangi ro'yxat:", yangi)
