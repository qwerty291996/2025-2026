import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class ParolGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Qt Designer'da yasalgan UIning yuklanishi
        uic.loadUi("generator.ui", self)
        
        # 2. "Yaratish" tugmasini funksiyaga bog'lash
        self.btn_generate.clicked.connect(self.parol_yaratish)

    def parol_yaratish(self):
        # 1. QSpinBox maydonidan foydalanuvchi tanlagan raqamni olish
        uzunlik = self.input_length.value()
        
        # 2. Parol uchun kerakli barcha belgilarni bitta qutiga yig'ish
        harflar = string.ascii_letters # Barcha katta va kichik ingliz harflari
        raqamlar = string.digits       # 0 dan 9 gacha bo'lgan raqamlar
        maxsus = "!@#$%^&*"            # Maxsus belgilar to'plami
        
        umumiy_baza = harflar + raqamlar + maxsus
        
        # 3. Kiritilgan uzunlik miqdoricha tasodifiy belgini tanlab olish
        yangi_parol = "".join(random.choice(umumiy_baza) for _ in range(uzunlik))
        
        # 4. Tayyor parolni faqat o'qish uchun mo'ljallangan maydonga yozish
        self.output_pass.setText(yangi_parol)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ParolGenerator()
    oyna.show()
    sys.exit(app.exec_())