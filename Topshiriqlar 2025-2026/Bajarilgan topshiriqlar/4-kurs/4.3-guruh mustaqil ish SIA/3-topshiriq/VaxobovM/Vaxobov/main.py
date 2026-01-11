import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QListWidget, QTextEdit, QLineEdit,
    QHBoxLayout, QVBoxLayout, QMenuBar, QAction, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt


class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eslatmalar dasturi (PyQt5)")

        self.notes_file = "notes.json"
        self.notes = {}  # {title: text}

        self.initUI()
        self.load_notes()

    # ---------------- UI YARATISH ----------------
    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Qidiruv oynasi
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Qidirish...")
        self.search_bar.textChanged.connect(self.search_notes)

        # Chap panel: eslatmalar ro‘yxati
        self.list_widget = QListWidget()
        self.list_widget.currentItemChanged.connect(self.load_selected_note)

        # O‘ng panel: matn oynasi
        self.text_edit = QTextEdit()
        self.text_edit.textChanged.connect(self.auto_save)

        # Panellarni joylashtirish
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.search_bar)
        left_layout.addWidget(self.list_widget)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout, 30)
        main_layout.addWidget(self.text_edit, 70)

        main_widget.setLayout(main_layout)

        # Menyu
        menu = QMenuBar()
        file_menu = menu.addMenu("File")
        edit_menu = menu.addMenu("Edit")

        # File → Import/Export
        import_action = QAction("Import", self)
        import_action.triggered.connect(self.import_notes)
        file_menu.addAction(import_action)

        export_action = QAction("Export", self)
        export_action.triggered.connect(self.export_notes)
        file_menu.addAction(export_action)

        # Edit → New, Delete
        new_action = QAction("New Note", self)
        new_action.triggered.connect(self.new_note)
        edit_menu.addAction(new_action)

        delete_action = QAction("Delete Note", self)
        delete_action.triggered.connect(self.delete_note)
        edit_menu.addAction(delete_action)

        self.setMenuBar(menu)

    # ---------------- FUNKSIYALAR ----------------

    def load_notes(self):
        """JSON-dan eslatmalarni yuklash"""
        if os.path.exists(self.notes_file):
            try:
                with open(self.notes_file, "r", encoding="utf-8") as f:
                    self.notes = json.load(f)
            except:
                self.notes = {}

        self.update_list()

    def save_notes(self):
        """JSON-ga saqlash"""
        with open(self.notes_file, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def update_list(self):
        """Ro‘yxatni yangilash"""
        self.list_widget.clear()
        for title in self.notes.keys():
            self.list_widget.addItem(title)

    def new_note(self):
        """Yangi eslatma yaratish"""
        title = f"Yangi eslatma {len(self.notes)+1}"
        self.notes[title] = ""
        self.update_list()
        items = self.list_widget.findItems(title, Qt.MatchExactly)
        if items:
            self.list_widget.setCurrentItem(items[0])
        self.save_notes()

    def delete_note(self):
        """Eslatmani o‘chirish"""
        current = self.list_widget.currentItem()
        if not current:
            return

        title = current.text()
        confirm = QMessageBox.question(self, "Tasdiqlash", f"'{title}' o‘chirilsinmi?")
        if confirm == QMessageBox.Yes:
            del self.notes[title]
            self.update_list()
            self.text_edit.clear()
            self.save_notes()

    def load_selected_note(self):
        """Tanlangan eslatma matnini yuklash"""
        item = self.list_widget.currentItem()
        if item:
            title = item.text()
            self.text_edit.blockSignals(True)
            self.text_edit.setText(self.notes.get(title, ""))
            self.text_edit.blockSignals(False)

    def auto_save(self):
        """Matn o‘zgarganda avtomatik saqlash"""
        item = self.list_widget.currentItem()
        if item:
            title = item.text()
            self.notes[title] = self.text_edit.toPlainText()
            self.save_notes()

    def search_notes(self):
        """Sarlavha va matn bo‘yicha qidiruv"""
        query = self.search_bar.text().lower()
        self.list_widget.clear()

        for title, text in self.notes.items():
            if query in title.lower() or query in text.lower():
                self.list_widget.addItem(title)

    # -------------- IMPORT / EXPORT ----------------

    def export_notes(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Notes", "", "JSON Files (*.json)")
        if not file_path:
            return
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.notes, f, ensure_ascii=False, indent=2)

    def import_notes(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Import Notes", "", "JSON Files (*.json)")
        if not file_path:
            return
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                imported = json.load(f)
                self.notes.update(imported)
                self.save_notes()
                self.update_list()
        except:
            QMessageBox.warning(self, "Xatolik", "Fayl noto‘g‘ri formatda!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotesApp()
    window.resize(900, 500)
    window.show()
    sys.exit(app.exec_())
