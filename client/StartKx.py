import conn
import sys
import webbrowser

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont
from Processing import Ui_Processing

class Ui_Info(QDialog):

    def __init__(self,id ,ip):
        self.user_id = id
        self.user_ip = ip

        update = conn.update()
        update.start()

        super().__init__()
        self.initUI()

    def initUI(self):
        ### remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnBottomHint)

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\login.png')
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

        ### Label
        user_id = QLabel('ID :' + self.user_id , self)
        user_id.setFont(QFont('Arial', 15))
        user_id.setStyleSheet('color:white')
        user_id.move(220, 140)
        user_ip = QLabel('IP: ' + self.user_ip, self)
        user_ip.setFont(QFont('Arial', 15))
        user_ip.setStyleSheet('color:white')
        user_ip.move(220, 180)


        ### Open Report Button
        rbtn = QPushButton('', self)
        rbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        rbtn.setIcon(QIcon('.\\img\\report.png'))
        rbtn.setIconSize(QtCore.QSize(500, 100))
        rbtn.setFixedSize(400, 90)
        rbtn.move(60, 300)

        ### Search Start Button
        sbtn = QPushButton('', self)
        sbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sbtn.setIcon(QIcon('.\\img\\scan.png'))
        sbtn.setIconSize(QtCore.QSize(500, 100))
        sbtn.setFixedSize(400, 90)
        sbtn.move(60, 430)

        ### btn clicked
        rbtn.clicked.connect(self.report_view)
        sbtn.clicked.connect(self.start_search)

    ### start_search click
    def start_search(self):
        self.hide()
        self.UI = Ui_Processing(self.user_id)
        self.UI.show()

    def report_view(self):
        webbrowser.open("https://www.naver.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    iv = Ui_Info()
    sys.exit(app.exec_())
