# Foydalanuvchidan sonlar sonini so‘raymiz
n = int(input("Nechta son kiritmoqchisiz? "))

# Bo‘sh ro‘yxat yaratamiz
sonlar = []

# Foydalanuvchidan n ta son kiritamiz
for i in range(n):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

# Juft va toq sonlar yig‘indisini hisoblaymiz
juft_yigindi = 0
toq_yigindi = 0

for son in sonlar:
    if son % 2 == 0:
        juft_yigindi += son
    else:
        toq_yigindi += son

# Natijani ekranga chiqaramiz
print(f"\nRo‘yxat: {sonlar}")
print(f"Juft sonlar yig‘indisi: {juft_yigindi}")
print(f"Toq sonlar yig‘indisi: {toq_yigindi}")
