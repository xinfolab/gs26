import sys
import core
import time
import pythoncom
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QPushButton, QDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from GotoTray import GoTrayUI


class get_ip_thread(QThread):
    gipEvent = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.ip_data = []

    def run(self):
        pythoncom.CoInitialize()
        gip = core.get_ip.ip()
        self.ip_data = gip.get_ip()
        self.gipEvent.emit(self.ip_data)
        self.sleep(10)


class get_registry_thread(QThread):
    gregEvent = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.reg_data = []

    def run(self):
        pythoncom.CoInitialize()
        greg = core.get_registry.registry()
        self.reg_data = greg.find_ioc_of_registry()
        self.gregEvent.emit(self.reg_data)

class get_proc_thread(QThread):
    gprocEvent = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.proc_data = {}

    def run(self):
        pythoncom.CoInitialize()
        self.sleep(20)
        gproc = core.get_proc_and_hash.proc()
        self.proc_data = gproc.get_proc()
        self.gprocEvent.emit(self.proc_data)


class get_file_thread(QThread):
    gfileEvent = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.file_data = {}

    def run(self):
        pythoncom.CoInitialize()
        gfile = core.get_file_and_hash.file_path()
        self.file_data = gfile.get_file()
        self.gfileEvent.emit(self.file_data)

class Ui_Processing(QDialog):
    last_count = 0
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
        self.close_Btn = QPushButton('',self)
        self.close_Btn.setIcon(QIcon('.\\img\\close_Btn.png'))
        self.close_Btn.setFixedSize(20,20)
        self.close_Btn.setIconSize(QtCore.QSize(30,30))
        self.close_Btn.move(back.width()-40,20)
        self.close_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ### GIF set
        self.moviee = QLabel(self)
        self.movie = QtGui.QMovie(".\\img\\Processing.gif")
        self.moviee.setMovie(self.movie)
        self.moviee.setGeometry(50,28,320,150)
        self.movie.start()     

        ### Pause Button
        self.P_btn = QPushButton('',self)
        self.P_btn.setIcon(QIcon('.\\img\\Pause.png'))
        self.P_btn.setIconSize(QtCore.QSize(170,90))
        self.P_btn.setFixedSize(150,70)
        self.P_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.P_btn.move(420,60)

        ### Continue Button
        self.C_btn = QPushButton('',self)
        self.C_btn.setIcon(QIcon('.\\img\\Continue.png'))
        self.C_btn.setIconSize(QtCore.QSize(170,90))
        self.C_btn.setFixedSize(150,70)
        self.C_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.C_btn.move(420,60)

        ### Cancel Button
        self.Can_btn = QPushButton('',self)
        self.Can_btn.setIcon(QIcon('.\\img\\Cancel.png'))
        self.Can_btn.setIconSize(QtCore.QSize(170,90))
        self.Can_btn.setFixedSize(150,70)
        self.Can_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Can_btn.move(600,60)

        ### Start Button

        self.S_btn = QPushButton('',self)
        self.S_btn.setIcon(QIcon('.\\img\\Start.png'))
        self.S_btn.setIconSize(QtCore.QSize(170,90))
        self.S_btn.setFixedSize(150,70)
        self.S_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.S_btn.move(600,60)

        ### hide btn P & S
        self.C_btn.setVisible(False)
        self.S_btn.setVisible(False)

        ### Table Widget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setFixedSize(760, 370)
        self.tableWidget.move(30, 200)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, self.tableWidget.width()/5.5)
        self.tableWidget.setColumnWidth(1, self.tableWidget.width()/2.5)
        self.tableWidget.setColumnWidth(2, self.tableWidget.width()/2.5)
        

        ### Btn Clicked
        self.P_btn.clicked.connect(self.P_btn_clicked)
        self.C_btn.clicked.connect(self.C_btn_clicked)
        self.Can_btn.clicked.connect(self.Can_btn_clicked)
        self.S_btn.clicked.connect(self.S_btn_clicked)
        self.close_Btn.clicked.connect(self.close_Btn_clicked)

        self.show()

        self.gipThread = get_ip_thread(self)
        self.gipThread.gipEvent.connect(self.gipThreadEventHandler)
        self.gipThreadStart()


        #self.gregThread = get_registry_thread(self)
        #self.gregThread.gregEvent.connect(self.gregThreadEventHandler)
        #self.gregThreadStart()

        self.gprocThread = get_proc_thread(self)
        self.gprocThread.gprocEvent.connect(self.gprocThreadEventHandler)
        self.gprocThreadStart()


        self.gfileThread = get_file_thread(self)
        self.gfileThread.gfileEvent.connect(self.gfileThreadEventHandler)
        self.gfileThreadStart()

    @pyqtSlot()
    def gipThreadStart(self):
        self.gipThread.start()

    @pyqtSlot(list)
    def gipThreadEventHandler(self, ip_data):
        count = len(ip_data)
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnCount(3)
        global last_count
        i = 0
        for k in ip_data:
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Warning"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(""))
            i = i + 1
            self.last_count = i
        

    @pyqtSlot()
    def gregThreadStart(self):
        self.gregThread.start()

    @pyqtSlot(list)
    def gregThreadEventHandler(self, reg_data):
        count = len(reg_data)
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnCount(3)
        i = self.last_count
        for reg_k in reg_data:
            print(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Warning"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(reg_k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(""))
            i = i + 1
            print(i)
            self.last_count = i

    @pyqtSlot()
    def gprocThreadStart(self):
        self.gprocThread.start()

    @pyqtSlot(dict)
    def gprocThreadEventHandler(self, proc_data):
        count = len(proc_data)
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnCount(3)
        i = self.last_count

        for proc_k in proc_data.keys():
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Warning"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(proc_k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(proc_data[proc_k]))
            i = i + 1
            self.last_count = i


    @pyqtSlot()
    def gfileThreadStart(self):
        self.gfileThread.start()

    @pyqtSlot(dict)
    def gfileThreadEventHandler(self, file_data):
        count = len(file_data)
        self.tableWidget.setRowCount(count)
        self.tableWidget.setColumnCount(3)
        i = self.last_count

        for k in file_data.keys():
            if file_data[k] == "":
                self.tableWidget.setItem(i, 0, QTableWidgetItem("Info"))
            else:
                self.tableWidget.setItem(i, 0, QTableWidgetItem("Warning"))

            self.tableWidget.setItem(i, 1, QTableWidgetItem(k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(file_data[k]))
            i = i + 1
            self.last_count = i

       ### clicked btn event show and hide
    def P_btn_clicked(self):
        self.P_btn.setVisible(False)
        self.C_btn.setVisible(True)
        self.movie.stop()     

    def C_btn_clicked(self):
        self.C_btn.setVisible(False)
        self.P_btn.setVisible(True)
        self.movie.start()     

    def Can_btn_clicked(self):
        self.Can_btn.setVisible(False)
        self.S_btn.setVisible(True)
        self.P_btn.setVisible(False)
        self.C_btn.setVisible(False)
        self.movie.stop()     

    def S_btn_clicked(self):
        self.S_btn.setVisible(False)
        self.P_btn.setVisible(True)
        self.C_btn.setVisible(False)
        self.Can_btn.setVisible(True)
        self.movie.start()     

    ### Close_Btn_clicked = Go Tray or Exit
    def close_Btn_clicked(self):

        self.UI = GoTrayUI()
        self.UI.show()

###    def search completed then open Completed GUI
###        self.hide()
#          self.UI = Ui_completed()
###        UI.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = Ui_Processing()
    sys.exit(app.exec_())
