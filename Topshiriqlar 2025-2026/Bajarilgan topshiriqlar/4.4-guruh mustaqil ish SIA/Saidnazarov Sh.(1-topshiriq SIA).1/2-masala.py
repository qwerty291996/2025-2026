a = float(input("a haqiqiy sonni kiriting: "))
n = int(input("n butun sonni kiriting: "))
#1-usul
s1=a**n
print(s1)
#2-usul
s2=1
for i in range(1,n+1):
    s2*=a
print(s2)
#3-usul
s3=1
while n >= 1: 
    s3 *= a
    n -= 1
print(s3)
    
