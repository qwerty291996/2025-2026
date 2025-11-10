# 1-masala
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

# Uchta son ichidan yig'indisi eng katta bo'lgan ikkitasini tanlaymiz
if a + b >= a + c and a + b >= b + c:
    print(f"Eng katta yig'indiga ega sonlar: {a}, {b}")
elif a + c >= a + b and a + c >= b + c:
    print(f"Eng katta yig'indiga ega sonlar: {a}, {c}")
else:
    print(f"Eng katta yig'indiga ega sonlar: {b}, {c}")


# 2-masala
n = int(input("n ni kiriting (n > 0): "))
s = 1.0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    s += 1 / factorial

print(f"Yig'indi: {s}")


# 3-masala
satr = input("Satrni kiriting: ")

lotin_kichik = 'abcdefghijklmnopqrstuvwxyz'
kirill_kichik = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

soni = 0

for harf in satr:
    if harf.lower() in lotin_kichik or harf.lower() in kirill_kichik:
        soni += 1

print(f"Kichik lotin va kirill harflarining umumiy soni: {soni}")
