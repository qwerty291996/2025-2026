from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
win = QtWidgets.QMainWindow()
ui = uic.loadUi('textEditor.ui')
ui.setWindowTitle("Salom")

def Open():
    adress = ui.URL.displayText()
    file = open(adress, 'r', encoding = 'utf-8')
    text = file.read()
    ui.Editor.setText(text)
    file.close
    
def Save():
    name = ui.Name.displayText() + '.txt'
    save_f = open(name, 'w', encoding='utf-8')
    edText = ui.Editor.toPlainText()
    save_f.write(edText)
    save_f.close

def Close():
    answer = QtWidgets.QMessageBox().question(
        win, None, "Would you like to save or not?",
        QtWidgets.QMessageBox.Save|QtWidgets.QMessageBox.Cancel
        
    )
    print(answer)
    ui.Editor.setText("")

ui.Save.clicked.connect(Save)
ui.Close.clicked.connect(Close)
ui.Open.clicked.connect(Open)

ui.show()
app.exec_()    
    
    



