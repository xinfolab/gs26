import sys
from urllib.request import urlopen
import conn

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QTextEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from StartKx import Ui_Info


class Ui_MainWindow(QWidget):
    id = None
    password = None

    def __init__(self):
        super().__init__()
        self.mainUI()

    def mainUI(self):
        ### remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnBottomHint)

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\background.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(), back.height())

        ### close Button
        close_btn = QPushButton('',self)
        close_btn.setIcon(QIcon('.\\img\\close_btn.png'))
        close_btn.setFixedSize(20,20)
        close_btn.setIconSize(QtCore.QSize(30,30))
        close_btn.move(back.width()-40,20)
        close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        close_btn.clicked.connect(QApplication.instance().quit)

        ### set Font
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

        self.ID_txt = QTextEdit('',self)
        self.ID_txt.setFixedSize(150,30)
        self.ID_txt.move(120,440)
        self.ID_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

        ### PW Label, txt
        PW_Label = QLabel('',self)
        PW_Label.setText('PW : ')
        PW_Label.setFont(font)
        PW_Label.setStyleSheet("color: white")
        PW_Label.setFixedSize(50,50)
        PW_Label.move(50,490)

        self.PW_txt = QTextEdit('',self)
        self.PW_txt.setFixedSize(150,30)
        self.PW_txt.move(120,500)
        self.PW_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))

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

    def err_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Enter the ID or Password ")
        msg.setWindowTitle("Login Error")

        res = msg.exec_()

    def sin_btn_clicked(self):
        self.id = self.ID_txt.toPlainText()
        self.password = self.PW_txt.toPlainText()

        login_class = conn.login()
        user_token = login_class.login_start(self.id, self.password)
        if False == user_token:
            self.err_messagebox()

        else:
            conn.server_data.USER_TOKEN = user_token
            self.hide()
            self.UI = Ui_Info(self.id, (urlopen('http://ip.42.pl/raw').read()).decode())
            self.UI.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    UI = Ui_MainWindow()
    sys.exit(app.exec_())
