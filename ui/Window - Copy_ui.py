# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p:\API\GUI\ui\Window - Copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 656)
        MainWindow.setStyleSheet("#icon_only_widget {\n"
"        background-color: #313a46;\n"
"        width:50px;\n"
"    }\n"
"#full_menu_widget {\n"
"        background-color: #313a46;\n"
"    }\n"
"#full_menu_widget QPushButton,#label_2 {\n"
"        border:none;\n"
"        text-align: left;\n"
"        color: #ffffff;\n"
"    }\n"
"#full_menu_widget QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }\n"
"\n"
"    #full_menu_widget QPushButton:checked {\n"
"        color: #fff;\n"
"    }\n"
"#logo_label_2 {\n"
"        color: #fff;\n"
"    }\n"
"#change_btn {\n"
"        padding: 5px;\n"
"        border: none;\n"
"        width: 30px;\n"
"        height: 30px;\n"
"    }\n"
"#search_input {\n"
"        border: none;\n"
"        padding: 5px 10px;\n"
"    }\n"
"\n"
"    #search_input:focus {\n"
"        background-color: #70B9FE;\n"
"    }\n"
"#user_btn {\n"
"        border: none;\n"
"    }\n"
"    #search_btn {\n"
"        border: none;\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setMaximumSize(QtCore.QSize(30, 16777215))
        self.icon_only_widget.setStyleSheet("")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout.setContentsMargins(0, 0, 5, 0)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMaximumSize(QtCore.QSize(20, 20))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/home-2.ico"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.verticalLayout.addWidget(self.logo_label_1)
        self.pushButton = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.icon_only_widget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setText("")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 381, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(110, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(150, 16777215))
        self.scrollArea.setStyleSheet("border: none;\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.full_menu_widget = QtWidgets.QWidget()
        self.full_menu_widget.setGeometry(QtCore.QRect(0, 0, 150, 656))
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.full_menu_widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icon/icon/home-1.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.logo_label_2 = QtWidgets.QLabel(self.widget_2)
        self.logo_label_2.setMinimumSize(QtCore.QSize(20, 20))
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout.addWidget(self.logo_label_2)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.full_menu_widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/icon/home-2.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.menu_facebook = QtWidgets.QWidget(self.full_menu_widget)
        self.menu_facebook.setObjectName("menu_facebook")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_facebook)
        self.verticalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Account_Manger_face = QtWidgets.QPushButton(self.menu_facebook)
        self.Account_Manger_face.setObjectName("Account_Manger_face")
        self.verticalLayout_2.addWidget(self.Account_Manger_face)
        self.Account_Edit_face = QtWidgets.QPushButton(self.menu_facebook)
        self.Account_Edit_face.setObjectName("Account_Edit_face")
        self.verticalLayout_2.addWidget(self.Account_Edit_face)
        self.Account_Generat_face = QtWidgets.QPushButton(self.menu_facebook)
        self.Account_Generat_face.setObjectName("Account_Generat_face")
        self.verticalLayout_2.addWidget(self.Account_Generat_face)
        self.Accept_Friend = QtWidgets.QPushButton(self.menu_facebook)
        self.Accept_Friend.setObjectName("Accept_Friend")
        self.verticalLayout_2.addWidget(self.Accept_Friend)
        self.Add_Friend = QtWidgets.QPushButton(self.menu_facebook)
        self.Add_Friend.setObjectName("Add_Friend")
        self.verticalLayout_2.addWidget(self.Add_Friend)
        self.Join_Groub = QtWidgets.QPushButton(self.menu_facebook)
        self.Join_Groub.setObjectName("Join_Groub")
        self.verticalLayout_2.addWidget(self.Join_Groub)
        self.Follow_face = QtWidgets.QPushButton(self.menu_facebook)
        self.Follow_face.setObjectName("Follow_face")
        self.verticalLayout_2.addWidget(self.Follow_face)
        self.Like_face = QtWidgets.QPushButton(self.menu_facebook)
        self.Like_face.setObjectName("Like_face")
        self.verticalLayout_2.addWidget(self.Like_face)
        self.Share = QtWidgets.QPushButton(self.menu_facebook)
        self.Share.setObjectName("Share")
        self.verticalLayout_2.addWidget(self.Share)
        self.verticalLayout_4.addWidget(self.menu_facebook)
        self.widget_5 = QtWidgets.QWidget(self.full_menu_widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setMinimumSize(QtCore.QSize(20, 20))
        self.label_3.setMaximumSize(QtCore.QSize(20, 20))
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/icon/home-2.ico"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_8.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setChecked(False)
        self.pushButton_8.setAutoExclusive(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.menu_insta = QtWidgets.QWidget(self.full_menu_widget)
        self.menu_insta.setObjectName("menu_insta")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_insta)
        self.verticalLayout_3.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Account_Manger_insta = QtWidgets.QPushButton(self.menu_insta)
        self.Account_Manger_insta.setObjectName("Account_Manger_insta")
        self.verticalLayout_3.addWidget(self.Account_Manger_insta)
        self.Account_Edit_insta = QtWidgets.QPushButton(self.menu_insta)
        self.Account_Edit_insta.setObjectName("Account_Edit_insta")
        self.verticalLayout_3.addWidget(self.Account_Edit_insta)
        self.Account_Generat_insta = QtWidgets.QPushButton(self.menu_insta)
        self.Account_Generat_insta.setObjectName("Account_Generat_insta")
        self.verticalLayout_3.addWidget(self.Account_Generat_insta)
        self.verticalLayout_4.addWidget(self.menu_insta)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.scrollArea.setWidget(self.full_menu_widget)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.main_widget)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.widget_4 = QtWidgets.QWidget(self.splitter)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.change_btn.setIcon(icon2)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_5.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_6.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget)
        self.search_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_6.addWidget(self.search_btn)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.user_btn = QtWidgets.QPushButton(self.widget)
        self.user_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon4)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_5.addWidget(self.user_btn)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.widget_4)
        self.tabWidget.setStyleSheet("#tabWidget {\n"
"    background-color: rgb(255, 0, 0);\n"
"    \n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    margin-left: 3px;\n"
"    image:  url(:/icon/icon/x-mark-1.ico)\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    \n"
"    image: url(:/icon/icon/x-mark-2.ico)\n"
"}\n"
"QTabBar::tab  {\n"
"                background: white;\n"
"                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f6f6f6, stop:1 #e0e0e0);\n"
"                border: solid #0066cc 2px;\n"
"                border-radius: 50px 50px 50px 50px;\n"
"                padding: 8px 16px;\n"
"                margin-right: 4px;\n"
"\n"
"                \n"
"}\n"
"QTabBar::tab:selected {\n"
"                background: white;\n"
"                border-color: #ccc;\n"
"                border-radius: 33px 34px 0px 0px;\n"
"border: solid #0066cc 2px;\n"
"            }")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.widget_information = QtWidgets.QWidget(self.splitter)
        self.widget_information.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_information.setMaximumSize(QtCore.QSize(16777215, 200))
        self.widget_information.setTabletTracking(False)
        self.widget_information.setAcceptDrops(False)
        self.widget_information.setObjectName("widget_information")
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.main_widget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        self.pushButton_3.toggled['bool'].connect(self.menu_facebook.setHidden) # type: ignore
        self.pushButton_8.toggled['bool'].connect(self.menu_insta.setHidden) # type: ignore
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.scrollArea.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_2.setText(_translate("MainWindow", "Dashbord"))
        self.pushButton_3.setText(_translate("MainWindow", "FACEBOOK"))
        self.Account_Manger_face.setText(_translate("MainWindow", "Account Manger"))
        self.Account_Edit_face.setText(_translate("MainWindow", "Account Edit"))
        self.Account_Generat_face.setText(_translate("MainWindow", "Account Generat"))
        self.Accept_Friend.setText(_translate("MainWindow", "Accept Frind"))
        self.Add_Friend.setText(_translate("MainWindow", "Add Friend"))
        self.Join_Groub.setText(_translate("MainWindow", "Join Groub"))
        self.Follow_face.setText(_translate("MainWindow", "Follow"))
        self.Like_face.setText(_translate("MainWindow", "Like"))
        self.Share.setText(_translate("MainWindow", "Share"))
        self.pushButton_8.setText(_translate("MainWindow", "INSTGRAM"))
        self.Account_Manger_insta.setText(_translate("MainWindow", "Account Manger"))
        self.Account_Edit_insta.setText(_translate("MainWindow", "Account Edit"))
        self.Account_Generat_insta.setText(_translate("MainWindow", "Account Generat"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
import resource_rc
