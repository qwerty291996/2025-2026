import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class ShifratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. UI faylni yuklash
        uic.loadUi("shifrator.ui", self)
        
        # 2. Tugma bosilganda shifrlash funksiyasini chaqirish
        self.btn_encrypt.clicked.connect(self.shifrlash)

    def shifrlash(self):
        # Kiritish maydonidan matnni olish
        asl_matn = self.input_text.text()
        shifrlangan_matn = ""
        qadam = 4

        # Sezar algoritmi
        for harf in asl_matn:
            if harf.isalpha():  # Faqat harflarni tekshirish
                # Harf katta yoki kichikligiga qarab ASCII boshlang'ich nuqtasini belgilash
                bosh_nuqta = ord('A') if harf.isupper() else ord('a')
                
                # Yangi harfni hisoblash (26 harflik sikl ichida aylantirish)
                yangi_kod = (ord(harf) - bosh_nuqta + qadam) % 26 + bosh_nuqta
                shifrlangan_matn += chr(yangi_kod)
            else:
                # Probel, raqam va tinish belgilarini o'zgarishsiz qoldirish
                shifrlangan_matn += harf

        # Natijani chiqarish maydoniga yozish
        self.output_text.setText(shifrlangan_matn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ShifratorApp()
    oyna.show()
    sys.exit(app.exec_())