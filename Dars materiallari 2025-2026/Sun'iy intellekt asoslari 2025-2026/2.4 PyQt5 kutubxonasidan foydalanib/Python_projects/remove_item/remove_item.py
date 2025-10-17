import sys
from PyQt5 import QtWidgets, uic


class ListApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("remove_item.ui", self)

        # Ro'yxatni boshlang'ich qiymat bilan to'ldiramiz
        self.items = ["Olma", "Banan", "Apelsin"]

        # Ro'yxatni boshlang'ich holatda ko'rsatamiz
        self.lblList.setText(f"Ro‘yxat: {', '.join(self.items)}")

        # Tugma bosilishi bilan o'chirish amali
        self.btnRemove.clicked.connect(self.remove_item)

    def remove_item(self):
        item_to_remove = self.lineItem.text().strip()  # Foydalanuvchidan matn olish
        if item_to_remove in self.items:
            self.items.remove(item_to_remove)  # Ro'yxatdan o'chirish
            self.lblList.setText(f"Ro‘yxat: {', '.join(self.items)}")  # Ro'yxatni yangilash
        else:
            self.lblList.setText("Xato: Bunday element ro'yxatda yo'q!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = ListApp()
    win.setWindowTitle("Ro‘yxatdan element o‘chirish")
    win.show()
    sys.exit(app.exec_())
