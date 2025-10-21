
n = int(input("n ni kiriting (n > 0): "))
a = float(input("a ni kiriting (haqiqiy son): "))

for i in range(1, n+1):
    daraja = a ** i
    print(f"{a}^{i} = {daraja}")

