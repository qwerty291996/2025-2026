def hisobla(ifoda):
    # ifodani bo'laklarga ajratamiz
    ifoda = ifoda.replace("+-", "+-")  # +- ni qabul qilamiz
    return eval(ifoda)

# Foydalanuvchidan arifmetik ifodani so'raymiz
ifoda = input("Arifmetik ifodani kiriting  ")

# Hisoblash
natija = hisobla(ifoda)

# Natijani chiqaramiz
print(f"Natija: {natija}")
