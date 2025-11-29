x, y = map(int, input().split())
if (x + y) % 2 == 1:
    print("Maydon oq") 
else:
    print("Maydon qora")


n = int(input("n ni kiriting: "))
S = 0
for i in range(n, 2*n + 1):
    S += i**2
print("Yig'indi S =", S)


binary_str = input("Ikkilik sanoq sistemasidagi sonni kiriting: ")
decimal_value = int(binary_str, 2)
print(str(decimal_value))




