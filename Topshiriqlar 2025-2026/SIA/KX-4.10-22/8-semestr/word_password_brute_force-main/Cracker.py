import sys
import os
import msoffcrypto
import io
import time
import itertools
from concurrent.futures import ProcessPoolExecutor, as_completed
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QFileDialog, QLabel, QProgressBar, QTextEdit, QMessageBox, QGroupBox,
    QRadioButton, QButtonGroup, QDialog, QPlainTextEdit
)
from PyQt5.QtCore import QThread, pyqtSignal

NUMBERS_TXT_PATH = r"numbers.txt"
CUSTOM_TXT_PATH = "shaxsiy_parollar.txt"


# --- MULTIPROCESSING FUNKSIYASI ---
def check_password_chunk(file_data, password_list):
    office_file = msoffcrypto.OfficeFile(io.BytesIO(file_data))
    for pwd in password_list:
        try:
            office_file.load_key(password=pwd, verify_password=True)
            return pwd
        except Exception:
            continue
    return None


class CustomDictDialog(QDialog):
    """Shaxsiy parollarni kiritish uchun yordamchi oyna"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("📝 Shaxsiy parollarni yozish")
        self.setFixedSize(400, 450)
        self.setStyleSheet("""
            QDialog { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI'; }
            QPlainTextEdit { background-color: #313244; border: 1px solid #45475a; border-radius: 6px; color: #a6adc8; font-family: 'Consolas'; font-size: 14px; padding: 5px;}
            QPushButton { background-color: #a6e3a1; color: #1e1e2e; border-radius: 6px; padding: 10px; font-weight: bold; font-size: 14px;}
            QPushButton:hover { background-color: #89dceb; }
            QLabel { color: #f38ba8; font-weight: bold; font-size: 13px; margin-bottom: 5px;}
        """)

        layout = QVBoxLayout(self)
        self.info_label = QLabel("💡 Har bir parolni alohida, yangi qatordan yozing:")
        layout.addWidget(self.info_label)

        self.editor = QPlainTextEdit(self)

        # --- NAMUNA QO'SHILDI (Placeholder) ---
        self.editor.setPlaceholderText(
            "Namuna:\n\n"
            "123456\n"
            "admin123\n"
            "mening_parolim\n"
            "qizil_olma2024\n\n"
            "(Eslatma: Vergul yoki bo'sh joy qo'ymang. Har bir paroldan so'ng 'Enter' tugmasini bosing!)"
        )
        layout.addWidget(self.editor)

        # Agar oldin yozilgan bo'lsa, uni ekranga chiqaramiz
        if os.path.exists(CUSTOM_TXT_PATH):
            with open(CUSTOM_TXT_PATH, "r", encoding="utf-8") as f:
                self.editor.setPlainText(f.read())

        self.btn_save = QPushButton("💾 Saqlash va Yopish")
        self.btn_save.clicked.connect(self.save_passwords)
        layout.addWidget(self.btn_save)

    def save_passwords(self):
        text = self.editor.toPlainText().strip()
        if not text:
            QMessageBox.warning(self, "Diqqat", "Hech qanday parol kiritmadingiz!")
            return

        with open(CUSTOM_TXT_PATH, "w", encoding="utf-8") as f:
            f.write(text)
        self.accept()


class PasswordCheckThread(QThread):
    progress_signal = pyqtSignal(str)
    progress_value_signal = pyqtSignal(int)
    result_signal = pyqtSignal(str, str)
    finished_signal = pyqtSignal(bool)

    def __init__(self, file_path: str, dict_path: str):
        super().__init__()
        self.file_path = file_path
        self.dict_path = dict_path
        self.is_running = True

    def count_lines_fast(self):
        self.progress_signal.emit("⏳ Lug'at hajmi hisoblanmoqda...")
        try:
            with open(self.dict_path, 'rb') as f:
                return sum(1 for _ in f)
        except Exception:
            return 0

    def run(self):
        start_time = time.time()

        # Parollar sonini sanash
        total_passwords = self.count_lines_fast()
        if total_passwords == 0:
            self.progress_signal.emit("❌ Lug'at bo'sh yoki topilmadi!")
            self.finished_signal.emit(False)
            return

        self.progress_signal.emit(f"📋 Jami o'qilgan parollar soni: {total_passwords:,} ta")

        try:
            with open(self.file_path, "rb") as f:
                file_data = f.read()

            num_cores = os.cpu_count() or 4
            self.progress_signal.emit(f"🚀 Multiprocessing ishga tushdi ({num_cores} yadro)...")

            chunk_size = 5000
            found_password = None
            processed_count = 0

            # Fayldan qismlab (chunk) o'qish generatori
            def generate_chunks():
                with open(self.dict_path, "r", encoding="utf-8", errors="ignore") as pf:
                    while True:
                        lines = list(itertools.islice(pf, chunk_size))
                        if not lines: break
                        yield [line.strip() for line in lines if line.strip()]

            with ProcessPoolExecutor(max_workers=num_cores) as executor:
                futures = {executor.submit(check_password_chunk, file_data, chunk): chunk for chunk in
                           generate_chunks()}

                for future in as_completed(futures):
                    if not self.is_running:
                        executor.shutdown(wait=False, cancel_futures=True)
                        break

                    result = future.result()
                    processed_count += len(futures[future])

                    percent = int((processed_count / total_passwords) * 100)
                    self.progress_value_signal.emit(percent)

                    if processed_count % (chunk_size * num_cores) == 0 or processed_count == total_passwords:
                        self.progress_signal.emit(f"🔎 {processed_count:,} / {total_passwords:,} ta tekshirildi...")

                    if result:
                        found_password = result
                        self.is_running = False
                        executor.shutdown(wait=False, cancel_futures=True)
                        break

            if found_password:
                elapsed = time.time() - start_time
                self.result_signal.emit(found_password, self.format_time(elapsed))
                self.finished_signal.emit(True)
            else:
                self.progress_signal.emit("📭 Ushbu lug'atdan parol topilmadi.")
                self.progress_value_signal.emit(100)
                self.finished_signal.emit(False)

        except Exception as e:
            self.progress_signal.emit(f"❌ Xato yuz berdi: {str(e)}")
            self.finished_signal.emit(False)

    def format_time(self, seconds):
        if seconds < 60: return f"{seconds:.2f} soniya"
        minutes, rem_seconds = int(seconds // 60), int(seconds % 60)
        hours, minutes = int(minutes // 60), minutes % 60
        if hours > 0: return f"{hours} soat, {minutes} daqiqa, {rem_seconds} soniya"
        return f"{minutes} daqiqa, {rem_seconds} soniya"

    def stop(self):
        self.is_running = False
        self.progress_signal.emit("🛑 Jarayon foydalanuvchi tomonidan to'xtatildi.")


class ModernChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = ""
        self.dict_path = NUMBERS_TXT_PATH
        self.thread = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DOCX Password Recovery [PRO]")
        self.setFixedSize(650, 700)
        self.setStyleSheet("""
            QWidget { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI', sans-serif; }
            QPushButton { background-color: #89b4fa; color: #1e1e2e; border-radius: 6px; padding: 10px; font-weight: bold; font-size: 13px;}
            QPushButton:hover { background-color: #b4befe; }
            QPushButton:disabled { background-color: #45475a; color: #7f849c; }
            QTextEdit { background-color: #313244; border: 1px solid #45475a; border-radius: 6px; color: #a6adc8; font-family: 'Consolas'; font-size: 13px;}
            QProgressBar { border: 1px solid #45475a; border-radius: 6px; text-align: center; color: white; background: #313244; font-weight: bold;}
            QProgressBar::chunk { background-color: #a6e3a1; border-radius: 5px;}
            QGroupBox { font-weight: bold; border: 1px solid #45475a; border-radius: 8px; margin-top: 15px; padding-top: 15px; font-size: 14px;}
            QLabel { font-size: 13px; }
            QRadioButton { font-size: 13px; font-weight: bold; padding: 5px; }
            QRadioButton::indicator { width: 16px; height: 16px; border-radius: 8px; border: 2px solid #89b4fa; }
            QRadioButton::indicator:checked { background-color: #a6e3a1; border: 2px solid #a6e3a1; }
        """)

        layout = QVBoxLayout()

        # 1. Faylni tanlash bloki
        file_group = QGroupBox("1. Qulflangan faylni tanlang")
        file_layout = QVBoxLayout()
        self.file_label = QLabel("Fayl tanlanmagan")
        self.file_label.setStyleSheet("color: #f38ba8; font-weight: bold;")
        self.btn_select_file = QPushButton("📁 DOCX Faylni Tanlash")
        self.btn_select_file.clicked.connect(self.select_docx_file)
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.btn_select_file)
        file_group.setLayout(file_layout)
        layout.addWidget(file_group)

        # 2. Hujum usuli bloki
        mode_group = QGroupBox("2. Hujum lug'atini tanlang")
        mode_layout = QVBoxLayout()

        self.radio_6digits = QRadioButton("🔢 6 xonali sonlar (numbers.txt orqali)")
        self.radio_custom = QRadioButton("📝 Shaxsiy ro'yxatni kiritish (Dastur ichida)")
        self.radio_rockyou = QRadioButton("💀 Rockyou.txt lug'ati (Fayl tanlash)")
        self.radio_6digits.setChecked(True)

        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.radio_6digits)
        self.btn_group.addButton(self.radio_custom)
        self.btn_group.addButton(self.radio_rockyou)

        self.radio_6digits.toggled.connect(self.toggle_dict_btn)
        self.radio_custom.toggled.connect(self.toggle_dict_btn)
        self.radio_rockyou.toggled.connect(self.toggle_dict_btn)

        self.dict_label = QLabel(f"Manzil: {NUMBERS_TXT_PATH}")
        self.dict_label.setStyleSheet("color: #a6adc8;")

        self.btn_action_dict = QPushButton("Fayl bilan ishlash")
        self.btn_action_dict.setEnabled(False)
        self.btn_action_dict.clicked.connect(self.handle_dict_action)

        mode_layout.addWidget(self.radio_6digits)
        mode_layout.addWidget(self.radio_custom)
        mode_layout.addWidget(self.radio_rockyou)
        mode_layout.addWidget(self.dict_label)
        mode_layout.addWidget(self.btn_action_dict)
        mode_group.setLayout(mode_layout)
        layout.addWidget(mode_group)

        # 3. Log va Progress bloki
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        self.pbar = QProgressBar()
        self.pbar.setValue(0)
        layout.addWidget(self.pbar)

        btn_layout = QHBoxLayout()
        self.btn_start = QPushButton("🚀 Boshlash")
        self.btn_start.setEnabled(False)
        self.btn_start.setStyleSheet("background-color: #a6e3a1; color: #1e1e2e;")
        self.btn_start.clicked.connect(self.start_check)

        self.btn_stop = QPushButton("🛑 To'xtatish")
        self.btn_stop.setEnabled(False)
        self.btn_stop.setStyleSheet("background-color: #f38ba8; color: #1e1e2e;")
        self.btn_stop.clicked.connect(self.stop_check)

        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def select_docx_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Word fayl", "", "Word Files (*.docx)")
        if path:
            self.file_path = path
            self.file_label.setText(f"📄 Fayl: {os.path.basename(path)}")
            self.file_label.setStyleSheet("color: #a6e3a1; font-weight: bold;")
            self.check_ready_to_start()

    def handle_dict_action(self):
        if self.radio_custom.isChecked():
            dialog = CustomDictDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                self.dict_path = CUSTOM_TXT_PATH
                self.dict_label.setText(f"Manzil: {CUSTOM_TXT_PATH} (Saqlandi)")
                self.dict_label.setStyleSheet("color: #a6e3a1; font-weight: bold;")
        elif self.radio_rockyou.isChecked():
            path, _ = QFileDialog.getOpenFileName(self, "Lug'at fayli", "", "Text Files (*.txt)")
            if path:
                self.dict_path = path
                self.dict_label.setText(f"Manzil: {os.path.basename(path)}")
                self.dict_label.setStyleSheet("color: #a6e3a1; font-weight: bold;")

        self.check_ready_to_start()

    def toggle_dict_btn(self):
        if self.radio_6digits.isChecked():
            self.dict_path = NUMBERS_TXT_PATH
            self.btn_action_dict.setEnabled(False)
            self.btn_action_dict.setText("Harakat talab etilmaydi")
            self.dict_label.setText(f"Manzil: {NUMBERS_TXT_PATH}")
            self.dict_label.setStyleSheet("color: #a6adc8;")
        elif self.radio_custom.isChecked():
            self.dict_path = CUSTOM_TXT_PATH if os.path.exists(CUSTOM_TXT_PATH) else ""
            self.btn_action_dict.setEnabled(True)
            self.btn_action_dict.setText("📝 Parollarni dasturda yozish")
            if not self.dict_path:
                self.dict_label.setText("Lug'at: Hali parollar yozilmagan")
                self.dict_label.setStyleSheet("color: #f38ba8;")
            else:
                self.dict_label.setText(f"Manzil: {CUSTOM_TXT_PATH} (Tayyor)")
                self.dict_label.setStyleSheet("color: #a6e3a1;")
        elif self.radio_rockyou.isChecked():
            self.dict_path = ""
            self.btn_action_dict.setEnabled(True)
            self.btn_action_dict.setText("📖 Lug'at faylini tanlash")
            self.dict_label.setText("Lug'at: Tanlanmagan")
            self.dict_label.setStyleSheet("color: #f38ba8;")

        self.check_ready_to_start()

    def check_ready_to_start(self):
        file_ok = bool(self.file_path)
        dict_ok = bool(self.dict_path)
        self.btn_start.setEnabled(file_ok and dict_ok)

    def start_check(self):
        if not os.path.exists(self.dict_path):
            QMessageBox.critical(self, "Xato", f"Belgilangan lug'at fayli topilmadi!\nManzil: {self.dict_path}")
            return

        self.log_area.clear()
        self.pbar.setValue(0)
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)
        self.btn_select_file.setEnabled(False)
        self.btn_action_dict.setEnabled(False)

        self.thread = PasswordCheckThread(self.file_path, self.dict_path)
        self.thread.progress_signal.connect(self.log_area.append)
        self.thread.progress_value_signal.connect(self.pbar.setValue)
        self.thread.result_signal.connect(self.show_result)
        self.thread.finished_signal.connect(self.on_finish)
        self.thread.start()

    def stop_check(self):
        if self.thread:
            self.thread.stop()
            self.btn_stop.setEnabled(False)

    def show_result(self, pwd, time_taken):
        QMessageBox.information(self, "Muvaffaqiyat!", f"Parol topildi: {pwd}\nSarflangan vaqt: {time_taken}")
        self.log_area.append("\n" + "=" * 40)
        self.log_area.append(f"<b style='color:#a6e3a1; font-size:16px;'>✅ PAROL TOPILDI!</b>")
        self.log_area.append(f"🔑 Parol: <b style='color:#f9e2af; font-size:16px;'>{pwd}</b>")
        self.log_area.append(f"⏱ Vaqt: {time_taken}")
        self.log_area.append("=" * 40 + "\n")

    def on_finish(self, success):
        self.check_ready_to_start()
        self.btn_stop.setEnabled(False)
        self.btn_select_file.setEnabled(True)
        self.toggle_dict_btn()
        if not success:
            self.log_area.append("<b style='color:#f38ba8;'>🏁 Jarayon tugatildi.</b>")


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    window = ModernChecker()
    window.show()
    sys.exit(app.exec_())
