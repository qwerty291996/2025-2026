def hisobla_yigindi(n):
    S = 0
    for i in range(n, 2*n + 1):
        S += i**2
    return S
n = int(input("n ni kiriting (n > 0): "))

if n > 0:
    natija = hisobla_yigindi(n)
    print(f"Yig'indi S = {natija}")
else:
    print("Iltimos, n > 0 butun son kiriting.")
