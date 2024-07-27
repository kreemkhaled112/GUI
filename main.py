from pages_functions.__init__ import *
from ui.sidebar_ui import Ui_MainWindow
from pages_functions.Facebook.Manger_Face import Manager_Face
from pages_functions.Facebook.Edit_Face import Edit_Face
from pages_functions.Facebook.User import User
from pages_functions.Facebook.Post import Post
from pages_functions.Facebook.Follow import Follow
from pages_functions.Facebook.Like import Like
from pages_functions.Facebook.Share import Share
from pages_functions.Facebook.Comment import Comment

class Downloader(QDialog):
    def __init__(self, url, output_file):
        super().__init__()
        self.url = url
        self.output_file = output_file

        self.initUI()

        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.onFinished)
        self.startDownload()

    def initUI(self):
        self.progress = QProgressBar(self)
        self.progress.setAlignment(Qt.AlignCenter)

        central_widget = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.progress)
        central_widget.setLayout(layout)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('File Downloader')
        self.show()

    def startDownload(self):
        request = QNetworkRequest(QUrl(self.url))
        self.reply = self.manager.get(request)
        self.reply.downloadProgress.connect(self.onProgress)

    def onProgress(self, bytes_received, bytes_total):
        if bytes_total > 0:
            self.progress.setValue(int(bytes_received * 100 / bytes_total))

    def onFinished(self):
        file = QFile(self.output_file)
        if file.open(QIODevice.WriteOnly):
            file.write(self.reply.readAll())
            file.close()
            print(f'Update Finished: {self.output_file}')
        else:
            print('Failed to open file for writing.')
        self.reply.deleteLater()
        self.manager.deleteLater()
        self.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.mac = ':'.join(['{:02x}'.format((uuid.getnode() >> 8 * i) & 0xff)for i in range(5, -1, -1)  ])
        self.ui.lineEdit.setText(self.mac)
        self.ui.copy.clicked.connect(lambda : QApplication.clipboard().setText(self.mac))
        self.ui.Home.hide()
        self.ui.Accound_edt.hide()
        self.ui.User.hide()
        self.ui.Post.hide()
        self.ui.Order.hide()
        self.ui.widget_order.hide()
        self.ui.stackedWidget.insertWidget(0, Manager_Face())
        self.ui.stackedWidget.insertWidget(1, Edit_Face())
        self.ui.stackedWidget.insertWidget(2, User())
        self.ui.stackedWidget.insertWidget(3, Post())
        self.ui.stackedWidget.insertWidget(4, Follow())
        self.ui.stackedWidget.insertWidget(5, Like())
        self.ui.stackedWidget.insertWidget(6, Share())
        self.ui.stackedWidget.insertWidget(7, Comment())
        self.ui.stackedWidget.setCurrentIndex(0)

        self.old_pos = self.pos()
        self.ui.close.clicked.connect(self.close)
        self.ui.maximize.clicked.connect(self.toggle_maximize_restore)
        self.ui.minimize.clicked.connect(self.showMinimized)
        self.Update()
        self.Active()

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
    def on_Home_toggled(self):
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
    def on_Profile_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(8)
    # def on_Setting_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(9)
    # def on_Help_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(10)
    def Update(self):
        if not self.check_internet_connection():
            input("Please check your internet connection!") ; return
        response = requests.get("https://pastebin.com/raw/gpQtcv4s")
        if response.status_code == 200:
            data = response.json()
            for item in data:
                version = item["version"]
                url = item["url"]
        if '1.0' < version:
            window = Downloader(url,'main.exe' )
            window.exec()

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
                    features = item["features"]
                    expiration_date = date.fromisoformat(item["expiration_date"])
                    return name , features , expiration_date
        return None, None , None
    def get_current_date(self,retries=3, delay=2):
        ntp_server = 'ntp2a.mcc.ac.uk'
        client = ntplib.NTPClient()
        for attempt in range(retries):
            try:
                response = client.request(ntp_server, version=3)
                timestamp = response.tx_time
                current_date = datetime.fromtimestamp(timestamp).date()
                return current_date
            except ntplib.NTPException as e:
                pass
            except Exception as e:
                pass
            if attempt < retries - 1:
                sleep(delay)
        
        return None
    def Active(self):
        name , features , expiration_date = self.get_data()
        if name:
            self.ui.label_name.setText(f'Welcome , {name}')
            current_date  = self.get_current_date()
            if current_date < expiration_date :
                if 'Home' in features:
                    self.ui.Home.setVisible(True)
                if 'Accound_edt' in features:
                    self.ui.Accound_edt.setVisible(True)
                if 'User' in features:
                    self.ui.User.setVisible(True)
                if 'Post' in features:
                    self.ui.Post.setVisible(True)
                if 'Order' in features:
                    self.ui.Order.setVisible(True)
                    
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
    # app = QApplication(sys.argv)
    # qtmodern.styles.dark(app)

    # url = 'https://download1338.mediafire.com/rlcnywppog6gbcwd8YBim76ygr-EDwHB4dZM20uNj17xcB8Sl9jWEruJwL6efbPsgLIMOHpBczwksYpYdkVFGkDUqAlX3Na7MQ3qgbAaHJQg22wf0iYQfKfQwh_57zBHnCXwmGvwpV6OiydNoEwYAb-ZOa5-5TYuWG2ZWIP9nhzG/g66aubh4erijbb3/New+Text+Document.txt'  # استبدل هذا بعنوان URL الخاص بك
    # output_file = 'pages_functions\\text.txt'  # استبدل هذا باسم الملف الذي تريد حفظه
    # window = MainWindow()
    # mw = qtmodern.windows.ModernWindow(window)
    # mw.show()
    # sys.exit(app.exec_())

    app = QApplication(sys.argv)

    # with open("pages_functions\style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())



