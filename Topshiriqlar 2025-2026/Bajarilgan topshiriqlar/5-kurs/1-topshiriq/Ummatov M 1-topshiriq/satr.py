s = input("Satrni kiriting: ")
N = int(input("N ni kiriting (natural son): "))
yangi_satr = ""
for i in range(len(s)):
    yangi_satr += s[i]
    if i != len(s) - 1:  
        yangi_satr += "*" * N
print("Natija:", yangi_satr)
