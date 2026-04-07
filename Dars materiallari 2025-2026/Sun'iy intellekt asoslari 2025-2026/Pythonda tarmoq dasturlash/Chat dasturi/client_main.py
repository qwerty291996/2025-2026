import sys
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
# Siz yaratgan dizayn faylini import qilamiz
from chat_design import Ui_MainWindow 

class ReceiverThread(QThread):
    """Tarmoqdan xabarlarni doimiy eshitib turuvchi alohida oqim"""
    signal_message = pyqtSignal(str)
    signal_users = pyqtSignal(list)

    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        while True:
            try:
                data = self.sock.recv(1024).decode('utf-8')
                if not data: break
                
                # Agar server foydalanuvchilar ro'yxatini yuborgan bo'lsa
                if data.startswith("USERS_LIST:"):
                    users = data.replace("USERS_LIST:", "").split(",")
                    self.signal_users.emit(users)
                else:
                    # Oddiy xabar bo'lsa
                    self.signal_message.emit(data)
            except:
                break

class ChatApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Dizaynni yuklash
        
        # 1. Serverga ulanish (Hozircha localhost)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect(('127.0.0.1', 5555))
            # Ismni yuboramiz (Hozircha vaqtincha ism)
            self.nickname = "Foydalanuvchi_" + str(hash(self))[:4]
            self.client_socket.send(self.nickname.encode('utf-8'))
        except:
            print("Serverga ulanib bo'lmadi!")

        # 2. Xabarlarni qabul qiluvchi oqimni yoqish
        self.receiver = ReceiverThread(self.client_socket)
        self.receiver.signal_message.connect(self.display_message)
        self.receiver.signal_users.connect(self.update_user_list)
        self.receiver.start()

        # 3. Tugmalarni funksiyalarga bog'lash
        self.pushButton_send.clicked.connect(self.send_text_message)
        self.pushButton_attach.clicked.connect(self.send_file_dialog)
        
        # ProgressBar-ni yashirib qo'yamiz (Siz Designer-da topa olmagan joyingiz)
        self.progressBar.hide()

    def update_user_list(self, users):
        self.listWidget_users.clear()
        for user in users:
            if user != self.nickname:
                self.listWidget_users.addItem(user)

    def send_text_message(self):
        receiver = self.listWidget_users.currentItem()
        message = self.textEdit_message.toPlainText() # QTextEdit-dan matnni olish
        
        if receiver and message:
            target = receiver.text()
            full_msg = f"{target}:{message}"
            self.client_socket.send(full_msg.encode('utf-8'))
            self.textEdit_chat.append(f"Siz -> {target}: {message}")
            self.textEdit_message.clear()

    def display_message(self, data):
        # Kelgan xabar formati "SENDER:MESSAGE"
        if ":" in data:
            sender, msg = data.split(":", 1)
            self.textEdit_chat.append(f"<b>{sender}:</b> {msg}")

    def send_file_dialog(self):
        # Fayl tanlash oynasi
        file_path, _ = QFileDialog.getOpenFileName(self, "Faylni tanlang")
        if file_path:
            self.textEdit_chat.append(f"<i>Fayl tanlandi: {file_path} (Yuborish logikasi keyingi darsda)</i>")
            # Bu yerga o'sha biz yozgan send_file funksiyasini ulaymiz

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec_())