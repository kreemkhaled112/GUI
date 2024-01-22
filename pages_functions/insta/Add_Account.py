from pages_functions.__init__ import *


from ui.insta.Add_Account_ui import Ui_Form
from pages_functions.__init__ import *

class Add_Account_insta(QDialog):
    def __init__(self, parent=None):
        super(Add_Account_insta, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        with open("static\style.qss", "r",encoding='utf-8') as style_file:
            style_str = style_file.read()
        self.setStyleSheet(style_str)

        self.ui.Save.clicked.connect(self.save)
        self.ui.Cancel.clicked.connect(self.accept)

    def save(self):
        if self.ui.User_Name.text()  == '' : QMessageBox.warning(self, 'No User Name', 'Please Enter an User Name.') ; return ""
        if self.ui.Password.text() == '' : QMessageBox.warning(self, 'No Password', 'Please Enter an Password.') ; return ""
        cursor.execute('INSERT INTO insta (groupname , username , email, password, cookies, type) VALUES (?, ?, ?, ?, ?, ?)', (self.ui.Group.text(), self.ui.User_Name.text(), self.ui.Email.text(), self.ui.Password.text(), self.ui.Cookies.text(), self.ui.Type.text())); conn.commit()
        self.accept()

        