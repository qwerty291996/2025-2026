from PyQt5 import uic
from PyQt5.QtWidgets import *



app=QApplication([])
win=QMainWindow()
ui=uic.loadUi("olma.ui")



def get():
    
    a=int(ui.son.text())
    s=a%10
    f=(a//10)%10
    d=a//100
    
    m=s+d+f
    ui.olma.setText(f"{m}")




ui.hisob.clicked.connect(get)
ui.show()
app.exec_()