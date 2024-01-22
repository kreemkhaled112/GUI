from PyQt6.QtWidgets import QApplication, QMainWindow 

from ui.Window_ui import Ui_MainWindow

from pages_functions.facebook.Manger_Face import Manger_Face
from pages_functions.facebook.Generat_Face import Generat_Face
from pages_functions.facebook.Generat_Face import Generat_Face
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## =======================================================================================================
        ## Get all the objects in windows
        ## =======================================================================================================
        self.Account_Generat_face = self.ui.Account_Generat_face
        self.Account_Manger_face = self.ui.Account_Manger_face 
        self.Accept_Friend = self.ui.Accept_Friend
        self.Add_Friend = self.ui.Add_Friend
        self.Join_Groub = self.ui.Join_Groub
        self.Follow_face = self.ui.Follow_face
        self.Like_face = self.ui.Like_face
        self.Account_Manger_insta = self.ui.Account_Manger_insta
        self.Account_Edit_insta = self.ui.Account_Edit_insta
        self.Account_Generat_insta = self.ui.Account_Generat_insta

        ## =======================================================================================================
        ## Create dict for menu buttons and tab windows
        ## =======================================================================================================
        self.menu_btns_list = {
            self.Account_Manger_face: Manger_Face(),
            self.Account_Generat_face: Generat_Face(),
            self.Accept_Friend: Accept_Friend(),
            self.Add_Friend: Add_Friend(),
            self.Join_Groub: Join_Groub(),
            self.Follow_f: Mazda(),
            self.Like_f: Tumbr(),
            self.Account_Manger_i: Tumbr(),
            self.Account_Edit_i: Tumbr(),
            self.Account_Generat_i: Tumbr(),
        }

        ## =======================================================================================================
        ## Show home window when start app
        ## =======================================================================================================
        self.show_home_window()

        ## =======================================================================================================
        ## Connect signal and slot
        ## =======================================================================================================
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.home_btn.clicked.connect(self.show_selected_window)
        self.dashboard_btn.clicked.connect(self.show_selected_window)
        self.toyota_btn.clicked.connect(self.show_selected_window)
        self.lexus_btn.clicked.connect(self.show_selected_window)
        self.mazda_btn.clicked.connect(self.show_selected_window)
        self.youtube_btn.clicked.connect(self.show_selected_window)
        self.tumbr_btn.clicked.connect(self.show_selected_window)

    def show_home_window(self):
        """
        Function for showing home window
        :return:
        """
        result = self.open_tab_flag(self.home_btn.text())
        self.set_btn_checked(self.home_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.home_btn.text()
            curIndex = self.ui.tabWidget.addTab(Manger(), title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def show_selected_window(self):
        """
        Function for showing selected window
        :return:
        """
        button = self.sender()

        result = self.open_tab_flag(button.text())
        self.set_btn_checked(button)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_list[button], title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self, index):
        """
        Function for close tab in tabWidget
        :param index: index of tab
        :return:
        """
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() == 0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_home_window()

    def open_tab_flag(self, tab):
        """
        Check if selected window showed or not
        :param tab: tab title
        :return: bool and index
        """
        open_tab_count = self.ui.tabWidget.count()

        for i in range(open_tab_count):
            tab_name = self.ui.tabWidget.tabText(i)
            if tab_name == tab:
                return True, i
            else:
                continue

        return False,

    def set_btn_checked(self, btn):
        """
        Set the status of selected button checked and set other buttons' status unchecked
        :param btn: button object
        :return:
        """
        for button in self.menu_btns_list.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)


if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
