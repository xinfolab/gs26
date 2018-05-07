import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from Report import Ui_Report

class Ui_completed(QDialog):
  
    def __init__(self):
        super().__init__()
        self.completeUI()

    def completeUI(self):
        ### remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnBottomHint)

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\Scan_Completed.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(),back.height())

        ### Close Button
        close_btn = QPushButton('',self)
        close_btn.setIcon(QIcon('.\\img\\close_btn.png'))
        close_btn.setFixedSize(20,20)
        close_btn.setIconSize(QtCore.QSize(30,30))
        close_btn.move(back.width()-40,20)
        close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        close_btn.clicked.connect(QApplication.instance().quit)
        
        ### Open Report Button
        R_btn = QPushButton('',self)
        R_btn.setIcon(QIcon('.\\img\\Open_Report.png'))
        R_btn.setIconSize(QtCore.QSize(500,200))
        R_btn.setFixedSize(500,90)
        R_btn.move(90,180)
        R_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        R_btn.clicked.connect(self.R_btn_clicked)

        self.show()

    ### Open Report Button Clicked -> Report.GUI
    def R_btn_clicked(self):
        self.hide()
        self.UI = Ui_Report()
        self.UI.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    UI = Ui_completed()
    sys.exit(app.exec_())