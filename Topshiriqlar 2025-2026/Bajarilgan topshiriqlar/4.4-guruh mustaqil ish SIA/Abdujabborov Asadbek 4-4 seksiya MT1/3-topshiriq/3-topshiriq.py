binary_str = input("Ikkilik sanoq sistemasidagi sonni kiriting: ")

try:
    
    decimal_value = int(binary_str, 2)

    decimal_str = str(decimal_value)
    print("O'nlik sanoq sistemasidagi qiymat:", decimal_str)

except ValueError:
    print("Noto‘g‘ri ikkilik satr kiritildi!")
