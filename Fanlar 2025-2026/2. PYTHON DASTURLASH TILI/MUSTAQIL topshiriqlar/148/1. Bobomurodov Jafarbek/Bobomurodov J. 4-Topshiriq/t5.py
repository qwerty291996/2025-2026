from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("t.ui", self)
        self.pushButton.clicked.connect(self.Chizish)
    def Chizish(self):
        

            x1 = int(self.lineEdit.text())
            
            x1=x1%86400
            self.label_2.setText(f"{x1//3600}:{(x1%3600)//60}:{(x1%3600)%60}")


app = QApplication([])
win = MainWindow()
win.show()
app.exec()