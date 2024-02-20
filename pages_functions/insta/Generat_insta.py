from pages_functions.__init__ import *

from ui.Public.Generat_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Public.Edit import Edit
from pages_functions.Insta.Data.Chrome import *

class Generat_Insta(QWidget):
    def __init__(self):
        super(Generat_Insta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui_Edit = Edit(Info())
        layout = QVBoxLayout(self.ui.widget_Edit); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.ui_Edit)
        self.is_running = False
        self.Error = 3
        self.Error1 = 600
        self.mp3 = "Data\\error.mp3"

        self.ui.widget_Email1.hide()
        self.ui.widget_Password1.hide()
        self.ui_Edit.ui.widget_Select.hide()
        self.ui_Edit.ui.Change_Password_check.hide()
        self.ui_Edit.Info.ui.table.setColumnHidden(3, True)

        self.ui_Edit.ui.Start.setText("Switch")
        self.ui_Edit.Info.ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("Username : Password"))
        self.ui_Edit.Info.ui.table.setColumnWidth(2, 200)

        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui_Edit.ui.Start.clicked.connect(lambda : Thread(target=self.Switch).start())
    
    def Password(self):
        if self.ui.lineEdit_password.text() : return self.ui.lineEdit_password.text()
        else:
            if self.ui.checkBox_password.isChecked() : return self.Generat_password()
            else: QMessage( 'No Password Selected', 'Please select an option.').mainloop() ;return  None
    def Generat_password(self):
        if self.ui.checkBox_4.isChecked() or self.ui.checkBox_5.isChecked() :
            chrs = ''
            text1 = self.ui.lineEdit_4.text() if self.ui.lineEdit_4.text() is not None else ''
            if self.ui.checkBox_4.isChecked() : chrs += '0123456789'
            if self.ui.checkBox_5.isChecked() : chrs += 'abcdefghijklmnopqrstuvwxyz'
            value =  int(self.ui.spinBox.value())
            password = text1 + ''.join(random.choices(list(chrs) if chrs else '', k=value))
            self.ui.Generat_Password_2.setText(password)
            return password
        else: QMessageBox.warning(self, 'No Password Selected', 'Please select an option.')
    def message(self,type,message):
        self.ui_Edit.Info.ui.label.setText(f"{message}")
        self.ui_Edit.Info.Add(type,f'{self.email}:{self.password}','Generat Account',"Generat Account", message )
        self.ui_Edit.Info.Update(s=self.success,f=self.failed)
    
    def Start(self):
        self.Chrom = Chrom_Insta()
        switch = self.Chrom.switch(self.email,self.name,self.password,self.cookie,self.password)
        if switch is not None:
            self.username , self.Cookie = switch
            if self.Cookie is None:
                cursor.execute(f"UPDATE account SET insta = 'ban' WHERE email = '{self.email}' ")
                conn.commit()
                input("......")
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ BAN ] : [ {self.email}:{self.password} ]', 1))
            else:
                result = self.Edit()
                if result == 'success':
                    try:
                        cursor.execute('INSERT INTO insta (username , email, password, cookies, type) VALUES (  ?, ?, ?, ?, ?)', (  self.username, self.email, self.password, self.Cookie, self.type))
                        cursor.execute(f"UPDATE account SET insta = 'good' WHERE email = '{self.email}' ")
                        conn.commit()
                        print(Colorate.Diagonal(Colors.green_to_blue, f'[ Done Add Account ] : [ {self.email}:{self.password} ]', 1))
                    except:print(f"Faild Contect Database ")
                elif result == 'Ban':
                    print(Colorate.Diagonal(Colors.red_to_blue, f'[ Error ] : [ {self.email}:{self.password} ]', 1))
                    cursor.execute(f"UPDATE account SET insta = 'ban' WHERE email = '{self.email}' ")
                    conn.commit()
                    input("......")
                elif result == 'Error Edit':
                    print('Error Edit')
        else:return 'faild'

    def Switch(self):
        if self.is_running == False :
            self.ui_Edit.ui.Start.setText("Stop")
            self.is_running = True
        elif self.is_running :
            self.ui_Edit.ui.Start.setText("Switch")
            self.is_running = False

        while self.is_running :
            ac = cursor.execute(f"SELECT * FROM account  ").fetchall()
            for row in ac :
                if row[7] == 'pending' :
                    self.name = row[1]
                    self.email = row[2]
                    self.password = row[3]
                    self.cookie = row[5]
                    break
            self.Start()

    def Edit(self):
        try:
            if self.ui_Edit.ui.Add_Profile_Photo_check.isChecked() :
                self.ui_Edit.Info.ui.label.setText(f"{self.username} Try Change Profile Photo")
                result = self.Chrom.Add_Photo(self.ui_Edit.get_random_file(self.ui_Edit.profil_photo))
                if result == "Ban" : return 'Ban'
            if self.ui_Edit.ui.Add_Cover_check.isChecked() :
                self.ui_Edit.Info.ui.label.setText(f"{self.username} Try Change Cover Photo")
                self.Chrom.Add_Cover(self.ui_Edit.get_random_file(self.ui_Edit.cover_photo))
            if self.ui_Edit.ui.Add_Bio_check.isChecked() :
                if self.ui.textEdit_bio.toPlainText() :
                    bio = random.choice(self.ui_Edit.ui.textEdit_bio.toPlainText().split('\n'))
                    self.ui_Edit.Info.ui.label.setText(f"{self.username} Try Change Bio")
                    self.Chrom.Edit_Bio(bio)
            if self.ui_Edit.ui.Profrssional_check.isChecked() :
                type = self.Chrom.profrssional()
                self.type = 'pro' if type == 'successfully' else 'normal'
            return 'success'
        except : return 'Error Edit'