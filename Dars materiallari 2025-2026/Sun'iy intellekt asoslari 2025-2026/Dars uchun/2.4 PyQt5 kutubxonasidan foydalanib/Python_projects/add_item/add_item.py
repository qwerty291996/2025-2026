import sys
from PyQt5 import QtWidgets, uic


class ListApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("add_item.ui", self)

        self.items = []  # Ro'yxatni saqlash uchun o'zgaruvchi

        self.btnAdd.clicked.connect(self.add_item)

    def add_item(self):
        new_item = self.lineItem.text().strip()  # Foydalanuvchidan matn olish
        if new_item:
            self.items.append(new_item)  # Ro'yxatga qo'shish
            self.lblList.setText(f"Ro‘yxat: {', '.join(self.items)}")  # Ro'yxatni yangilash
        else:
            self.lblList.setText("Xato: Bo'sh element qo'shish mumkin emas!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = ListApp()
    win.setWindowTitle("Ro‘yxatga element qo‘shish")
    win.show()
    sys.exit(app.exec_())
