import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)  # .ui faylni yuklaymiz

        # Menu action’larini ulash (Designer’dagi objectName’lar bilan)
        self.actionSayHello.triggered.connect(self.say_hello)
        self.actionClear.triggered.connect(self.clear_text)
        self.actionExit.triggered.connect(self.close)           # tayyor slot
        self.actionAbout.triggered.connect(self.show_about)

        # Dastlabki holat
        self.labelMsg.setText("Menyudan biror amalni tanlang 🙂")
        self.statusBar().showMessage("Tayyor")

    # --- Slotlar (funksiyalar)
    def say_hello(self):
        self.labelMsg.setText("Salom, Menyu!")
        self.statusBar().showMessage("Hello bosildi")

    def clear_text(self):
        self.labelMsg.clear()
        self.statusBar().showMessage("Matn tozalandi")

    def show_about(self):
        QMessageBox.information(
            self,
            "About",
            "Eng oddiy menyu misoli: File → Say Hello / Clear / Exit, Help → About"
        )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("Oddiy Menyu — PyQt misoli")
    w.resize(420, 260)
    w.show()
    sys.exit(app.exec_())
