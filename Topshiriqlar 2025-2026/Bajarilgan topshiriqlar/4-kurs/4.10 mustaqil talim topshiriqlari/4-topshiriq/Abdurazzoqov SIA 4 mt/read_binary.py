with open("image.png", "rb") as f:
    data = f.read()          # butun faylni o‘qish
    first_100 = data[:100]   # birinchi 100 bayt
print(first_100)
with open("image_copy.png", "wb") as f_copy:
    f_copy.write(data)
print("Fayl muvaffaqiyatli nusxalandi!")
