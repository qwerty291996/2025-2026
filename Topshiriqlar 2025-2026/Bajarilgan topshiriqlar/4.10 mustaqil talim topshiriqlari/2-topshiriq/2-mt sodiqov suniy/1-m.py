sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
print("Eng kichik indeks:", sonlar.index(min(sonlar)))
print("Eng katta indeks:", sonlar.index(max(sonlar)))
