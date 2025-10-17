import sys
from PyQt5 import QtWidgets, uic

def to_float(s):
    s = (s or "").strip().replace(",", ".")
    return float(s)

class SimpleCalc(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("simple_calc.ui", self)

        self.btnPlus.clicked.connect(lambda: self.calc("add"))
        self.btnMinus.clicked.connect(lambda: self.calc("sub"))
        self.btnMul.clicked.connect(lambda: self.calc("mul"))
        self.btnDiv.clicked.connect(lambda: self.calc("div"))

    def calc(self, op):
        try:
            a = to_float(self.lineA.text())
            b = to_float(self.lineB.text())

            if op == "add":
                res = a + b
            elif op == "sub":
                res = a - b
            elif op == "mul":
                res = a * b
            elif op == "div":
                if b == 0:
                    self.lblResult.setText("Natija: nolga bo‘lish mumkin emas!")
                    return
                res = a / b
            else:
                res = "Noma’lum amal"

            self.lblResult.setText(f"Natija: {res}")
        except ValueError:
            self.lblResult.setText("Natija: xato kiritish!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = SimpleCalc()
    win.setWindowTitle("Oddiy 4-amal kalkulyatori")
    win.show()
    sys.exit(app.exec_())
