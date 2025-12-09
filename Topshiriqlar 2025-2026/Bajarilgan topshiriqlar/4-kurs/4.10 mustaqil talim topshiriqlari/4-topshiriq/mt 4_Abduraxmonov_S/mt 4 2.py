# input.txt faylini o‘qish rejimida ochamiz
with open("input.txt", "r", encoding="utf-8") as file:
    # 1-qatorni o‘qib, integerga aylantirish
    first_line = int(file.readline().strip())

    # Qolgan qatorlarni o‘qish
    remaining_lines = file.readlines()

# Natijalarni chiqarish
print("Birinchi qator (int):", first_line)
print("Qolgan qatorlar:")
for line in remaining_lines:
    print(line.strip())
