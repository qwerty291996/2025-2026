# Matnlardan iborat ro‘yxat
sozlar = ['dasturlash', 'python', 'intellekt', 'suniy', 'tarmoq']
# Har bir so'zning uzunligini topamiz
uzunliklar = [len(soz) for soz in sozlar]
# Natijani chiqaramiz
print("So‘zlar ro‘yxati:", sozlar)
print("Ularning uzunliklari:", uzunliklar)
# Eng uzun so‘z uzunligini aniqlaymiz
max_uzunlik = max(uzunliklar)
# Eng uzun so‘z(lar)ni topamiz
eng_uzun_sozlar = [soz for soz in sozlar if len(soz) == max_uzunlik]
# Natijani chiqaramiz
print(f"\nEng uzun so‘z uzunligi: {max_uzunlik} ta belgi")
if len(eng_uzun_sozlar) == 1:
    print(f"Eng uzun so‘z: {eng_uzun_sozlar[0]}")
else:
    print("Bir nechta eng uzun so‘zlar mavjud:")
    for s in eng_uzun_sozlar:
        print("-", s)
