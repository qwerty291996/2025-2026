import os
def mutlaq_yolni_ol(fayl_nomi):
    mutlaq_yol = os.path.abspath(fayl_nomi)
    return mutlaq_yol
fayl = input("Mutlaq yo'lini bilmoqchi bo'lgan fayl nomini kiriting: ")
natija = mutlaq_yolni_ol(fayl)
print("\nFaylning mutlaq yo'li:")
print(natija)
