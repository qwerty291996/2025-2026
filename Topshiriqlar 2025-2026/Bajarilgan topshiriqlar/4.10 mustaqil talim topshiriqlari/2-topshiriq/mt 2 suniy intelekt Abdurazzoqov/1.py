# Matnli ro‘yxat yaratamiz
mevalar = ['olma', 'banan', 'uzum', 'olcha']
# Ro‘yxat elementlarini tartib raqami bilan chiqaramiz
print("Mevalar ro‘yxati:")
for i, meva in enumerate(mevalar, start=1):
    print(f"{i}-element: {meva}")
# Foydalanuvchidan indeks so‘raymiz
try:
    indeks = int(input("\nQaysi mevaning nomini bilmoqchisiz? Indeksni kiriting: "))
    # Indeks to‘g‘riligini tekshiramiz
    if 1 <= indeks <= len(mevalar):
        print(f"Siz tanlagan meva: {mevalar[indeks - 1]}")
    else:
        print("Xatolik: Bunday indeks mavjud emas!")
except ValueError:
    print("Xatolik: Iltimos, butun son kiriting!")
