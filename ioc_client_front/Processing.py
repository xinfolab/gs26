import sys
from Completed import Ui_completed

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QIcon

class Ui_Processing(QDialog):

    def __init__(self):

        super().__init__()

        self.processUI()

    def processUI(self):
        ### remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnBottomHint)

        ### background image and Fixed Size
        back_label = QLabel(self)
        back = QPixmap('.\\img\\33_back.png')
        back_label.setPixmap(back)
        self.setFixedSize(back.width(),back.height())
        
        ### close Button
        close_btn = QPushButton('',self)
        close_btn.setIcon(QIcon('.\\img\\close_btn.png'))
        close_btn.setFixedSize(20,20)
        close_btn.setIconSize(QtCore.QSize(30,30))
        close_btn.move(back.width()-40,20)
        close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        close_btn.clicked.connect(QApplication.instance().quit)

        ### GIF set
        self.moviee = QLabel(self)
        self.movie = QtGui.QMovie(".\\img\\Processing.gif")
        self.moviee.setMovie(self.movie)
        self.moviee.setGeometry(50,50,300,100)
        self.movie.start()     

        ### Pause Button
        self.P_btn = QPushButton('',self)
        self.P_btn.setIcon(QIcon('.\\img\\Pause.png'))
        self.P_btn.setIconSize(QtCore.QSize(170,90))
        self.P_btn.setFixedSize(150,70)
        self.P_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.P_btn.move(420,50)

        ### Continue Button
        self.C_btn = QPushButton('',self)
        self.C_btn.setIcon(QIcon('.\\img\\Continue.png'))
        self.C_btn.setIconSize(QtCore.QSize(170,90))
        self.C_btn.setFixedSize(150,70)
        self.C_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.C_btn.move(420,50)

        ### Cancel Button
        self.Can_btn = QPushButton('',self)
        self.Can_btn.setIcon(QIcon('.\\img\\Cancel.png'))
        self.Can_btn.setIconSize(QtCore.QSize(170,90))
        self.Can_btn.setFixedSize(150,70)
        self.Can_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Can_btn.move(600,50)

        ### Start Button

        self.S_btn = QPushButton('',self)
        self.S_btn.setIcon(QIcon('.\\img\\Start.png'))
        self.S_btn.setIconSize(QtCore.QSize(170,90))
        self.S_btn.setFixedSize(150,70)
        self.S_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.S_btn.move(600,50)

        ### hide btn P & S
        self.C_btn.setVisible(False)
        self.S_btn.setVisible(False)

        ### tabWidget ~ tab4
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(50, 200, 700, 350))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab, "File")
        self.tab_2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_2, "Registry")
        self.tab_3 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_3, "Network")
        self.tab_4 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_4, "Process")
        

        ### Btn Clicked
        self.P_btn.clicked.connect(self.P_btn_clicked)
        self.C_btn.clicked.connect(self.C_btn_clicked)
        self.Can_btn.clicked.connect(self.Can_btn_clicked)
        self.S_btn.clicked.connect(self.S_btn_clicked)

        self.show()

       ### clicked btn event show and hide
    def P_btn_clicked(self):
        self.P_btn.setVisible(False)
        self.C_btn.setVisible(True)

    def C_btn_clicked(self):
        self.C_btn.setVisible(False)
        self.P_btn.setVisible(True)

    def Can_btn_clicked(self,state):
        self.Can_btn.setVisible(False)
        self.S_btn.setVisible(True)
        self.P_btn.setVisible(False)

    def S_btn_clicked(self,state):
        self.S_btn.setVisible(False)
        self.Can_btn.setVisible(True)
        self.P_btn.setVisible(True)

###    def search completed then open Completed GUI
###        self.hide()
#          self.UI = Ui_completed()
###        UI.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = Ui_Processing()
    sys.exit(app.exec_())
