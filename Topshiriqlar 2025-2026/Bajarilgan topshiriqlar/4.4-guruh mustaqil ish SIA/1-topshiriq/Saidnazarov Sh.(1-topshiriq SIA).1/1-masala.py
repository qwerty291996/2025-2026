x1 = int(input("x1 ni kiriting : "))
y1 = int(input("y1 ni kiriting : "))
x2 = int(input("x2 ni kiriting : "))
y2 = int(input("y2 ni kiriting : "))

if abs(x1 - x2) == abs(y1 - y2):
    print("Rost: xa o'ta oladi")
else:
    print("Yolg‘on: yoq' fil bunday yurolmaydi")
#2-usul
f = bool(abs(x1 - x2) == abs(y1 - y2))
print(f"Fil bir yurishda o‘ta oladimi? {f}")
