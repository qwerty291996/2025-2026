"""
n butun soni berilgan (n>0). Bir sikldan foydalangan holda quyidagi 
yig'indini hisoblovchi programma tuzilsin.
1-a+a²-a³+...(-1)ⁿ
"""

a = int(input())
n = int(input())

s = 0

for i in range(n + 1): 
    s += ((-1)**i)*(a**i)

print("Yig'indi:", s)
