n = int(input("n ni kiriting))
S = 0
for i in range(1, n + 1):
    S += 2 * i - 1
    print(f"{i}^2 = {S}")