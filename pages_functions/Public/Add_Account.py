from pages_functions.__init__ import *
from ui.Public.Add_Account_ui import Ui_Form
from pages_functions.Facebook.Data.Edit import *

class Add_Account(QDialog):
    def __init__(self, parent=None):
        super(Add_Account, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.widget_username.hide()
        self.ui.comboBox.currentIndexChanged.connect(self.filter_table)
        self.ui.Save.clicked.connect(self.save)
        self.ui.Cancel.clicked.connect(self.accept)
    
    def filter_table(self):
        selected_column = self.ui.comboBox.currentIndex()
        if selected_column == 0: self.ui.widget_username.hide() ; self.ui.widget_email.setVisible(True)
        elif selected_column == 1: self.ui.widget_email.hide() ; self.ui.widget_username.setVisible(True)
    
    def save(self):
        if self.ui.Email.text()  == ''  : QMessageBox.warning(self, 'No Email', 'Please Enter an Email.') ; return
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

# kzndrvca@hi2.in:830382t8e