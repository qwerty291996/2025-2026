
# 2.1- masala
# a, b = map(int,input().split())
# c, d = map(int,input().split())

# if (a+b)%2!=0 and (c+d)!=0:
#     print("Berilgan maydonlar bir xil rangda")

# else:
#     print("Berilgan maydonlar xar xil rangda")




# 2.2 - masala
# n=int(input())
# s=1
# b=1
# while n>=b:
#     s*=b
#     b+=0.1
# print(s)


# 2.3 - masala
n=input()
n=int(n)
a=""
while n>1:
    b=str(n%2)
    a+=b
    n=n//2
    if n==1:
        a+="1"
    elif n==0:
        a+="0"
print(a[::-1])