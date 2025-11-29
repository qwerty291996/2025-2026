n = input().strip()     # son satr ko'rinishida olinadi
n = int(n)              # butun songa o‘tkazamiz
binary = bin(n)[2:]     # bin() funksiyasi 0b1101 ko‘rinishda beradi, [2:] esa '0b' ni olib tashlaydi
print(binary)
