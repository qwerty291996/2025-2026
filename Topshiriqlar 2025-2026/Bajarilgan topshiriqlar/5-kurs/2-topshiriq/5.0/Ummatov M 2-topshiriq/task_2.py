ism = ['Laziz', 'Faxriddin', 'Beksulton', 'Abdulloh']
baho = [78, 91, 80, 95]

talabalar = list(zip(ism, baho))

ortacha = sum(baho) / len(baho)

print(f"O'rtacha baho: {ortacha:.2f}\n")

yuqori_baholar = [(i, b) for i, b in talabalar if b > ortacha]

print("O'rtacha bahodan yuqori bahoga ega talabalar:")
for i, b in yuqori_baholar:
    print(f"{i} — {b} ball")
