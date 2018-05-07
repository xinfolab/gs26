import sys
from info import info_view
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap

class main_view(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 300, 500, 600)
        self.setWindowTitle('A malicious behavior scanner based on IOC')
        self.setWindowIcon(QIcon('.\\img\\icon.png'))

        #background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\background.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(), back.height())

        # Quit Button
        qbtn = QPushButton('', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.setIcon(QIcon('.\\img\\No.png'))
        qbtn.setIconSize(QtCore.QSize(170, 90))
        qbtn.setFixedSize(150, 70)
        qbtn.move(50, 450)

        # Excute Button
        ebtn = QPushButton('', self)
        ebtn.clicked.connect(self.info)
        ebtn.setIcon(QIcon('.\\img\\Yes.png'))
        ebtn.setIconSize(QtCore.QSize(170, 90))
        ebtn.setFixedSize(150, 70)
        ebtn.move(320, 450)
        self.show()

    def info(self):
        self.hide()
        self.info = info_view()
        self.info.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mv = main_view()

    sys.exit(app.exec_())
