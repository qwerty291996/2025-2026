def maydon_rangi(x, y):
    if (x + y) % 2 == 1:
        return "Oq"
    else:
        return "Qora"
x = int(input("x ni kiriting (1 dan 8 gacha): "))
y = int(input("y ni kiriting (1 dan 8 gacha): "))

if 1 <= x <= 8 and 1 <= y <= 8:
    print(f"({x},{y}) maydonning rangi: {maydon_rangi(x, y)}")
else:
    print("Kiritilgan koordinatalar 1 dan 8 gacha bo'lishi kerak.")
