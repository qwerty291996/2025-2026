n = int(input().strip())
S = 1.0
for i in range(1, n + 1):
    S *= (1 + 0.1 * i)
print(round(S, 6))  # Natijani 6 xonagacha aniqlik bilan chiqaramiz
