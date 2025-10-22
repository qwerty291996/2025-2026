"""
Satr berilgan. Satrdagi raqamlar sonini aniqlovchi programma tuzilsin.
"""
str = input()

numbers = 0

for i in str:
    if i.isdigit():
        numbers += 1

print("Satrdagi raqamlar soni:", numbers)
