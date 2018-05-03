import sys
from Report import Ui_Report

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
class Ui_completed(QDialog):
  
    def __init__(self):
        super().__init__()
        self.completeUI()

    def completeUI(self):

        self.setWindowTitle('Kx')
        self.setWindowIcon(QIcon('.\\img\\QIcon.png'))

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\Scan_Completed.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(),back.height())

        
        ### Open Report Button
        R_btn = QPushButton('',self)
        R_btn.setIcon(QIcon('.\\img\\Open_Report.png'))
        R_btn.setIconSize(QtCore.QSize(500,200))
        R_btn.setFixedSize(500,100)
        R_btn.move(100,250)
        R_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()
        ### Completed GUI -> Report GUI
###        self.hide()
###        self.UI = Ui_Report()
###        self.UI.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    UI = Ui_completed()
    sys.exit(app.exec_())