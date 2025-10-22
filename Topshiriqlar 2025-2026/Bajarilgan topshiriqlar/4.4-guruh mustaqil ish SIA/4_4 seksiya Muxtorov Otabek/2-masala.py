n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    formula = 2 * i - 1
    s += formula
    print(s)
