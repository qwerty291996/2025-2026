with open("data.txt", 'r') as file:
    d = list(map(int, file.read().split(',')))
f = r'dataa.txt'
fayl = open(f, 'w')

if (len(d) % 2 == 0):
    for i in range(int((len(d) // 2))):
        fayl.write(str(d[i]))
        fayl.write(str(d[len(d) - 1 - i]))
else:
    for i in range(int((len(d) // 2))):
        fayl.write(str(d[i]))
        fayl.write(str(d[len(d) - 1 - i]))

    fayl.write(str(d[(len(d)) // 2]))
fayl.close()
