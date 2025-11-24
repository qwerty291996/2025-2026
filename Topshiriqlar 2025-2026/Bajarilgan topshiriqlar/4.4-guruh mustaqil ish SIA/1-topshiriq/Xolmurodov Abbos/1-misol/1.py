x1, y1 = map(int, input("Birinchi koordinatalarni kiriting (x1 y1): ").split())
x2, y2 = map(int, input("Ikkinchi koordinatalarni kiriting (x2 y2): ").split())

if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print("Rost: Ot bir yurishda bu maydonga o‘tadi.")
else:
    print("Yolg'on: Ot bir yurishda bu maydonga o‘tolmaydi.")
