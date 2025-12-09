import os
def royxatni_chiqar(katalog_yoli):
    try:
        fayllar = os.listdir(katalog_yoli)
        print("\n Katalogdagi fayllar:")
        for f in fayllar:
            print(f)
    except FileNotFoundError:
        print("Bunday katalog mavjud emas!")
    except PermissionError:
        print("Ruxsat berilmagan katalog!")
yol = input("Fayllar ro'yxatini ko'rmoqchi bo'lgan katalog manzilini kiriting:\n> ")
royxatni_chiqar(yol)
