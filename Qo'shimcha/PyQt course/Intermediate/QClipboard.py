import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from PyQt5.QtCore import QSize
import warnings

# Ogohlantirishlarni o'chirish
warnings.filterwarnings("ignore")

class ClipboardDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Oyna sozlamalari
        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("Clipboard Ilovasi Demo")
        
        # Matn maydonini yaratish
        self.text_area = QPlainTextEdit(self)
        self.text_area.setPlainText("Sichqonchaning o'ng tugmasi orqali tahrirlashingiz mumkin.")
        self.text_area.move(10, 10)
        self.text_area.resize(400, 200)
        
        # Clipboard (bufer) xizmatiga ulanish
        # Agar clipboarddagi ma'lumot o'zgarsa, 'text_changed' funksiyasi ishlaydi
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.text_changed)

    def text_changed(self):
        # Clipboarddagi yangi matnni olish
        new_text = self.clipboard.text()
        
        # Terminalga chiqarish
        print(f"Clipboard o'zgardi: {new_text}")
        
        # Dastur ichidagi matn maydoniga joylashtirish
        self.text_area.insertPlainText(f"\n[Nusxa olindi]: {new_text}")

# Dasturni ishga tushirish qismi
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ClipboardDemo()
    demo.show()
    sys.exit(app.exec_())