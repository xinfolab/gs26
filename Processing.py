import sys
from Completed import Ui_completed

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QDialog
from PyQt5.QtGui import QIcon

class Ui_Processing(QDialog):

    def __init__(self):

        super().__init__()

        self.processUI()

    def processUI(self):
        ### GUI size
        self.setGeometry(1000,500,800,600)
        self.setWindowTitle('Kx')
        self.setStyleSheet("background-color: brgb(33, 33, 33)")

        
        ### GIF set
        self.moviee = QLabel(self)
        self.movie = QtGui.QMovie(".\\img\\Processing.gif")
        self.moviee.setMovie(self.movie)
        self.moviee.setGeometry(50,50,300,100)
        self.movie.start()     

        ### Pause Button
        P_btn = QPushButton('',self)
        P_btn.setIcon(QIcon('.\\img\\Pause.png'))
        P_btn.setIconSize(QtCore.QSize(170,90))
        P_btn.setFixedSize(150,70)
        P_btn.move(420,50)

        ### Continue Button
        C_btn = QPushButton('',self)
        C_btn.setIcon(QIcon('.\\img\\Continue.png'))
        C_btn.setIconSize(QtCore.QSize(170,90))
        C_btn.setFixedSize(150,70)
        C_btn.move(420,50)

        ### Cancel Button
        Can_btn = QPushButton('',self)
        Can_btn.setIcon(QIcon('.\\img\\Cancel.png'))
        Can_btn.setIconSize(QtCore.QSize(170,90))
        Can_btn.setFixedSize(150,70)
        Can_btn.move(600,50)

        ### Start Button

        S_btn = QPushButton('',self)
        S_btn.setIcon(QIcon('.\\img\\Start.png'))
        S_btn.setIconSize(QtCore.QSize(170,90))
        S_btn.setFixedSize(150,70)
        S_btn.move(600,50)

        ### hide btn P & S
        C_btn.hide()
        S_btn.hide()

        ### Btn Clicked
###        P_btn.clicked.connect(self.P_btn_clicked)
###        C_btn.clicked.connect(self.C_btn_clicked)
###        Can_btn.clicked.connect(self.Can_btn_clicked)
###        S_btn.clicked.connect(self.S_btn_clicked)

        self.show()

       ### clicked btn event
###    def P_btn_clicked(self, state):
###        self.P_btn.setDisabled()
###        self.C_btn.setEnabled(True)

###    def C_btn_clicked(self):
###       self.sender().setVisible(False)
###       self.P_btn.setVisible(True)

###    def Can_btn_clicked(self,state) :
###        self.sender().setVisible(False)
###        self.S_btn.setVisible(True)

###    def S_btn_clicked(self,state) :
###        self.sender().setVisible(False)
###        self.Can_btn.setVisible(True)


###    def search completed then open Completed GUI
###        self.hide()
#          self.UI = Ui_completed()
###        UI.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = Ui_Processing()
    sys.exit(app.exec_())


           ### 비활성 self.sender().setEnabled(False)
