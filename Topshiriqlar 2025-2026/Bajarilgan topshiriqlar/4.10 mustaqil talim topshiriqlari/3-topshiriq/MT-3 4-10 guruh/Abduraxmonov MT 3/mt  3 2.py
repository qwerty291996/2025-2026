def oraliq_yigindi(a, b):
    if a > b:
        a, b = b, a  
    yigindi = 0
    for son in range(a, b + 1):
        yigindi += son
    return yigindi
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

natija = oraliq_yigindi(a, b)
print(f"{a} dan {b} gacha bo'lgan sonlarning yig'indisi: {natija}")
