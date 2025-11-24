def katta_soz(matn):
    # Matnni so'zlarga bo'lish
    sozlar = matn.split()
    # Eng uzun so'zni topish
    eng_uzun = max(sozlar, key=len)
    return eng_uzun
# Misol uchun
matn = "Bu yerda enguzunso'z topilishi kerak"
print(katta_soz(matn))
