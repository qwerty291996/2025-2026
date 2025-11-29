x1, y1 = map(int, input("(x1 y1): ").split())
x2, y2 = map(int, input("(x2 y2): ").split())

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("Rost ")
else:
    print("Yolg‘on ")