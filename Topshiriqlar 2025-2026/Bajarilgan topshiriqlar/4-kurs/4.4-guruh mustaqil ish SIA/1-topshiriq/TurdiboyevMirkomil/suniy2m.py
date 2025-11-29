a = float(input("a ni kiriting (haqiqiy son): "))
n = int(input("n ni kiriting (butun va n>0): "))

for i in range(1, n+1):
    print(f"{a}^{i} = {a**i}")
