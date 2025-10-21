import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("color_menu.ui", self)  # Qt Designer faylini yuklash

        # --- Menu bandlarini bog‘lash
        self.actionRed.triggered.connect(lambda: self.change_color("red"))
        self.actionBlue.triggered.connect(lambda: self.change_color("lightblue"))
        self.actionReset.triggered.connect(self.reset_view)
        self.actionAbout.triggered.connect(self.show_about)

        # Boshlang‘ich holat
        self.labelInfo.setText("Menyudan rang tanlang 🎨")
        self.statusBar().showMessage("Tayyor")

    # --- Funksiyalar
    def change_color(self, color):
        self.labelInfo.setStyleSheet(f"background-color: {color}; font-size: 16px;")
        self.statusBar().showMessage(f"Fon rangi: {color}")

    def reset_view(self):
        self.labelInfo.setStyleSheet("background-color: none; font-size: 16px;")
        self.labelInfo.setText("Menyudan rang tanlang 🎨")
        self.statusBar().showMessage("Tiklandi (Reset)")

    def show_about(self):
        QMessageBox.information(
            self,
            "About",
            "Bu oddiy PyQt menyu dasturi.\nMenyudan fon rangini tanlashingiz mumkin."
        )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("Rangli Menyu — PyQt misoli")
    w.resize(400, 250)
    w.show()
    sys.exit(app.exec_())
