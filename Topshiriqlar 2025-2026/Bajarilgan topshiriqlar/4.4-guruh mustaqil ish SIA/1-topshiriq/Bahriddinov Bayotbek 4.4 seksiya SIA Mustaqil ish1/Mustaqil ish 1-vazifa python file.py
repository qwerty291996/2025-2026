def ruh_yurishi(x1, y1, x2, y2):
    # Koordinatalar 1 dan 8 gacha bo'lishini tekshiramiz
    if not (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8):
        return False

    # Ruh bir yurishda diagonallar bo'ylab harakat qiladi
    if abs(x2 - x1) == abs(y2 - y1):
        return True
    else:
        return False

# Misol uchun:
print(ruh_yurishi(1, 1, 3, 3))  # True (ruh 1,1 dan 3,3 ga yuradi)
print(ruh_yurishi(4, 4, 5, 6))  # False (ruh bunday yurishni amalga oshirolmaydi)
