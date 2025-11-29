# Boshlang'ich ro‘yxat
sonlar = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# Takrorlanuvchi sonlarni aniqlaymiz
takroriy_sonlar = []

for son in sonlar:
    if sonlar.count(son) > 1 and son not in takroriy_sonlar:
        takroriy_sonlar.append(son)

# Natijani chiqaramiz
print(f"Asl ro‘yxat: {sonlar}")
print(f"Takrorlanuvchi sonlar: {takroriy_sonlar}")

# Har bir takrorlanuvchi son nechta marta uchrashganini chiqaramiz
print("\nTakrorlanish soni:")
for son in takroriy_sonlar:
    print(f"{son} – {sonlar.count(son)} marta")
