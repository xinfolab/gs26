import sys
import webbrowser
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QFont

class info_view(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def report_view(self):
        webbrowser.open("https://www.naver.com")


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
        user_ip = QLabel('IP: 117.16.11.8', self)
        user_ip.setFont(QFont('Arial', 20))
        user_ip.setStyleSheet('color:white')
        user_ip.move(310, 170)


        rbtn = QPushButton('', self)
        rbtn.clicked.connect(self.report_view)
        rbtn.setIcon(QIcon('.\\img\\report.png'))
        rbtn.setIconSize(QtCore.QSize(500, 100))
        rbtn.setFixedSize(400, 90)
        rbtn.move(60, 300)

        sbtn = QPushButton('', self)
        sbtn.clicked.connect(QApplication.instance().quit)
        sbtn.setIcon(QIcon('.\\img\\scan.png'))
        sbtn.setIconSize(QtCore.QSize(500, 100))
        sbtn.setFixedSize(400, 90)
        sbtn.move(60, 430)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    iv = info_view()
    sys.exit(app.exec_())
