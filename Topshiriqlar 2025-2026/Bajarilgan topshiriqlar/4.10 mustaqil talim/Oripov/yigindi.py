n = int(input("n ni kiriting (n > 0): "))
a = float(input("a ni kiriting: "))
S = 0
for i in range(0, n + 1):
    daraja = a ** i
    S += daraja
    print(f"a^{i} = {daraja}")
print(f"Yig‘indi: {S}")
