import sys
import ipaddress
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QFrame,
    QScrollArea, QComboBox, QDialog
)
from PyQt5.QtCore import Qt


class SubnetDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Professional Subnetting Tool")
        self.setMinimumSize(560, 720)
        if parent:
            self.setStyleSheet(parent.styleSheet())
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Asosiy Tarmoq (Network/Prefix qo'yishni unutma):"))
        self.input_base = QLineEdit()
        self.input_base.setPlaceholderText("Masalan: 192.168.5.0/24 ")
        layout.addWidget(self.input_base)

        h_layout = QHBoxLayout()

        v_type = QVBoxLayout()
        v_type.addWidget(QLabel("Bo'lish usuli:"))
        self.combo_type = QComboBox()
        self.combo_type.addItems([
            "Subnetlar soniga qarab",
            "Hostlar soniga qarab",
            "VLSM"
        ])
        self.combo_type.currentIndexChanged.connect(self.update_placeholder)
        v_type.addWidget(self.combo_type)
        h_layout.addLayout(v_type)

        v_val = QVBoxLayout()
        v_val.addWidget(QLabel("Qiymatni kiriting:"))
        self.input_value = QLineEdit()
        self.input_value.setPlaceholderText("Masalan: 4")
        v_val.addWidget(self.input_value)
        h_layout.addLayout(v_val)

        layout.addLayout(h_layout)

        self.btn_sub = QPushButton("SUBNETLARNI HISOBLASH")
        self.btn_sub.setFixedHeight(45)
        self.btn_sub.clicked.connect(self.process_subnetting)
        layout.addWidget(self.btn_sub)

        self.logic_label = QLabel("")
        self.logic_label.setStyleSheet("""
            background-color: #313244;
            color: #fab387;
            padding: 10px;
            border: 1px dashed #fab387;
            border-radius: 5px;
            font-family: Consolas;
            font-size: 13px;
        """)
        self.logic_label.setWordWrap(True)
        self.logic_label.hide()
        layout.addWidget(self.logic_label)

        layout.addWidget(QLabel("Natijalar:"))
        self.result_area = QScrollArea()
        self.result_area.setWidgetResizable(True)

        self.res_content = QWidget()
        self.res_layout = QVBoxLayout(self.res_content)
        self.res_layout.setAlignment(Qt.AlignTop)

        self.result_area.setWidget(self.res_content)
        layout.addWidget(self.result_area)

    def update_placeholder(self):
        mode = self.combo_type.currentIndex()
        if mode == 0:
            self.input_value.setPlaceholderText("Masalan: 4")
        elif mode == 1:
            self.input_value.setPlaceholderText("Masalan: 50")
        else:
            self.input_value.setPlaceholderText("Masalan: 50, 40, 30, 20, 10")

    def clear_results(self):
        for i in reversed(range(self.res_layout.count())):
            item = self.res_layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

    def add_result_box(self, text):
        res_box = QLabel(text)
        res_box.setStyleSheet("""
            background-color: #45475a;
            padding: 12px;
            border-radius: 8px;
            color: #a6e3a1;
            margin-bottom: 8px;
            font-family: Consolas;
            font-size: 13px;
        """)
        res_box.setWordWrap(True)
        self.res_layout.addWidget(res_box)

    def parse_base_network(self, text):
        text = text.strip()
        if not text:
            raise ValueError("Asosiy tarmoqni kiriting!")

        # Agar prefix yozilmagan bo'lsa, /24 deb olinadi
        if "/" not in text:
            text += "/24"

        return ipaddress.IPv4Network(text, strict=False)

    def subnet_info_text(self, subnet, need_hosts=None, index=None):
        if subnet.prefixlen >= 31:
            first_host = "Foydalaniladigan host yo'q"
            last_host = "Foydalaniladigan host yo'q"
            usable_hosts = subnet.num_addresses
        else:
            first_host = str(subnet.network_address + 1)
            last_host = str(subnet.broadcast_address - 1)
            usable_hosts = subnet.num_addresses - 2

        lines = []
        if index is not None:
            lines.append(f"🔹 Subnet #{index}")
        if need_hosts is not None:
            lines.append(f"👥 Talab: {need_hosts} host")

        lines.extend([
            f"🌐 Tarmoq: {subnet.network_address}/{subnet.prefixlen}",
            f"🎭 Maska: {subnet.netmask}",
            f"📍 Birinchi host: {first_host}",
            f"📍 Oxirgi host: {last_host}",
            f"📢 Broadcast: {subnet.broadcast_address}",
            f"📦 Sig'imi: {usable_hosts} host"
        ])
        return "\n".join(lines)

    def process_equal_subnets(self, base_net, subnet_count):
        old_prefix = base_net.prefixlen
        borrowed_bits = math.ceil(math.log2(subnet_count))
        new_prefix = old_prefix + borrowed_bits

        if new_prefix > 32:
            raise ValueError("Prefix 32 dan oshib ketdi!")

        logic_text = (
            f"MANTIQ: {subnet_count} ta subnet uchun {borrowed_bits} bit qarz olindi.\n"
            f"Eski prefix: /{old_prefix} + {borrowed_bits} bit = Yangi prefix: /{new_prefix}"
        )
        self.logic_label.setText(logic_text)
        self.logic_label.show()

        subnets = list(base_net.subnets(new_prefix=new_prefix))
        for i, sn in enumerate(subnets, 1):
            self.add_result_box(self.subnet_info_text(sn, index=i))

    def process_host_based(self, base_net, host_count):
        old_prefix = base_net.prefixlen
        needed_bits = math.ceil(math.log2(host_count + 2))
        new_prefix = 32 - needed_bits

        if new_prefix < old_prefix:
            raise ValueError("Bu hostlar soni uchun asosiy tarmoq juda kichik!")

        logic_text = (
            f"MANTIQ: {host_count} ta host uchun {needed_bits} bit host qismi kerak.\n"
            f"32 - {needed_bits} bit = Yangi prefix: /{new_prefix}"
        )
        self.logic_label.setText(logic_text)
        self.logic_label.show()

        subnets = list(base_net.subnets(new_prefix=new_prefix))
        for i, sn in enumerate(subnets, 1):
            self.add_result_box(self.subnet_info_text(sn, index=i))

    def process_vlsm(self, base_net, hosts):
        hosts.sort(reverse=True)

        logic_lines = [
            "MANTIQ: VLSM usuli tanlandi.",
            f"Kiritilgan hostlar (katta -> kichik): {hosts}",
            "Agar subnet joriy tarmoqqa sig'masa, avtomatik keyingi tarmoqqa o'tadi."
        ]
        self.logic_label.setText("\n".join(logic_lines))
        self.logic_label.show()

        current_address = int(base_net.network_address)
        current_block_end = int(base_net.broadcast_address)
        base_prefix = base_net.prefixlen

        for i, need_hosts in enumerate(hosts, 1):
            needed_bits = math.ceil(math.log2(need_hosts + 2))
            prefix = 32 - needed_bits
            block_size = 2 ** needed_bits

            if prefix < base_prefix:
                raise ValueError(
                    f"{need_hosts} ta host uchun /{prefix} kerak bo'ladi. "
                    f"Bu esa asosiy /{base_prefix} tarmoqdan kattaroq blok."
                )

            aligned_address = ((current_address + block_size - 1) // block_size) * block_size
            subnet = ipaddress.IPv4Network((aligned_address, prefix), strict=False)

            # Agar joriy bazaviy blokka sig'masa, keyingi bazaviy blokka o'tkazamiz
            if int(subnet.broadcast_address) > current_block_end:
                next_block_start = current_block_end + 1
                current_address = next_block_start
                current_block_end = next_block_start + base_net.num_addresses - 1

                aligned_address = ((current_address + block_size - 1) // block_size) * block_size
                subnet = ipaddress.IPv4Network((aligned_address, prefix), strict=False)

                # Hizalanish sababli yana chiqib ketishi mumkin, shunda yana oldinga suramiz
                while int(subnet.broadcast_address) > current_block_end:
                    next_block_start = current_block_end + 1
                    current_address = next_block_start
                    current_block_end = next_block_start + base_net.num_addresses - 1
                    aligned_address = ((current_address + block_size - 1) // block_size) * block_size
                    subnet = ipaddress.IPv4Network((aligned_address, prefix), strict=False)

            self.add_result_box(self.subnet_info_text(subnet, need_hosts=need_hosts, index=i))
            current_address = int(subnet.broadcast_address) + 1

    def process_subnetting(self):
        self.clear_results()

        try:
            base_net = self.parse_base_network(self.input_base.text())
            mode = self.combo_type.currentIndex()
            raw_value = self.input_value.text().strip()

            if not raw_value:
                raise ValueError("Qiymatni kiriting!")

            if mode == 0:
                val = int(raw_value)
                if val <= 0:
                    raise ValueError("Subnet soni 0 dan katta bo'lishi kerak!")
                self.process_equal_subnets(base_net, val)

            elif mode == 1:
                val = int(raw_value)
                if val <= 0:
                    raise ValueError("Host soni 0 dan katta bo'lishi kerak!")
                self.process_host_based(base_net, val)

            else:
                hosts = [int(x.strip()) for x in raw_value.split(",") if x.strip()]
                if not hosts:
                    raise ValueError("VLSM uchun hostlar ro'yxatini kiriting. Masalan: 50, 40, 30, 20, 10")
                if any(h <= 0 for h in hosts):
                    raise ValueError("Barcha host sonlari musbat bo'lishi kerak!")

                self.process_vlsm(base_net, hosts)

        except Exception as e:
            QMessageBox.warning(self, "Xato", f"Xatolik yuz berdi: {str(e)}")


class NetworkCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("IP Network Analyzer PRO v2.0")
        self.resize(650, 820)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Segoe UI';
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #89b4fa;
            }
            QLineEdit {
                background-color: #313244;
                border: 2px solid #45475a;
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
                color: #f5e0dc;
            }
            QLineEdit:focus {
                border: 2px solid #89b4fa;
            }
            QPushButton {
                background-color: #89b4fa;
                color: #11111b;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #b4befe;
            }
            QComboBox {
                background-color: #313244;
                border: 1px solid #45475a;
                border-radius: 5px;
                padding: 5px;
                color: white;
            }
        """)

        main_layout = QVBoxLayout(self)

        header = QLabel("✨ Created by cadet Elmirzayev Akobirshoh")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("""
            QLabel {
                color: #f9e2af;
                font-size: 16px;
                font-weight: bold;
                padding: 10px;
                border-bottom: 2px solid #45475a;
                background-color: #181825;
            }
        """)
        main_layout.addWidget(header)

        top_bar = QHBoxLayout()
        top_bar.addStretch()

        self.btn_open_subnet = QPushButton("📡 SUBNETTING TOOL")
        self.btn_open_subnet.setFixedSize(190, 40)
        self.btn_open_subnet.setStyleSheet("""
            QPushButton {
                background-color: #fab387;
                color: #11111b;
                font-size: 13px;
                font-weight: bold;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #f9c59a;
            }
        """)
        self.btn_open_subnet.clicked.connect(self.open_subnet_dialog)
        top_bar.addWidget(self.btn_open_subnet)
        main_layout.addLayout(top_bar)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")

        container = QWidget()
        layout = QVBoxLayout(container)

        layout.addWidget(QLabel("Host IP manzilini kiriting:"))
        self.input_ip = QLineEdit()
        self.input_ip.setPlaceholderText("Masalan: 192.168.1.10")
        layout.addWidget(self.input_ip)

        layout.addWidget(QLabel("Prefix (CIDR):"))
        self.input_prefix = QLineEdit()
        self.input_prefix.setPlaceholderText("24")
        layout.addWidget(self.input_prefix)

        self.btn_calc = QPushButton("TAHLIL QILISH")
        self.btn_calc.clicked.connect(self.calculate_main)
        layout.addWidget(self.btn_calc)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: #45475a; margin: 10px 0;")
        layout.addWidget(line)

        self.res_labels = {}
        keys = [
            "Tarmoq adresi",
            "Maska",
            "Broadcast",
            "Birinchi host",
            "Oxirgi host",
            "Hostlar soni",
            "IP Klassi",
            "Turi (Private/Public)",
            "IP Binary",
            "Mask Binary"
        ]

        for k in keys:
            layout.addWidget(QLabel(f"{k}:"))
            lbl = QLabel("---")
            lbl.setTextInteractionFlags(Qt.TextSelectableByMouse)
            lbl.setStyleSheet("""
                background-color: #313244;
                padding: 10px;
                border-radius: 8px;
                font-family: Consolas;
                color: #a6e3a1;
                font-size: 14px;
            """)
            lbl.setWordWrap(True)
            layout.addWidget(lbl)
            self.res_labels[k] = lbl

        scroll.setWidget(container)
        main_layout.addWidget(scroll)

    def open_subnet_dialog(self):
        dialog = SubnetDialog(self)
        dialog.exec_()

    def calculate_main(self):
        try:
            ip_text = self.input_ip.text().strip()
            prefix_text = self.input_prefix.text().strip()

            if not ip_text or not prefix_text:
                raise ValueError("IP va prefixni to'liq kiriting!")

            prefix = int(prefix_text)
            if prefix < 0 or prefix > 32:
                raise ValueError("Prefix 0 dan 32 gacha bo'lishi kerak!")

            ip_obj = ipaddress.IPv4Address(ip_text)
            net = ipaddress.IPv4Network(f"{ip_text}/{prefix}", strict=False)

            self.res_labels["Tarmoq adresi"].setText(str(net.network_address))
            self.res_labels["Maska"].setText(str(net.netmask))
            self.res_labels["Broadcast"].setText(str(net.broadcast_address))

            if prefix >= 31:
                self.res_labels["Birinchi host"].setText("Foydalaniladigan host yo'q")
                self.res_labels["Oxirgi host"].setText("Foydalaniladigan host yo'q")
                count = net.num_addresses
            else:
                self.res_labels["Birinchi host"].setText(str(net.network_address + 1))
                self.res_labels["Oxirgi host"].setText(str(net.broadcast_address - 1))
                count = net.num_addresses - 2

            self.res_labels["Hostlar soni"].setText(str(count))

            first_octet = int(ip_text.split('.')[0])
            if 1 <= first_octet <= 126:
                cls = "A"
            elif 128 <= first_octet <= 191:
                cls = "B"
            elif 192 <= first_octet <= 223:
                cls = "C"
            else:
                cls = "D/E"

            self.res_labels["IP Klassi"].setText(f"{cls} Klass")
            self.res_labels["Turi (Private/Public)"].setText(
                "Private (Ichki)" if ip_obj.is_private else "Public (Tashqi)"
            )

            binary_ip = ".".join(format(int(x), "08b") for x in ip_text.split("."))
            binary_mask = ".".join(format(int(x), "08b") for x in str(net.netmask).split("."))

            self.res_labels["IP Binary"].setText(binary_ip)
            self.res_labels["Mask Binary"].setText(binary_mask)

        except Exception as e:
            QMessageBox.critical(self, "Xato", f"Ma'lumot noto'g'ri: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetworkCalculator()
    window.show()
    sys.exit(app.exec_())