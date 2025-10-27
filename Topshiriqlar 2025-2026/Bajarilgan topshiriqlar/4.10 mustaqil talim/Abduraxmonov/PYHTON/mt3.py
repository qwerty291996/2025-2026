binary_str = input("Ikkilik sonni kiriting: ")
if all(ch in '01' for ch in binary_str) and len(binary_str) > 0:
    decimal_value = int(binary_str, 2)
    print(f"O‘nlik sanoq sistemasidagi qiymat: {decimal_value}")
else:
    print("Xatolik: faqat 0 va 1 lardan iborat ikkilik son kiriting!")
