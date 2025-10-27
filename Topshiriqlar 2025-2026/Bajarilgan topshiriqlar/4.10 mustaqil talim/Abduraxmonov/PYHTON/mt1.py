x = int(input("x ni kiriting : "))
y = int(input("y ni kiriting : "))
if 1 <= x <= 8 and 1 <= y <= 8:
    if (x + y) % 2 == 0:
        print(" qora katak.")
    else:
        print("( oq katak.")
else:
    print("x va y 1 dan 8 gacha butun son bo‘lishi kerak!")
