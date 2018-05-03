import sys
import time

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon

class Ui_Report(QDialog):
  
    def __init__(self):
        super().__init__()
        self.ReportUI()

    def ReportUI(self):
        self.setGeometry(1000,500,800,600)
        self.setWindowTitle('Kx')
        self.setStyleSheet("background-color: brgb(33, 33, 33)")

        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        
        ### Kx Label
        Kx_Label = QLabel('',self)
        Kx_Label.setText('Kx')
        Kx_Label.setFont(font)
        Kx_Label.setStyleSheet("color : white")
        Kx_Label.setFixedSize(100,100)
        Kx_Label.move(30,0)

        ### User name's Report Label
        font.setPointSize(20)
        Uname_Label = QLabel('',self)
        Uname_Label.setText('K3y6reak\'s Report')
        Uname_Label.setFont(font)
        
        Uname_Label.setStyleSheet("color : white")
        Uname_Label.setFixedSize(300,100)
        Uname_Label.move(220,0)
        
        ### Time Label Threading 구현 예정
        font.setPointSize(12)
        now = time.localtime()
        t_date = "%04d.%02d.%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
        t_time = "   %02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)

        tdate_Label = QLabel('',self)
        tdate_Label.setText(t_date)
        tdate_Label.setFont(font)
        tdate_Label.setStyleSheet("color : white")
        tdate_Label.move(650,20)

        ttime_Label = QLabel('',self)
        ttime_Label.setText(t_time)
        ttime_Label.setFont(font)
        ttime_Label.setStyleSheet("color : white")
        ttime_Label.move(650,50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    UI = Ui_Report()
    sys.exit(app.exec_())