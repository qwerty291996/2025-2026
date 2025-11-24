print("Avval n soni keyin a kiritiladi!!!")
n = int(input())
a = float(input())
yigindi = 0
for i in range(1, n+1):
    daraja = a ** i
    print(f"{a}^{i} = ",daraja)
    yigindi += daraja

print(f"\nDarajalarning yig'indisi: {yigindi}")
