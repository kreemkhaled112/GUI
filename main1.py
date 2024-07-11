from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint
from ui.sidebar_ui import Ui_MainWindow
import uuid , requests , ntplib , sys
from datetime import datetime, date
from pages_functions.Facebook.Manger_Face import Manager_Face
from pages_functions.Facebook.Edit_Face import Edit_Face
from pages_functions.Facebook.User import User
from pages_functions.Facebook.Post import Post
from pages_functions.Facebook.Follow import Follow
from pages_functions.Facebook.Like import Like
from pages_functions.Facebook.Share import Share
from pages_functions.Facebook.Comment import Comment
from pages_functions.Facebook.Report import Report

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.mac = ':'.join(['{:02x}'.format((uuid.getnode() >> 8 * i) & 0xff)for i in range(5, -1, -1)  ])
        self.ui.Profile.setText(self.mac)
        self.ui.Profile.clicked.connect(lambda : QApplication.clipboard().setText(self.ui.Profile.text()))

        
        self.ui.stackedWidget.insertWidget(0, Manager_Face())
        self.ui.stackedWidget.insertWidget(1, Edit_Face())
        self.ui.stackedWidget.insertWidget(2, User())
        self.ui.stackedWidget.insertWidget(3, Post())
        self.ui.stackedWidget.insertWidget(4, Follow())
        self.ui.stackedWidget.insertWidget(5, Like())
        self.ui.stackedWidget.insertWidget(6, Share())
        self.ui.stackedWidget.insertWidget(7, Comment())
        self.ui.widget_order.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home.setChecked(True)

        self.old_pos = self.pos()
        self.ui.close.clicked.connect(self.close)
        self.ui.maximize.clicked.connect(self.toggle_maximize_restore)
        self.ui.minimize.clicked.connect(self.showMinimized)

    ## Change QPushButton Checkable status when stackedWidget index changed
    # def on_stackedWidget_currentChanged(self, index):
    #     btn_list = self.ui.full_menu_widget.findChildren(QPushButton)
        
    #     for btn in btn_list:
    #         if index in [5, 6]:
    #             btn.setAutoExclusive(False)
    #             btn.setChecked(False)
    #         else:
    #             btn.setAutoExclusive(True)
    ## functions for changing menu page
    def on_home_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_Accound_edt_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_User_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_Post_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_Follow_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    def on_Like_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    def on_Shar_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    def on_Comment_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

    def toggle_maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())



