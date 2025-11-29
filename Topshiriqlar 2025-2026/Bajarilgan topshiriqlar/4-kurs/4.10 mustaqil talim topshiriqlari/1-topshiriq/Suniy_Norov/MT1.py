# 1-misol
x1, y1, x2, y2 = map(int, input().split())
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("Rost") 
else:
    print("Yolg'on")

# 2-misol
n = int(input("n= "))
a = float(input("a= "))

for i in range(1, n + 1):
    print(f"{a} ni {i}-darajasi: "+ pow(a,i))

# 3-misol
s = input("Satr: ")
yangi_satr = ' '.join(s)

print(yangi_satr)
