from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

app = QApplication(sys.argv)

win = QWidget()
layout = QVBoxLayout(win)

label = QLabel("Salom, QLabel!")
layout.addWidget(label)




label.setStyleSheet("""
    font-family: 'Times New Roman';
    font-size: 20px;
    font-weight: bold;
    color: darkred;
""")





















win.show()
sys.exit(app.exec_())
