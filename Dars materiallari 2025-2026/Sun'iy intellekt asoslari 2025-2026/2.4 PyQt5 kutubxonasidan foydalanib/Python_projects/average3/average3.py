import sys
from PyQt5 import QtWidgets, uic

def to_float(s):
    s = (s or "").strip().replace(",", ".")
    return float(s)

class Average3(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("average3.ui", self)
        self.btnAvg.clicked.connect(self.calc_avg)

    def calc_avg(self):
        try:
            a = to_float(self.lineA.text())
            b = to_float(self.lineB.text())
            c = to_float(self.lineC.text())
            avg = (a + b + c) / 3
            self.lblResult.setText(f"Natija: {avg}")
        except ValueError:
            self.lblResult.setText("Natija: xato kiritish!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Average3()
    win.setWindowTitle("3 ta son o‘rtachasi")
    win.show()
    sys.exit(app.exec_())
