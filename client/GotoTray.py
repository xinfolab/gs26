import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QCheckBox, QSystemTrayIcon,QDialog, QMenu, QAction, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
 
proc_self = 0

class GoTrayUI(QDialog):
 
    def __init__(self):

        super().__init__()
        self.GotoTrayUI()

    def GotoTrayUI(self):

        ### Font configure
        font = QtGui.QFont()
        font.setBold(True)

        ### remove title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnBottomHint)

        ### background image and Fixed Size
        back_label = QLabel(self)
        back_label.setGeometry(QtCore.QRect(2,2,400,250))
        back = QPixmap('.\\img\\33_back.png')
        back_label.setPixmap(back)
        
        ### close Button ( check box checked = go tray )
        Close_btn = QPushButton('',self)
        Close_btn.setIcon(QIcon('.\\img\\Close_btn.png'))
        Close_btn.setFixedSize(20,20)
        Close_btn.setIconSize(QtCore.QSize(30,30))
        Close_btn.move(360,20)
        Close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ### check box ( checked = go tray | non_checked = exit )
        self.check_box = QCheckBox("Tray Icon으로 보내시겠습니까?",self)
        self.check_box.setFont(font)
        self.check_box.setStyleSheet("color : white")

        self.check_box.move(80,80)
        self.check_box.resize(300,50)

        ### Exit Button ( check box checked = go tray )
        Exit_btn = QPushButton('',self)
        Exit_btn.setText('종료')
        Exit_btn.setFixedSize(80,40)
        Exit_btn.move(100,160)
        Exit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        ### Cancel Button
        Cancel_btn = QPushButton('',self)
        Cancel_btn.setText('취소')
        Cancel_btn.setFixedSize(80,40)
        Cancel_btn.move(240,160)
        Cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # TrayIcon Setting
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('.\\img\\Icon.png'))
        show_action = QAction("실행", self)
        quit_action = QAction("종료", self)
        self.tray_icon.show()

        ### Tray Icon menu - 실행 - show process_UI
        show_action.triggered.connect(self.active_tray)
        ### Tray Icon menu - 종료 - exit
        quit_action.triggered.connect(QApplication.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        Cancel_btn.clicked.connect(self.hide)
        Close_btn.clicked.connect(self.closeEvent)
        Exit_btn.clicked.connect(self.closeEvent)
        self.show()
    
    ### Check box Click 에 대한.
    def closeEvent(self):
        if self.check_box.isChecked():
            self.hide()
            ### processing UI hide set
            self = proc_self
            self.hide()
        else:
            exit()
    def active_tray(self):
        self = proc_self
        self.show()
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    UI = GoTrayUI()
    sys.exit(app.exec())
