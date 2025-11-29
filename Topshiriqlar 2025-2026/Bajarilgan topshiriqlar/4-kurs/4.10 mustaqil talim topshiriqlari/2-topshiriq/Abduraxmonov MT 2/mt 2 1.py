n = int(input("Necha ta son kiritasiz? n = "))
royxat = []
for i in range(n):
    son = int(input(f"{i+1}-sonni kiriting: "))
    royxat.append(son)
print("Kiritilgan ro'yxat:", royxat)
print("Eng katta element:", max(royxat))
print("Eng kichik element:", min(royxat))
