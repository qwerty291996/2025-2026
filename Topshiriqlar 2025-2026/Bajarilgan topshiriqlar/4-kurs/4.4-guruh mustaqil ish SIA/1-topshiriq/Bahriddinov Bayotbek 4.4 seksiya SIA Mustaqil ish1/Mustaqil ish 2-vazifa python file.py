def yigindi(n):
    # Yig'indini hisoblash
    s = 0
    for i in range(1, n + 1):
        # Har bir qo'shiluvchining qiymatini hisoblash
        term = 1 + i / 10
        # Yig'indiga qo'shish
        s += term
    return s

# Foydalanuvchidan n ni olish
n = int(input("n ni kiriting (n>0): "))
print("Yig'indi =", yigindi(n))

