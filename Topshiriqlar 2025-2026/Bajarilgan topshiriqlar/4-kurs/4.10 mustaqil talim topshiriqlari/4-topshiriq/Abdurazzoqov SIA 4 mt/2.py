# Faylga to'liq manzil
file_path = r"C:\Users\abdurazzoqov_a\Desktop\Abdurazzoqov SIA 4 mt\log.txt"

# 1. Faylga qo'shimcha yozish
with open(file_path, "a", encoding="utf-8") as f: # To'liq manzil ishlatildi
    f.write("YAngilangan ma'lumot\n")

# 2. Fayldan oxirgi yozuvni o'qish
try:
    with open(file_path, "r", encoding="utf-8") as f: # To'liq manzil ishlatildi
        lines = f.readlines()
        if lines:
            print("Oxirgi yozuv:", lines[-1].strip())
        else:
            print("Fayl bo'sh.")
except FileNotFoundError:
    print(f"⚠️ Xatolik: {file_path} manzili topilmadi. Papka mavjudligini tekshiring.")