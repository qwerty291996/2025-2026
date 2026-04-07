import sys, itertools, string, pyzipper, rarfile, multiprocessing, subprocess, os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QLineEdit, QLabel, QFileDialog, QTextEdit, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal, Qt

# 7-Zip yo'li
SEVEN_ZIP_PATH = r"C:\Program Files\7-Zip\7z.exe"

# 1. MUSTAQIL FUNKSIYA (KLASSDAN TASHQARIDA BO'LISHI SHART)
def check_password_universal(file_path, password):
    try:
        if os.path.exists(SEVEN_ZIP_PATH):
            cmd = [SEVEN_ZIP_PATH, "t", file_path, f"-p{password}", "-y"]
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)
            return result.returncode == 0
        
        if file_path.lower().endswith('.zip'):
            with pyzipper.AESZipFile(file_path) as zf:
                zf.extractall(pwd=password.encode(), path="temp_ext")
                return True
        elif file_path.lower().endswith('.rar'):
            with rarfile.RarFile(file_path) as rf:
                rf.extractall(pwd=password, path="temp_ext")
                return True
    except:
        return False
    return False

# 2. MULTIPROCESSING UCHUN WRAPPER (KLASSDAN TASHQARIDA)
def check_batch_wrapper(args):
    file_path, passwords = args
    for pwd in passwords:
        if check_password_universal(file_path, pwd):
            return pwd
    return None

class FastCrackerThread(QThread):
    status_signal = pyqtSignal(str)
    current_pw_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool, str)

    def __init__(self, file_path, mode, dict_path=None):
        super().__init__()
        self.file_path = file_path
        self.mode = mode
        self.dict_path = dict_path
        self._is_running = True

    def run(self):
        num_cores = multiprocessing.cpu_count()
        batch_size = 500
        pool = multiprocessing.Pool(processes=num_cores)
        found_password = None

        try:
            if self.mode == "numbers":
                self.status_signal.emit(f"🚀 {num_cores} yadroli qidiruv...")
                for length in range(1, 7):
                    if not self._is_running or found_password: break
                    self.status_signal.emit(f"🔹 {length} xonali raqamlar...")
                    iterable = ("".join(p) for p in itertools.product(string.digits, repeat=length))
                    
                    while self._is_running:
                        batch = list(itertools.islice(iterable, batch_size * num_cores))
                        if not batch: break
                        
                        chunks = [batch[i:i + batch_size] for i in range(0, len(batch), batch_size)]
                        task_data = [(self.file_path, chunk) for chunk in chunks]
                        
                        # MANA SHU QATOR TO'G'RI: self.wrapper ishlatilmayapti
                        results = pool.map(check_batch_wrapper, task_data)
                        
                        for r in results:
                            if r: 
                                found_password = r
                                break
                        if found_password: break
                        self.current_pw_signal.emit(batch[-1])

            else: # LUG'AT REJIMI
                self.status_signal.emit(f"📖 Lug'at yuklanmoqda...")
                with open(self.dict_path, 'r', encoding='utf-8', errors='ignore') as f:
                    while self._is_running:
                        batch = [f.readline().strip() for _ in range(batch_size * num_cores)]
                        batch = [p for p in batch if p]
                        if not batch: break
                        chunks = [batch[i:i + batch_size] for i in range(0, len(batch), batch_size)]
                        task_data = [(self.file_path, chunk) for chunk in chunks]
                        results = pool.map(check_batch_wrapper, task_data)
                        for r in results:
                            if r: 
                                found_password = r
                                break
                        if found_password: break
                        self.current_pw_signal.emit(batch[-1])
        finally:
            pool.terminate()
            pool.join()

        if found_password:
            self.finished_signal.emit(True, found_password)
        else:
            self.finished_signal.emit(False, "Topilmadi")

    def stop(self):
        self._is_running = False

class UltraCrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Universal Archive Cracker Pro v9.0')
        self.setFixedSize(550, 650)
        self.setStyleSheet("""
            QWidget { background-color: #0f0f0f; color: #00ff41; font-family: 'Consolas'; }
            QLineEdit { background-color: #1a1a1a; border: 1px solid #00ff41; padding: 8px; color: #fff; }
            QPushButton { background-color: #1a1a1a; border: 1px solid #00ff41; padding: 10px; font-weight: bold; color: #00ff41; }
            QPushButton:hover { background-color: #00ff41; color: #000; }
            QTextEdit { background-color: #000; border: 1px solid #333; color: #00ff41; }
            #status_label { color: #ffeb3b; font-size: 20px; font-weight: bold; }
        """)
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Arxiv faylini tanlang (7z/ZIP/RAR):'))
        
        file_layout = QHBoxLayout()
        self.file_input = QLineEdit()
        self.btn_browse = QPushButton('📁 Tanlash')
        self.btn_browse.clicked.connect(self.browse_archive)
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(self.btn_browse)
        layout.addLayout(file_layout)

        self.status_label = QLabel('TAYYOR')
        self.status_label.setObjectName("status_label")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        grid = QHBoxLayout()
        btn_num = QPushButton('🔢 RAQAMLAR')
        btn_rock = QPushButton('🔥 ROCKYOU')
        btn_custom = QPushButton('📂 MY DICT')
        btn_num.clicked.connect(lambda: self.start_process("numbers"))
        btn_rock.clicked.connect(lambda: self.start_process("rockyou"))
        btn_custom.clicked.connect(lambda: self.start_process("custom"))
        grid.addWidget(btn_num)
        grid.addWidget(btn_rock)
        grid.addWidget(btn_custom)
        layout.addLayout(grid)

        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        self.btn_stop = QPushButton('🛑 TO\'XTATISH')
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.stop_process)
        layout.addWidget(self.btn_stop)
        self.setLayout(layout)

    def browse_archive(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Arxivni tanlang', '', "Archives (*.zip *.rar *.7z)")
        if fname: self.file_input.setText(fname)

    def start_process(self, mode):
        archive = self.file_input.text()
        if not archive: return
        dict_path = None
        if mode in ["rockyou", "custom"]:
            dict_path, _ = QFileDialog.getOpenFileName(self, 'Lug\'atni tanlang', '', "Text files (*.txt)")
            if not dict_path: return

        self.btn_stop.setEnabled(True)
        self.thread = FastCrackerThread(archive, mode, dict_path)
        self.thread.status_signal.connect(self.log_area.append)
        self.thread.current_pw_signal.connect(self.status_label.setText)
        self.thread.finished_signal.connect(self.on_finished)
        self.thread.start()

    def stop_process(self):
        if hasattr(self, 'thread'): self.thread.stop()

    def on_finished(self, found, result):
        self.btn_stop.setEnabled(False)
        if found:
            QMessageBox.information(self, "Topildi!", f"Parol: {result}")
        else:
            QMessageBox.warning(self, "Tugadi", "Parol topilmadi.")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    ex = UltraCrackerApp()
    ex.show()
    sys.exit(app.exec_())
