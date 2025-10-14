# Kirish
n = int(input("Archa balandligi n ni kiriting: "))   # masalan: 5
t = int(input("Tana balandligi t ni kiriting: "))     # masalan: 2
 
# Archaning (barg) qismi
for i in range(1, n + 1):
    yulduzlar = 2 * i - 1
    bosh_joy = n - i
    print(" " * bosh_joy + "*" * yulduzlar)
 
# Tana (poya) qismi: markazlangan, eni 1 ta '*'
for _ in range(t):
    print(" " * (n - 1) + "*")


