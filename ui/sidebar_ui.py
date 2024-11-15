# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p:\API\GUI\ui\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 516)
        MainWindow.setStyleSheet("\n"
"#MainWindow {\n"
"        background-color: #ffffff;\n"
"    }\n"
"#stackedWidget {\n"
"        background-color:#ffffff;\n"
"        border-top-left-radius:16px;\n"
"        padding:16px 31px;\n"
"    }\n"
"    \n"
"#full_menu_widget ,#widget_main,#frame_1{\n"
"        background-color: #313a46;\n"
"    }\n"
"    \n"
"#full_menu_widget QPushButton {\n"
"    background-color: #313a46;\n"
"    border:none;\n"
"    border-radius: 3px;\n"
"    text-align: left;\n"
"    padding: 8px 0 8px 15px;\n"
"    color: #788596;\n"
"}\n"
"\n"
"#full_menu_widget QPushButton:hover {\n"
"    background-color: rgba( 86, 101, 115, 0.5);\n"
"}\n"
"\n"
"#widget_5 QPushButton:checked {\n"
"    background-color: #fff;\n"
"    border-bottom-right-radius:28px;\n"
"    border-top-right-radius:28px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"        color: rgb(0, 0, 0);\n"
"        border: 2px solid gray;\n"
"        border-radius: 5px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    color: white;\n"
"    padding: 8px 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #ffffff;\n"
"    border: 0px 2px 2px 0 solid #8f8f8f; \n"
"}\n"
"\n"
"QTableWidget QHeaderView::section:horizontal {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QTableWidget::item:nth-child {\n"
"    background-color:transparent;\n"
"    color:#000000;\n"
"}\n"
"QTableWidget::item:hover {\n"
"    background-color: #3ea6ff; \n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #3ea6ff; \n"
"}\n"
"QTableWidget QHeaderView {\n"
"    color: #ffffff;\n"
"    background-color:#8f8f8f;\n"
"    border-bottom: solid 2px #d8d8d8;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    width: 7px;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #888;\n"
"    min-height: 40px;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_main = QtWidgets.QWidget(self.centralwidget)
        self.widget_main.setStyleSheet("")
        self.widget_main.setObjectName("widget_main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_main)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.full_menu_widget = QtWidgets.QWidget(self.widget_main)
        self.full_menu_widget.setStyleSheet("")
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(5, 12, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.full_menu_widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Home = QtWidgets.QPushButton(self.widget_5)
        self.Home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Home.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home.setIcon(icon)
        self.Home.setIconSize(QtCore.QSize(14, 14))
        self.Home.setCheckable(True)
        self.Home.setChecked(True)
        self.Home.setAutoExclusive(True)
        self.Home.setObjectName("Home")
        self.verticalLayout_2.addWidget(self.Home)
        self.Accound_edt = QtWidgets.QPushButton(self.widget_5)
        self.Accound_edt.setMinimumSize(QtCore.QSize(100, 0))
        self.Accound_edt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Accound_edt.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Accound_edt.setIcon(icon1)
        self.Accound_edt.setIconSize(QtCore.QSize(14, 14))
        self.Accound_edt.setCheckable(True)
        self.Accound_edt.setAutoExclusive(True)
        self.Accound_edt.setObjectName("Accound_edt")
        self.verticalLayout_2.addWidget(self.Accound_edt)
        self.User = QtWidgets.QPushButton(self.widget_5)
        self.User.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/group-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.User.setIcon(icon2)
        self.User.setIconSize(QtCore.QSize(14, 14))
        self.User.setCheckable(True)
        self.User.setAutoExclusive(True)
        self.User.setObjectName("User")
        self.verticalLayout_2.addWidget(self.User)
        self.Post = QtWidgets.QPushButton(self.widget_5)
        self.Post.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Post.setIcon(icon3)
        self.Post.setIconSize(QtCore.QSize(14, 14))
        self.Post.setCheckable(True)
        self.Post.setAutoExclusive(True)
        self.Post.setObjectName("Post")
        self.verticalLayout_2.addWidget(self.Post)
        self.Order = QtWidgets.QPushButton(self.widget_5)
        self.Order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/product-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Order.setIcon(icon4)
        self.Order.setIconSize(QtCore.QSize(14, 14))
        self.Order.setCheckable(True)
        self.Order.setAutoExclusive(True)
        self.Order.setObjectName("Order")
        self.verticalLayout_2.addWidget(self.Order)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_order = QtWidgets.QWidget(self.full_menu_widget)
        self.widget_order.setObjectName("widget_order")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_order)
        self.verticalLayout_6.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Follow = QtWidgets.QPushButton(self.widget_order)
        self.Follow.setCheckable(True)
        self.Follow.setObjectName("Follow")
        self.verticalLayout_6.addWidget(self.Follow)
        self.Like = QtWidgets.QPushButton(self.widget_order)
        self.Like.setCheckable(True)
        self.Like.setObjectName("Like")
        self.verticalLayout_6.addWidget(self.Like)
        self.Shar = QtWidgets.QPushButton(self.widget_order)
        self.Shar.setCheckable(True)
        self.Shar.setObjectName("Shar")
        self.verticalLayout_6.addWidget(self.Shar)
        self.Comment = QtWidgets.QPushButton(self.widget_order)
        self.Comment.setCheckable(True)
        self.Comment.setObjectName("Comment")
        self.verticalLayout_6.addWidget(self.Comment)
        self.verticalLayout_4.addWidget(self.widget_order)
        spacerItem = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Profile = QtWidgets.QPushButton(self.full_menu_widget)
        self.Profile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/moderator-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Profile.setIcon(icon5)
        self.Profile.setCheckable(True)
        self.Profile.setObjectName("Profile")
        self.verticalLayout_3.addWidget(self.Profile)
        self.Setting = QtWidgets.QPushButton(self.full_menu_widget)
        self.Setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/gear-2-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Setting.setIcon(icon6)
        self.Setting.setCheckable(True)
        self.Setting.setObjectName("Setting")
        self.verticalLayout_3.addWidget(self.Setting)
        self.Help = QtWidgets.QPushButton(self.full_menu_widget)
        self.Help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Help.setIcon(icon7)
        self.Help.setIconSize(QtCore.QSize(14, 14))
        self.Help.setCheckable(True)
        self.Help.setObjectName("Help")
        self.verticalLayout_3.addWidget(self.Help)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addWidget(self.full_menu_widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_main)
        self.stackedWidget.setStyleSheet("QPushButton {\n"
"  border-radius: 10px;\n"
"  border: 2px solid #8f8f8f;\n"
"  padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #E1F4FA;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #007BFF;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_profile = QtWidgets.QWidget()
        self.page_profile.setAutoFillBackground(False)
        self.page_profile.setObjectName("page_profile")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.page_profile)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_2 = QtWidgets.QWidget(self.page_profile)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_name = QtWidgets.QLabel(self.widget_2)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_5.addWidget(self.label_name, 0, QtCore.Qt.AlignHCenter)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.copy = QtWidgets.QPushButton(self.widget_4)
        self.copy.setCheckable(True)
        self.copy.setObjectName("copy")
        self.horizontalLayout_4.addWidget(self.copy)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_2.setStyleSheet("border: none;")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.gridLayout_13.addWidget(self.widget_2, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_profile)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_setting)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_19 = QtWidgets.QWidget(self.page_setting)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_19)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_6 = QtWidgets.QWidget(self.widget_19)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.widget_7)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_4.setStyleSheet("background-color: #8f8f8f;\n"
"border-radius: 10px;\n"
"border: 2px solid #8f8f8f;\n"
"padding: 5px;")
        self.pushButton_4.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.verticalLayout_8.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget_9)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.widget_9)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout_7.addWidget(self.widget_9)
        self.verticalLayout_8.addWidget(self.widget_8, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_13.addWidget(self.widget_6)
        self.widget_10 = QtWidgets.QWidget(self.widget_19)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        self.widget_11.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget_11)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_11)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setStyleSheet("background-color: #8f8f8f;\n"
"border-radius: 10px;\n"
"border: 2px solid #8f8f8f;\n"
"padding: 5px;")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_9.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(self.widget_10)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_13 = QtWidgets.QWidget(self.widget_12)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.widget_13)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_13)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_8.addWidget(self.spinBox_2)
        self.verticalLayout_10.addWidget(self.widget_13)
        self.verticalLayout_9.addWidget(self.widget_12, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_13.addWidget(self.widget_10)
        self.gridLayout_6.addWidget(self.widget_19, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.stackedWidget.addWidget(self.page_setting)
        self.page_help = QtWidgets.QWidget()
        self.page_help.setObjectName("page_help")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_help)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget_14 = QtWidgets.QWidget(self.page_help)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.widget_17 = QtWidgets.QWidget(self.widget_14)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.widget_17)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_6.setStyleSheet("background-color: #8f8f8f;\n"
"border-radius: 10px;\n"
"border: 2px solid #8f8f8f;\n"
"padding: 5px;")
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(14, 14))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_11.addWidget(self.pushButton_6)
        self.verticalLayout_12.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.widget_14)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textEdit = QtWidgets.QTextEdit(self.widget_18)
        self.textEdit.setStyleSheet("border: none;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_11.addWidget(self.textEdit)
        self.verticalLayout_12.addWidget(self.widget_18)
        self.gridLayout_12.addWidget(self.widget_14, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.widget_15 = QtWidgets.QWidget(self.page_help)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.widget_15)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.widget_16 = QtWidgets.QWidget(self.widget_15)
        self.widget_16.setStyleSheet("QPushButton {\n"
"  border: none;\n"
"}")
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_3.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icon/icon/telegram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icon/icon/whatsapp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_16)
        self.pushButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icon/icon/facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon11)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.horizontalLayout_10.addWidget(self.widget_16, 0, QtCore.Qt.AlignRight)
        self.gridLayout_12.addWidget(self.widget_15, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.stackedWidget.addWidget(self.page_help)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_main, 1, 0, 1, 1)
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_1.setStyleSheet("")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_3.setContentsMargins(-1, 7, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_4 = QtWidgets.QLabel(self.frame_1)
        self.logo_label_4.setMinimumSize(QtCore.QSize(20, 20))
        self.logo_label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.logo_label_4.setText("")
        self.logo_label_4.setPixmap(QtGui.QPixmap(":/icon/icon/facebook.png"))
        self.logo_label_4.setScaledContents(True)
        self.logo_label_4.setWordWrap(False)
        self.logo_label_4.setObjectName("logo_label_4")
        self.horizontalLayout_3.addWidget(self.logo_label_4)
        self.logo_label_5 = QtWidgets.QLabel(self.frame_1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.logo_label_5.setFont(font)
        self.logo_label_5.setStyleSheet("color: #fff;")
        self.logo_label_5.setObjectName("logo_label_5")
        self.horizontalLayout_3.addWidget(self.logo_label_5)
        self.widget = QtWidgets.QWidget(self.frame_1)
        self.widget.setStyleSheet("QPushButton {\n"
"  border: none;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimize = QtWidgets.QPushButton(self.widget)
        self.minimize.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icon/icon/minimize-window-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize.setIcon(icon12)
        self.minimize.setCheckable(True)
        self.minimize.setFlat(True)
        self.minimize.setObjectName("minimize")
        self.horizontalLayout.addWidget(self.minimize)
        self.maximize = QtWidgets.QPushButton(self.widget)
        self.maximize.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icon/icon/maximize-window-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize.setIcon(icon13)
        self.maximize.setCheckable(True)
        self.maximize.setAutoDefault(False)
        self.maximize.setFlat(True)
        self.maximize.setObjectName("maximize")
        self.horizontalLayout.addWidget(self.maximize)
        self.close = QtWidgets.QPushButton(self.widget)
        self.close.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icon/icon/x-mark-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon14)
        self.close.setCheckable(True)
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.horizontalLayout_3.addWidget(self.widget, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.frame_1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.Order.toggled['bool'].connect(self.widget_order.setVisible) # type: ignore
        self.pushButton_4.toggled['bool'].connect(self.widget_8.setVisible) # type: ignore
        self.pushButton_5.toggled['bool'].connect(self.widget_12.setVisible) # type: ignore
        self.pushButton_6.toggled['bool'].connect(self.widget_18.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home.setText(_translate("MainWindow", "Home"))
        self.Accound_edt.setText(_translate("MainWindow", "Account Edit"))
        self.User.setText(_translate("MainWindow", "User"))
        self.Post.setText(_translate("MainWindow", "Post"))
        self.Order.setText(_translate("MainWindow", "Order"))
        self.Follow.setText(_translate("MainWindow", "Follow"))
        self.Like.setText(_translate("MainWindow", "Like"))
        self.Shar.setText(_translate("MainWindow", "Share"))
        self.Comment.setText(_translate("MainWindow", "Comment"))
        self.Profile.setText(_translate("MainWindow", "Profile"))
        self.Setting.setText(_translate("MainWindow", "Setting"))
        self.Help.setText(_translate("MainWindow", "Help"))
        self.label_name.setText(_translate("MainWindow", "Welcome"))
        self.label_11.setText(_translate("MainWindow", "App Id"))
        self.copy.setText(_translate("MainWindow", "Copy"))
        self.label.setText(_translate("MainWindow", "Home"))
        self.label_2.setText(_translate("MainWindow", "Change Ip After  :"))
        self.label_4.setText(_translate("MainWindow", "Account Edit"))
        self.label_5.setText(_translate("MainWindow", "Change Ip After  :"))
        self.label_6.setText(_translate("MainWindow", "version : v1.0"))
        self.label_3.setText(_translate("MainWindow", "Contact"))
        self.logo_label_5.setText(_translate("MainWindow", "S M M"))
import resource_rc
