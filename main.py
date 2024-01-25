from PyQt5.QtWidgets import *

from ui.Window_ui import Ui_MainWindow

from pages_functions.Facebook.Manger_Face import Manger_Face
from pages_functions.Facebook.Edit_Face import Edit_Face
from pages_functions.Facebook.Generat_Face import Generat_Face
from pages_functions.Facebook.Accept import Accept
from pages_functions.Facebook.Friend import Friend
from pages_functions.Facebook.Join import Join
from pages_functions.Facebook.Follow import Follow
from pages_functions.Facebook.Like import Like
from pages_functions.Facebook.Share import Share
from pages_functions.Insta.Manger_Insta import Manger_Insta
from pages_functions.Insta.Edit_Insta import Edit_Insta
from pages_functions.Insta.Generat_Insta import Generat_Insta


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Account_Manger_face = self.ui.Account_Manger_face 
        self.Account_Edit_face = self.ui.Account_Edit_face
        self.Account_Generat_face = self.ui.Account_Generat_face
        self.Accept_Friend = self.ui.Accept_Friend
        self.Add_Friend = self.ui.Add_Friend
        self.Join_Groub = self.ui.Join_Groub
        self.Follow_face = self.ui.Follow_face
        self.Like_face = self.ui.Like_face
        self.Share = self.ui.Share
        self.Account_Manger_insta = self.ui.Account_Manger_insta
        self.Account_Edit_insta = self.ui.Account_Edit_insta
        self.Account_Generat_insta = self.ui.Account_Generat_insta

        ## Create dict for menu buttons and tab windows
        self.menu_btns_list = {
            self.Account_Manger_face: Manger_Face(),
            self.Account_Edit_face: Edit_Face(),
            self.Account_Generat_face: Generat_Face(),
            self.Accept_Friend: Accept(),
            self.Add_Friend: Friend(),
            self.Join_Groub: Join(),
            self.Follow_face: Follow(),
            self.Like_face: Like(),
            self.Share: Share(),
            self.Account_Manger_insta: Manger_Insta(),
            self.Account_Edit_insta: Edit_Insta(),
            self.Account_Generat_insta: Generat_Insta(),
        }

        # Show home window when start app
        self.show_home_window()
        self.ui.icon_only_widget.hide()

        # Connect signal and slot
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.Account_Manger_face.clicked.connect(self.show_selected_window)
        self.Account_Edit_face.clicked.connect(self.show_selected_window)
        self.Account_Generat_face.clicked.connect(self.show_selected_window)
        self.Accept_Friend.clicked.connect(self.show_selected_window)
        self.Add_Friend.clicked.connect(self.show_selected_window)
        self.Join_Groub.clicked.connect(self.show_selected_window)
        self.Follow_face.clicked.connect(self.show_selected_window)
        self.Like_face.clicked.connect(self.show_selected_window)
        self.Share.clicked.connect(self.show_selected_window)
        self.Account_Manger_insta.clicked.connect(self.show_selected_window)
        self.Account_Edit_insta.clicked.connect(self.show_selected_window)
        self.Account_Generat_insta.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        result = self.open_tab_flag(self.Account_Manger_face.objectName())
        self.set_btn_checked(self.Account_Manger_face)

        if result[0]: self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.Account_Manger_face.text()
            curIndex = self.ui.tabWidget.addTab(Manger_Face(), title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def show_selected_window(self):
        button = self.sender()

        result = self.open_tab_flag(button.objectName())
        self.set_btn_checked(button)

        if result[0]: self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):

        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            # self.ui.scrollArea.setCurrentIndex(0)
            self.show_home_window()

    def open_tab_flag(self, tab):
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
            else: continue
        return False,

    def set_btn_checked(self, btn):
        for button in self.menu_btns_list.keys():
            if button != btn: button.setChecked(False)
            else: button.setChecked(True)


if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
