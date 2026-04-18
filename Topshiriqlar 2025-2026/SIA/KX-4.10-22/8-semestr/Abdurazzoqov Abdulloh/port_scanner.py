import sys
import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QTextEdit, QLabel, QProgressBar)
from PyQt5.QtCore import pyqtSignal, QObject, Qt
from PyQt5.QtGui import QFont

# Signal boshqaruvi uchun klass
class ScannerSignals(QObject):
    log = pyqtSignal(str)
    progress = pyqtSignal(int)
    finished = pyqtSignal()

class FastPortScanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Oyna sozlamalari
        self.setWindowTitle('Ultra Fast Port Scanner')
        self.setFixedSize(500, 600)
        self.setStyleSheet("""
            QWidget { background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI', Arial; }
            QLineEdit { background-color: #313244; border: 1px solid #45475a; padding: 5px; border-radius: 4px; }
            QPushButton { background-color: #89b4fa; color: #1e1e2e; font-weight: bold; border-radius: 5px; padding: 10px; }
            QPushButton:hover { background-color: #b4befe; }
            QPushButton:disabled { background-color: #585b70; }
            QTextEdit { background-color: #181825; border: 1px solid #45475a; border-radius: 5px; font-family: 'Consolas'; }
            QProgressBar { border: 1px solid #45475a; border-radius: 5px; text-align: center; }
            QProgressBar::chunk { background-color: #a6e3a1; }
        """)

        layout = QVBoxLayout()

        # Host kiritish
        layout.addWidget(QLabel('Nishon IP yoki Domen (masalan: 127.0.0.1):'))
        self.host_input = QLineEdit('127.0.0.1')
        layout.addWidget(self.host_input)

        # Portlar va Oqimlar oralig'i
        settings_layout = QHBoxLayout()
        
        self.start_port = QLineEdit('1')
        self.end_port = QLineEdit('1024')
        self.thread_count = QLineEdit('100') # Bir vaqtda 100 ta portni tekshiradi

        settings_layout.addWidget(QLabel('Start:'))
        settings_layout.addWidget(self.start_port)
        settings_layout.addWidget(QLabel('End:'))
        settings_layout.addWidget(self.end_port)
        settings_layout.addWidget(QLabel('Oqimlar:'))
        settings_layout.addWidget(self.thread_count)
        
        layout.addLayout(settings_layout)

        # Boshqarish tugmasi
        self.scan_btn = QPushButton('SKANERLASHNI BOSHLASH')
        self.scan_btn.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_btn)

        # Progress bar
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # Natija maydoni
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def scan_port(self, host, port):
        """Bitta portni tekshirish logikasi"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0) # Har bir ulanish uchun max 1 soniya kutish
            result = sock.connect_ex((host, port))
            
            if result == 0:
                # Agar port ochiq bo'lsa, xizmat nomini ham aniqlashga urinish
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "noma'lum"
                self.signals.log.emit(f"✅ [OCHIQ] Port {port} ({service})")
            
            sock.close()
        except:
            pass
        
        # Progressni yangilash
        self.processed += 1
        percent = int((self.processed / self.total_ports) * 100)
        self.signals.progress.emit(percent)

    def run_worker(self, host, start, end, threads):
        """ThreadPoolExecutor yordamida skanerlashni boshqarish"""
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for port in range(start, end + 1):
                executor.submit(self.scan_port, host, port)
        
        self.signals.finished.emit()

    def start_scan(self):
        host = self.host_input.text()
        try:
            start = int(self.start_port.text())
            end = int(self.end_port.text())
            threads = int(self.thread_count.text())
        except ValueError:
            self.result_area.setText("⚠️ Xato: Portlar va oqimlar soni faqat raqam bo'lishi kerak!")
            return

        # UI tayyorlash
        self.result_area.clear()
        self.result_area.append(f"🔍 {host} skanerlanmoqda...\n")
        self.scan_btn.setEnabled(False)
        self.progress_bar.setValue(0)
        
        self.total_ports = end - start + 1
        self.processed = 0

        # Signallarni bog'lash
        self.signals = ScannerSignals()
        self.signals.log.connect(lambda msg: self.result_area.append(msg))
        self.signals.progress.connect(self.progress_bar.setValue)
        self.signals.finished.connect(self.on_finished)

        # Alohida thread-da skanerlashni boshlash (UI qotib qolmasligi uchun)
        t = threading.Thread(target=self.run_worker, args=(host, start, end, threads), daemon=True)
        t.start()

    def on_finished(self):
        self.result_area.append("\n✨ Skanerlash yakunlandi!")
        self.scan_btn.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Windowsda icon bilan muammo bo'lmasligi uchun
    app.setStyle('Fusion') 
    scanner = FastPortScanner()
    scanner.show()
    sys.exit(app.exec_())