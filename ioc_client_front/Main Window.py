import sys
from StartKx import Ui_Info

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon, QPixmap,QPalette

class Ui_MainWindow(QWidget):
  
    def __init__(self):
        super().__init__()
        self.mainUI()

    def mainUI(self):
        self.setGeometry(500, 300, 500, 600)
        self.setWindowTitle('Kx')

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\background.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(),back.height())

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)

        ### ID Label, txt
        ID_Label = QLabel('',self)
        ID_Label.setText('I D : ')
        ID_Label.setFont(font) 
        ID_Label.setStyleSheet("color: white")
        ID_Label.setFixedSize(50,50)
        ID_Label.move(50,430)

        ID_txt = QTextEdit('',self)
        ID_txt.setFixedSize(150,30)
        ID_txt.move(120,440)
        ID_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        ### PW Label, txt
        PW_Label = QLabel('',self)
        PW_Label.setText('PW : ')
        PW_Label.setFont(font)
        PW_Label.setStyleSheet("color: white")
        PW_Label.setFixedSize(50,50)
        PW_Label.move(50,490)

        PW_txt = QTextEdit('',self)
        PW_txt.setFixedSize(150,30)
        PW_txt.move(120,500)
        PW_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        
        ### Sign In Button
        sin_btn = QPushButton('',self)
        sin_btn.setText('Sign in')
        sin_btn.setFixedSize(120,40)
        sin_btn.move(300,435)
        sin_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ### Sign Up Button
        sup_btn = QPushButton('',self)
        sup_btn.setText('Sign up')
        sup_btn.setFixedSize(120,40)
        sup_btn.move(300,495)
        sup_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ###Btn_Clicked
        sin_btn.clicked.connect(self.sin_btn_clicked)
###        sup_btn.clicked.connect(self.sup_btn_clicked)

        self.show()

    def sin_btn_clicked(self):
        self.hide()
        self.UI = Ui_Info()
        self.UI.show()
###    def sup_btn_clicked(self):
###        UI = Ui_Processing()
###        UI.exec()
###        UI.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    UI = Ui_MainWindow()
    sys.exit(app.exec_())