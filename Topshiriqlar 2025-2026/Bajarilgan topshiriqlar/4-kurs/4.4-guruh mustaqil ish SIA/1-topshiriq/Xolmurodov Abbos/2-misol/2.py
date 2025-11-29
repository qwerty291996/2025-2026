n = int(input("n ni kiriting (n > 0): "))
a = float(input("a ni kiriting: "))

yigindi = 0
for i in range(n + 1):
    daraja = a ** i
    yigindi += daraja
    print(f"a^{i} = {daraja}")
print("Yig‘indi:", yigindi)
