from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QPoint
from ui.main_ui import Ui_MainWindow
import uuid , requests , ntplib
from datetime import datetime, date
from pages_functions.Facebook.Manger_Face import Manager_Face
from pages_functions.Facebook.Edit_Face import Edit_Face
from pages_functions.Facebook.Generat_Face import Generat_Face
from pages_functions.Facebook.User import User
from pages_functions.Facebook.Post import Post
from pages_functions.Facebook.Follow import Follow
from pages_functions.Facebook.Like import Like
from pages_functions.Facebook.Share import Share
from pages_functions.Facebook.Report import Report

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.mac = ':'.join(['{:02x}'.format((uuid.getnode() >> 8 * i) & 0xff)for i in range(5, -1, -1)  ])
        self.ui.mac.setText(self.mac)
        self.ui.mac.clicked.connect(lambda : QApplication.clipboard().setText(self.ui.mac.text()))

        self.Account_Manger_face = self.ui.Account_Manger_face 
        self.Account_Edit_face = self.ui.Account_Edit_face
        self.Account_Generat_face = self.ui.Account_Generat_face
        self.User = self.ui.User
        self.Post = self.ui.Post
        self.Follow_face = self.ui.Follow_face
        self.Like_face = self.ui.Like_face
        self.Share_face = self.ui.Share_face

        self.menu_btns_list = {
            self.Account_Manger_face: Manager_Face(),
            self.Account_Edit_face: Edit_Face(),
            self.Account_Generat_face: Generat_Face(),
            self.User: User(),
            self.Post: Post(),
            self.Follow_face: Follow(),
            self.Like_face: Like(),
            self.Share_face: Share(),
        }

        self.show_home_window()
        self.ui.scrollArea.hide()
        self.ui.menu_facebook.hide()
        self.ui.Report_face.hide()
        
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.Account_Manger_face.clicked.connect(self.show_selected_window)
        self.Account_Edit_face.clicked.connect(self.show_selected_window)
        self.Account_Generat_face.clicked.connect(self.show_selected_window)
        self.User.clicked.connect(self.show_selected_window)
        self.Post.clicked.connect(self.show_selected_window)
        self.Follow_face.clicked.connect(self.show_selected_window)
        self.Like_face.clicked.connect(self.show_selected_window)
        self.Share_face.clicked.connect(self.show_selected_window)
        self.Active()
    def check_internet_connection(self):
        try:
            requests.get("http://www.google.com", timeout=10)
            return True
        except requests.RequestException:
            return False
    def get_data(self):
        response = requests.get("https://pastebin.com/raw/H72kttsG")
        if response.status_code == 200:
            data = response.json()
            for item in data:
                if  item["id"] == self.mac:
                    name = item["name"]
                    type = item["type"]
                    expiration_date = date.fromisoformat(item["expiration_date"])
                    return name , type , expiration_date
        return None, None , None
    def get_current_date(self):
        ntp_server = 'ntp2a.mcc.ac.uk' 
        client = ntplib.NTPClient()
        try:
            response = client.request(ntp_server, version=3)
            timestamp = response.tx_time
            current_date = datetime.fromtimestamp(timestamp).date()
            return current_date
        except ntplib.NTPException:
            return None
        except Exception as e:
            return None
    def Active(self):
        if not self.check_internet_connection():
            input("Please check your internet connection!") ; return
        name , type , expiration_date = self.get_data()
        if type:
            self.ui.mac.setText(name)
            current_date  = self.get_current_date()
            if type == "Full":     
                if current_date > expiration_date :
                    self.Account_Edit_face.hide()
                    self.Account_Generat_face.hide()
                    self.User.hide()
                    self.Post.hide()
                    self.Follow_face.hide()
                    self.Like_face.hide()
                    self.Share_face.hide()
                    self.ui.mac.setText('Expired')
            if type == "Server":
                if current_date > expiration_date :
                    self.ui.mac.setText('Expired')
                    self.Follow_face.hide()
                    self.Like_face.hide()
                    self.Share_face.hide()
                self.Account_Edit_face.hide()
                self.Account_Generat_face.hide()
                self.User.hide()
                self.Post.hide()
        else:
            self.Account_Edit_face.hide()
            self.Account_Generat_face.hide()
            self.User.hide()
            self.Post.hide()
            self.Follow_face.hide()
            self.Like_face.hide()
            self.Share_face.hide()
    def show_home_window(self):
        result = self.open_tab_flag(self.Account_Manger_face.objectName())
        self.set_btn_checked(self.Account_Manger_face)

        if result[0]: self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            title = self.Account_Manger_face.text()
            curIndex = self.ui.tabWidget.addTab(Manager_Face(), title)
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
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec())
