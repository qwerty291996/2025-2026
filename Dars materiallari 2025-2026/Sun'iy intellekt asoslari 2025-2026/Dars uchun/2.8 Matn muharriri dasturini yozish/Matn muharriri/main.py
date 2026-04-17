# main.py — PyQt5: Sodda matn muharriri (.ui asosida)
# 1- o‘quv savoli: dizayndagi elementlar uchun funksiyalar (File/Edit/Help)
# 2- o‘quv savoli: testlashga tayyor holat (dialoglar, status, Ln/Col)

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox,
    QLabel, QTextEdit, QPlainTextEdit, QAction
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1) .ui dizaynini yuklash (Qt Designer’da chizilgan interfeys)
        uic.loadUi("TextEditor.ui", self)

        # 2) Muhim vidjetlar: matn maydoni va status label (Ln/Col)
        #    Sizning .ui faylingizda QTextEdit nomi: "textEdit"
        self.text_edit = (self.findChild(QTextEdit, "textEdit")
                          or self.findChild(QPlainTextEdit, "textEdit")
                          or self.findChild(QTextEdit, "plainTextEdit")
                          or self.findChild(QPlainTextEdit, "plainTextEdit"))
        self.lbl_lncol: QLabel = self.findChild(QLabel, "lblLnCol")

        # 3) Holat: joriy fayl yo‘li va "o'zgargan/o'zgarmagan" flag
        self.current_path = None
        self.is_modified = False

        # 4) QAction’larni topish (sizdagi .ui da ba’zilarida trailing space bor)
        def A(name: str):
            return self.findChild(QAction, name)

        self.act_new       = A("actionNew ") or A("actionNew")
        self.act_open      = A("actionOpen")
        self.act_save      = A("actionSave ") or A("actionSave")
        self.act_save_as   = A("actionSaveAs")
        self.act_exit      = A("actionExit")

        self.act_undo      = A("actionUndo")
        self.act_redo      = A("actionRedo")
        self.act_cut       = A("actionCut")
        self.act_copy      = A("actionCopy")
        self.act_paste     = A("actionPaste")
        self.act_selectall = A("actionSelectAll")

        self.act_about     = A("actionAbout")

        # 5) QAction → funksiyalarga ulash (File)
        if self.act_new:      self.act_new.triggered.connect(self.new_file)
        if self.act_open:     self.act_open.triggered.connect(self.open_file)
        if self.act_save:     self.act_save.triggered.connect(self.save_file)
        if self.act_save_as:  self.act_save_as.triggered.connect(self.save_file_as)
        if self.act_exit:     self.act_exit.triggered.connect(self.close)

        # 6) QAction → funksiyalarga ulash (Edit)
        if self.act_undo:       self.act_undo.triggered.connect(lambda: self.text_edit and self.text_edit.undo())
        if self.act_redo:       self.act_redo.triggered.connect(lambda: self.text_edit and self.text_edit.redo())
        if self.act_cut:        self.act_cut.triggered.connect(lambda: self.text_edit and self.text_edit.cut())
        if self.act_copy:       self.act_copy.triggered.connect(lambda: self.text_edit and self.text_edit.copy())
        if self.act_paste:      self.act_paste.triggered.connect(lambda: self.text_edit and self.text_edit.paste())
        if self.act_selectall:  self.act_selectall.triggered.connect(lambda: self.text_edit and self.text_edit.selectAll())

        # 7) QAction → funksiyalarga ulash (Help)
        if self.act_about:    self.act_about.triggered.connect(self.show_about)

        # 8) Matn o'zgarsa va kursor joyi o'zgarsa → holatlarni yangilash
        if self.text_edit:
            self.text_edit.textChanged.connect(self.on_text_changed)
            self.text_edit.cursorPositionChanged.connect(self.update_ln_col)

        # 9) Boshlang'ich ko‘rinish
        self.update_window_title()
        self.update_ln_col()

    # ---------- Yordamchi: oyna sarlavhasi ----------
    def update_window_title(self):
        name = self.current_path if self.current_path else "Untitled"
        if self.is_modified:
            name += " *"
        self.setWindowTitle(f"Sodda matn muharriri — {name}")

    # ---------- Yordamchi: Ln/Col indikator ----------
    def update_ln_col(self):
        if not self.text_edit or not self.lbl_lncol:
            return
        c = self.text_edit.textCursor()
        line = c.blockNumber() + 1
        col = c.positionInBlock() + 1
        self.lbl_lncol.setText(f"Ln {line}, Col {col}")

    # ---------- Yordamchi: matn olish/joylash ----------
    def get_text(self):
        return self.text_edit.toPlainText() if self.text_edit else ""

    def set_text(self, text: str):
        if self.text_edit:
            self.text_edit.blockSignals(True)
            self.text_edit.setPlainText(text)
            self.text_edit.blockSignals(False)
            self.is_modified = False
            self.update_window_title()
            self.update_ln_col()

    # ---------- Yordamchi: saqlashdan oldin so‘rash ----------
    def confirm_discard_changes(self) -> bool:
        if self.is_modified:
            reply = QMessageBox.question(
                self, "Saqlansinmi?",
                "Saqlanmagan o'zgarishlar mavjud. Saqlashni xohlaysizmi?",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                return self.save_file()
            elif reply == QMessageBox.Cancel:
                return False
        return True

    # ---------- Matn o‘zgartirilganda ----------
    def on_text_changed(self):
        self.is_modified = True
        self.update_window_title()

    # ===================== FILE MENYUSI =====================
    def new_file(self):
        # Yangi hujjat: saqlanmagan o‘zgarishlar bo‘lsa — so‘raysiz
        if not self.confirm_discard_changes():
            return
        self.current_path = None
        self.set_text("")

    def open_file(self):
        # Fayl ochish: dialog, UTF-8 ustun, bo‘lmasa system default
        if not self.confirm_discard_changes():
            return
        path, _ = QFileDialog.getOpenFileName(
            self, "Open", "", "Text Files (*.txt);;All Files (*.*)"
        )
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(path, "r", encoding=sys.getdefaultencoding(), errors="replace") as f:
                content = f.read()
        self.current_path = path
        self.set_text(content)

    def save_file(self) -> bool:
        # Saqlash: yo‘l bor bo‘lsa shu faylga, bo‘lmasa "Save As"
        if self.current_path is None:
            return self.save_file_as()
        try:
            with open(self.current_path, "w", encoding="utf-8") as f:
                f.write(self.get_text())
            self.is_modified = False
            self.update_window_title()
            self.statusBar().showMessage("Saved", 2000)
            return True
        except Exception as e:
            QMessageBox.critical(self, "Xatolik", f"Saqlashda xatolik:\n{e}")
            return False

    def save_file_as(self) -> bool:
        # "Save As": yangi nom/yo‘l tanlash
        path, _ = QFileDialog.getSaveFileName(
            self, "Save As", "", "Text Files (*.txt);;All Files (*.*)"
        )
        if not path:
            return False
        self.current_path = path
        return self.save_file()

    # ===================== HELP MENYUSI =====================
    def show_about(self):
        QMessageBox.information(
            self, "About",
            "Sodda matn muharriri (PyQt5)\n"
            "Qt Designer’da chizilgan .ui asosida ishlaydi."
        )

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
