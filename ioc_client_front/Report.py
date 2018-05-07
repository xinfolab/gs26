import sys
import threading,time

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QPushButton
from PyQt5.QtGui import QIcon, QPixmap

class Ui_Report(QDialog):
  
    def __init__(self):
        super().__init__()
        self.ReportUI()

    def ReportUI(self):
        ### remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnBottomHint)

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\33_back.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(),back.height())

        ### Close Button
        close_btn = QPushButton('',self)
        close_btn.setIcon(QIcon('.\\img\\close_btn.png'))
        close_btn.setFixedSize(20,20)
        close_btn.setIconSize(QtCore.QSize(30,30))
        close_btn.move(back.width()-40,20)
        close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        close_btn.clicked.connect(self.close_window)

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
        
        ### Date Label 
        font.setPointSize(12)
        now = time.localtime()
        t_date = "%04d.%02d.%02d" % (now.tm_year, now.tm_mon, now.tm_mday)

        tdate_Label = QLabel('',self)
        tdate_Label.setText(t_date)
        tdate_Label.setFont(font)
        tdate_Label.setStyleSheet("color : white")
        tdate_Label.move(650,20)

        ### time Label
        self.ttime_Label = QLabel('',self)
        self.ttime_Label.setFont(font)
        self.ttime_Label.setStyleSheet("color : white")
        self.ttime_Label.move(650,50)

        ### tabWidget set
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(50, 200, 700, 350))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "All")
        self.tab_2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_2, "File")
        self.tab_3 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_3, "Registry")
        self.tab_4 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_4, "Network")
        self.tab_5 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_5, "Process")
        self.show_Time()
        self.show()
    
    ### get current time
    def show_Time(self):
        now = time.localtime()
        t_time = "   %02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
        self.ttime_Label.setText(t_time)
        self.timer = threading.Timer(1,self.show_Time)
        self.timer.start()

    def close_window(self):
        self.timer.cancel()
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    UI = Ui_Report()
    sys.exit(app.exec_())