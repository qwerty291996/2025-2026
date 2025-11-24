with open('log.txt', 'a', encoding='utf-8') as file:
    file.write("Yangilangan malumot\n")
try:
    with open('log.txt', 'r', encoding='utf-8') as file:
        content = file.read().strip().split('\n')
        if content:
            last_entry = content[-1]
            print("Oxirgi yozuv:", last_entry)
        else:
            print("Fayl bo'sh")
except FileNotFoundError:
    print("log.txt fayli topilmadi. Yangi fayl yaratildi.")
