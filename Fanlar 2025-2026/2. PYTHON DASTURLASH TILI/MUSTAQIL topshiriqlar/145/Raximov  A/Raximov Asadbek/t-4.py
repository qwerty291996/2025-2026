# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:21:02 2024

@author: User
"""
from PyQt5 import QtWidgets,uic
app = QtWidgets.QApplication([])
ui = uic.loadUi("t-4.ui")
def OK():

    a = ui.A.displayText()
    #123
    k = int(a)%10 #k=3
    t = int(a)//10 # t = 12
    s = k*100+t
    ui.natija.setText(str(s))

ui.OK.clicked.connect(OK)
ui.show()
app.exec_()


