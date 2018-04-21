# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from Processing import Ui_Processing as UI
from PyQt5.Qt import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
   
    def setupUi(self, Dialog): ## GUI 구성
        Dialog.setObjectName("Main Window")
        Dialog.resize(548, 515)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 87, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 87, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 87, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(79, 87, 94))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Dialog.setPalette(palette)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 491, 101))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 200, 111, 91))
        font = QtGui.QFont()
        font.setFamily("굴림체")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_N = QtWidgets.QPushButton(Dialog)
        self.pushButton_N.setGeometry(QtCore.QRect(60, 380, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.pushButton_N.setFont(font)
        self.pushButton_N.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_N.setStyleSheet("background-color:yellow")
        self.pushButton_N.setObjectName("pushButton_N")
        self.pushButton_Y = QtWidgets.QPushButton(Dialog)
        self.pushButton_Y.setGeometry(QtCore.QRect(300, 380, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.pushButton_Y.setFont(font)
        self.pushButton_Y.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Y.setStyleSheet("background-color:brgb(21, 95, 255)")
        self.pushButton_Y.setObjectName("pushButton_Y")
        
              
        self.pushButton_N.clicked.connect(QCoreApplication.instance().quit) ## Button N - 종료

        self.pushButton_Y.clicked.connect(self.mainUI) ## Button Y - 프로그램 시작 (누름과 동시 검사 시작)

    def retranslateUi(self, Dialog): ## Dinamic Language Switchting
        _translate = QtCore.QCoreApplication.translate
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setWindowTitle(_translate("Dialog", "Main Window"))
        self.label.setText(_translate("Dialog", "A malicous behavior Scanner base on"))
        self.label_2.setText(_translate("Dialog", "IOC"))
        self.pushButton_N.setText(_translate("Dialog", "No"))
        self.pushButton_Y.setText(_translate("Dialog", "Yes"))
   
    def mainUI(self):
        xmlf = QtWidgets.QDialog()
        xmlf.ui = UI()
        xmlf.ui.setupUi(xmlf)
        xmlf.exec_()
        xmlf.show() 
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

