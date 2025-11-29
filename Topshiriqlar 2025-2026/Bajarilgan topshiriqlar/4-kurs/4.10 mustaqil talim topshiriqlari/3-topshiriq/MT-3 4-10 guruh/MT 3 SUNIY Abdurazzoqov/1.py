# salom_ber() nomli funksiya yozamiz
def salom_ber(ism):
    """Foydalanuvchining ismini qabul qilib, salom beruvchi funksiya"""
    matn = f"Salom, {ism}!"
    print(matn)
    return matn

# Foydalanuvchidan ismni so‘raymiz
ism_kirit = input("Ismingizni kiriting: ")

# Funksiyani chaqiramiz
salom_ber(ism_kirit)
