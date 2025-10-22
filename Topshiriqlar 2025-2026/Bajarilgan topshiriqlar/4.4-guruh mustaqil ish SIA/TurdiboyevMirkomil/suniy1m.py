def farsin_yurish(x1, y1, x2, y2):
    return abs(x2 - x1) == abs(y2 - y1)

x1 = int(input("Birinchi koordinata x1 (1-8): "))
y1 = int(input("Birinchi koordinata y1 (1-8): "))
x2 = int(input("Ikkinchi koordinata x2 (1-8): "))
y2 = int(input("Ikkinchi koordinata y2 (1-8): "))

if farsin_yurish(x1, y1, x2, y2):
    print("Farsin shu yurishda o'ta oladi.")
else:
    print("Farsin shu yurishda o'ta olmaydi.")
