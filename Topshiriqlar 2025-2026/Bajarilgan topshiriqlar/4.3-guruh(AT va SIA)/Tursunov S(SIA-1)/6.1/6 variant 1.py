def farzin_yurishi(x1, y1, x2, y2):

    if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
        return True
    else:
        return False

x1 = int(input("x1 (1-8): "))
y1 = int(input("y1 (1-8): "))
x2 = int(input("x2 (1-8): "))
y2 = int(input("y2 (1-8): "))
if farzin_yurishi(x1, y1, x2, y2):
    print("Farzin bir yurishda o'ta oladi.")
else:
    print("Farzin bir yurishda o'ta olmaydi.")
