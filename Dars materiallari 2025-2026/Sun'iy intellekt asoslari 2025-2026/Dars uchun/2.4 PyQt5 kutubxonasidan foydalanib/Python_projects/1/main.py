from PyQt5.QtCore import Qt

label.setTextFormat(Qt.PlainText)   # qat'iy oddiy matn
label.setText("1 < 2 & 3")         # PlainText bo'lsa HTML teglari ishlamaydi

label.setTextFormat(Qt.RichText)    # HTML (rich text) ishlaydi
label.setText('<b>Qalin</b> va <span style="color:red">qizil</span>')
label.setOpenExternalLinks(True)    # <a href="..."> linklarini tashqi brauzerda ochish
