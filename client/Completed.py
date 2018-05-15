import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QCursor
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
        
        ### Open Report Button
        R_btn = QPushButton('',self)
        R_btn.setIcon(QIcon('.\\img\\Open_Report.png'))
        R_btn.setIconSize(QtCore.QSize(500,200))
        R_btn.setFixedSize(500,90)
        R_btn.move(90,200)
        R_btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        ### close Button
        close_Btn = QPushButton('',self)
        close_Btn.setIcon(QIcon('.\\img\\close_btn.png'))
        close_Btn.setFixedSize(20,20)
        close_Btn.setIconSize(QtCore.QSize(30,30))
        close_Btn.move(back.width()-40,20)
        close_Btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        close_Btn.clicked.connect(QApplication.instance().quit)

        self.show()
        ### Click Open_Report Btn -> Web
        ### def R_btn_clicked(self) :
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    UI = Ui_completed()
    sys.exit(app.exec_())
