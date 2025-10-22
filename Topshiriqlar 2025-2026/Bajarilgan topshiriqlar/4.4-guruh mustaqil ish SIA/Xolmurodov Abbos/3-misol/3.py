satr = input("Satrni kiriting: ")
N = int(input("N ni kiriting: "))

natija = ""
for i in range(len(satr)):
    natija += satr[i]
    if (i + 1) % N == 0:
        natija += "*"

print("Natija:", natija)
