import sys
import core
import conn
import pythoncom

from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication, QPushButton, QDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap, QIcon
from collections import OrderedDict
import GotoTray

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

class send_report_thread(QThread):
    countEvent = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent
        self.count = 4
        self._status = True

    def run(self):
        while self._status:
            if self.count <= 0:
                self._status = False
                self.countEvent.emit(self.count)
            else:
                self.msleep(1000)

class Ui_Processing(QDialog):
    last_count = 0
    count = 0
    report = OrderedDict()

    def __init__(self, id ):
        self.user_id = id

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

        ### Table Widget Label Warning, Notice set
        self.warn = QLabel(self)
        self.warn_img = QPixmap('.\\img\\Warning.png')
        self.Notice = QLabel(self)
        self.Notice_img = QPixmap('.\\img\\Notice.png') 

        ### Btn Clicked
        self.P_btn.clicked.connect(self.P_btn_clicked)
        self.C_btn.clicked.connect(self.C_btn_clicked)
        self.Can_btn.clicked.connect(self.Can_btn_clicked)
        self.S_btn.clicked.connect(self.S_btn_clicked)
        self.close_Btn.clicked.connect(self.close_Btn_clicked)

        self.show()

        ### core thread
        self.gipThread = get_ip_thread(self)
        self.gipThread.gipEvent.connect(self.gipThreadEventHandler)
        self.gipThreadStart()

        self.gregThread = get_registry_thread(self)
        self.gregThread.gregEvent.connect(self.gregThreadEventHandler)
        self.gregThreadStart()

        self.gprocThread = get_proc_thread(self)
        self.gprocThread.gprocEvent.connect(self.gprocThreadEventHandler)
        self.gprocThreadStart()

        self.gfileThread = get_file_thread(self)
        self.gfileThread.gfileEvent.connect(self.gfileThreadEventHandler)
        self.gfileThreadStart()

        ### report thread
        self.reportThread = send_report_thread(self)
        self.reportThread.countEvent.connect(self.reportThreadEventHandler)
        self.reportThreadStart()

    @pyqtSlot()
    def gipThreadStart(self):
        self.gipThread.start()

    @pyqtSlot(list)
    def gipThreadEventHandler(self, ip_data):
        self.count += self.last_count
        self.count += len(ip_data)
        self.tableWidget.setRowCount(self.count)
        self.tableWidget.setColumnCount(3)

        i = self.last_count
        self.report["ip"] = ip_data

        for k in ip_data:
            self.Notice.setPixmap(self.Notice_img)
            self.tableWidget.setCellWidget(i,0,self.Notice)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(""))
            i = i + 1
            self.last_count = i

        self.reportThread.count -= 1

    @pyqtSlot()
    def gregThreadStart(self):
        self.gregThread.start()

    @pyqtSlot(list)
    def gregThreadEventHandler(self, reg_data):
        self.count += self.last_count
        self.count += len(reg_data) -1

        self.tableWidget.setRowCount(self.count)
        self.tableWidget.setColumnCount(3)

        i = self.last_count
        self.report["registry"] = reg_data

        for reg_k in reg_data:
            self.Notice.setPixmap(self.Notice_img)
            self.tableWidget.setCellWidget(i,0,self.Notice)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(reg_k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(""))
            i = i + 1
            self.last_count = i

        self.reportThread.count -= 1

    @pyqtSlot()
    def gprocThreadStart(self):
        self.gprocThread.start()

    @pyqtSlot(dict)
    def gprocThreadEventHandler(self, proc_data):
        self.count += self.last_count
        self.count += len(proc_data) -1

        self.tableWidget.setRowCount(self.count)
        self.tableWidget.setColumnCount(3)

        i = self.last_count
        self.report["process"] = proc_data

        for proc_k in proc_data.keys():
            self.Notice.setPixmap(self.Notice_img)
            self.tableWidget.setCellWidget(i,0,self.Notice)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(proc_k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(proc_data[proc_k]))
            i = i + 1
            self.last_count = i

        self.reportThread.count -= 1

    @pyqtSlot()
    def gfileThreadStart(self):
        self.gfileThread.start()

    @pyqtSlot(dict)
    def gfileThreadEventHandler(self, file_data):
        self.count += self.last_count
        self.count += len(file_data) -2
        
        self.tableWidget.setRowCount(self.count)
        self.tableWidget.setColumnCount(3)

        i = self.last_count
        self.report["file"] = file_data

        for k in file_data.keys():
            if file_data[k] == "":
                ### Table widget - info Label
                self.warn = QLabel(self)
                self.warn_img = QPixmap('.\\img\\Warning.png')
                self.warn.setPixmap(self.warn_img)
                self.tableWidget.setCellWidget(i,0,self.warn)

            else:
                ### Table widget - Warn Label
                self.Notice = QLabel(self)
                self.Notice_img = QPixmap('.\\img\\Notice.png') 
                self.Notice.setPixmap(self.Notice_img)
                self.tableWidget.setCellWidget(i,0,self.Notice)

            self.tableWidget.setItem(i, 1, QTableWidgetItem(k))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(file_data[k]))
            i = i + 1
            self.last_count = i
        self.reportThread.count -= 1

    @pyqtSlot()
    def reportThreadStart(self):
        self.reportThread.start()

    @pyqtSlot(int)
    def reportThreadEventHandler(self, count):
        if count <= 0:
            complete_report = conn.make_format(self.user_id, self.report)
            conn.send_report(complete_report)

            self.P_btn.setVisible(False)
            self.S_btn.setVisible(True)
            self.movie.stop()

            conn.web_open()

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

        self.UI = GotoTray.GoTrayUI()
        self.UI.show()
        self.proc_self = self
        GotoTray.proc_self = self.proc_self

    ### MousePressEvent & MouseMoveEvent = drag window
    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = Ui_Processing()


    sys.exit(app.exec_())
