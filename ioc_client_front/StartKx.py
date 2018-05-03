import sys
import webbrowser
from Processing import Ui_Processing

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Ui_Info(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 500, 600)
        self.setWindowTitle('A Malicious behavior scanner based on IOC')
        self.setWindowIcon(QIcon('.\\img\\icon.png'))

        back_label = QLabel(self)
        back = QPixmap('.\\img\\login.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(), back.height())


        user_id = QLabel('ID: k3y6reak', self)
        user_id.setFont(QFont('Arial', 20))
        user_id.setStyleSheet('color:white')
        user_id.move(310, 130)
        user_ip = QLabel('IP: 117.16.11.18', self)
        user_ip.setFont(QFont('Arial', 20))
        user_ip.setStyleSheet('color:white')
        user_ip.move(310, 170)


        rbtn = QPushButton('', self)
        
        rbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        rbtn.setIcon(QIcon('.\\img\\report.png'))
        rbtn.setIconSize(QtCore.QSize(500, 100))
        rbtn.setFixedSize(400, 90)
        rbtn.move(60, 300)

        ### btn Search Start
        sbtn = QPushButton('', self)
        sbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sbtn.setIcon(QIcon('.\\img\\scan.png'))
        sbtn.setIconSize(QtCore.QSize(500, 100))
        sbtn.setFixedSize(400, 90)
        sbtn.move(60, 430)
        
        ### btn clicked
        rbtn.clicked.connect(self.report_view)
        sbtn.clicked.connect(self.start_search)

    def start_search(self):
        self.hide()
        self.UI = Ui_Processing()
        self.UI.show()

    def report_view(self):
        webbrowser.open("https://www.naver.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    iv = Ui_Info()
    sys.exit(app.exec_())

