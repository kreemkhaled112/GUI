from pages_functions.__init__ import *
from ui.Public.Add_Account_ui import Ui_Form
from pages_functions.Facebook.Data.Edit import *

class Add_Account(QDialog):
    def __init__(self, parent=None):
        super(Add_Account, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.Save.clicked.connect(self.save)
        self.ui.Cancel.clicked.connect(self.accept)

    def save(self):
        if self.ui.Email.text()  == '' : QMessageBox.warning(self, 'No User Name', 'Please Enter an User Name.') ; return
        if self.ui.Password.text() == '' : QMessageBox.warning(self, 'No Password', 'Please Enter an Password.') ; return
        if self.ui.Cookies.text() == '' : Name = "None" ; username = "None"
        else:
            Name = Get_Name(self.ui.Cookies.text()).Get()
            username = re.search(r'c_user=(\d+)', self.ui.Cookies.text()).group(1)
        try:cursor.execute('INSERT INTO account (groupname , name , email, password,username, cookies, gendar) VALUES (?, ?, ?, ?, ?,?, ?)', (self.ui.Group.text(), Name, self.ui.Email.text(), self.ui.Password.text(),username,self.ui.Cookies.text(), "female")); conn.commit()
        except: print("database is locked")
        self.accept()
        data = cursor.execute("SELECT * FROM account").fetchall()
        self.parent().loadTableData(data)
        Thread(target=self.parent().Update()).start()

        