from pages_functions.__init__ import *
from ui.Public.Add_Account1_ui import Ui_Form

class Add_Account(QDialog):
    def __init__(self, parent=None):
        super(Add_Account, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.Save.clicked.connect(self.save)
        self.ui.Cancel.clicked.connect(self.accept)

    def save(self):
        if self.ui.Email.text()  == '' : QMessageBox.warning(self, 'No User Name', 'Please Enter an User Name.') ; return ""
        if self.ui.Password.text() == '' : QMessageBox.warning(self, 'No Password', 'Please Enter an Password.') ; return ""
        cursor.execute('INSERT INTO account (groupname , name , email, password,username, cookies, gendar) VALUES (?, ?, ?, ?, ?,?, ?)', (self.ui.Group.text(), self.ui.Name.text(), self.ui.Email.text(), self.ui.Password.text(),self.ui.User_Name.text(),self.ui.Cookies.text(), "female")); conn.commit()
        self.accept()
        self.parent().loadTableData()

        