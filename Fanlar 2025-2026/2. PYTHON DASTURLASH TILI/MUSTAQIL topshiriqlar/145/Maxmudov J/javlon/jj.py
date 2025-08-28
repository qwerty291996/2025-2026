from PyQt5 import uic
from PyQt5.QtWidgets import *



app=QApplication([])
win=QMainWindow()
ui=uic.loadUi("j.ui")



def get():
    
    a=int(ui.son.text())
    g=a%10

    ui.birlar.setText(f"{g}")
    
    d=(a//10)%10
    ui.onlar.setText(f"{d}")


ui.chiqarish.clicked.connect(get)
ui.show()
app.exec_()