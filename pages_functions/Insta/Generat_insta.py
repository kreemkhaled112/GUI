from pages_functions.__init__ import *
from ui.insta.Generat_ui import Ui_Form
from pages_functions.__init__ import *
from pages_functions.insta.Data.Follow import *
from pages_functions.insta.Data.Chrome import *

class Generat_insta(QWidget):
    def __init__(self):
        super(Generat_insta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        with open("static\style.qss", "r",encoding='utf-8') as style_file:
            style_str = style_file.read()
        self.setStyleSheet(style_str)
        self.is_running = False
        self.Error = 3
        self.Error1 = 600
        self.mp3 = "Data\\error.mp3"
        self.type = 'normal'
        self.ui.widget_2.hide()
        # self.ui.widget_4.hide()
        self.ui.widget_6.hide()
        self.ui.lineEdit_3.setText('pastaaa6000')
        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui.pushButton_3.clicked.connect(self.Browes_photo)
        self.ui.pushButton_4.clicked.connect(self.Browes_cover)
        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)

        self.ui.Add_Profile.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.Add_Cover.stateChanged.connect(lambda state: self.toggle_page(state, 1))
        self.ui.Edit_Bio.stateChanged.connect(lambda state: self.toggle_page(state, 2))
        self.ui.Profrssional.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.Follow.stateChanged.connect(lambda state: self.toggle_page(state, 4))

        self.ui.Switch.clicked.connect(lambda : Thread(target=self.Start).start())

        self.checked_state = [False, False, False,False, False, False,False, False, False, False, False]


    def toggle_page(self, state, index):
        if state == 2: 
            self.checked_state[index] = True
            self.ui.stackedWidget.setCurrentIndex(index)
            self.ui.stackedWidget.widget(index).setVisible(True)
        elif self.checked_state[index]:
            self.checked_state[index] = False
            self.ui.stackedWidget.widget(index).setVisible(False)
            self.ui.stackedWidget.setCurrentIndex(0)
    def Name(self):
        if self.ui.lineEdit.text() : return self.ui.lineEdit.text()
        else:
            if self.ui.checkBox.isChecked() :
                if self.ui.radioButton.isChecked():
                    random_item = cursor.execute("SELECT data FROM name WHERE type='male' ORDER BY RANDOM() LIMIT 1").fetchone()
                    return random_item
                elif self.ui.radioButton_2.isChecked(): 
                    random_item = cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone()
                    return random_item
                elif self.ui.radioButton_3.isChecked():
                    random_item = cursor.execute("SELECT data FROM name ORDER BY RANDOM() LIMIT 1").fetchone() 
                    return random_item
                else: QMessageBox.warning(self, 'No Name Selected', 'Please select an option.')
            else: QMessageBox.warning(self, 'No Name Selected', 'Please select an option.')
    def Password(self):
        if self.ui.lineEdit_3.text() : return self.ui.lineEdit_3.text()
        else:
            if self.ui.checkBox_3.isChecked() : return self.Generat_password()
            else:
                QMessageBox.warning(self, 'No Password Selected', 'Please select an option.')
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
        else:
            QMessageBox.warning(self, 'No Password Selected', 'Please select an option.')
    def Browes_photo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        folderPath = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if folderPath:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.lineEdit_8.setText(folderPath)
            self.ui.label_15.setText(f'{file_count}')
            self.addphoto = corrected_path + '\\' + random_file

    def Browes_cover(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        folderPath = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if folderPath:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.lineEdit_9.setText(folderPath)
            self.ui.label_17.setText(f'{file_count}')
            self.addcover = corrected_path + "\\" + random_file

    def get_random_file(self, folder_path):
        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if files:return random.choice(files) , len(files)
            else:
                print('No files in the folder.')
                return 'No files in the folder.'
        except Exception as e:
            print(f"Error getting random file: {e}")
            return 'Error getting random file.'
    def switch(self):
        ac = cursor.execute(f"SELECT * FROM account  ").fetchall()
        for row in ac :
            if row[6] == 'pending' :
                self.email = row[1]
                pas = row[2]
                cookie = row[4]
                break
        name = self.Name()
        self.password = self.Password()
        self.Chrom = Chrom_Insta()
        switch = self.Chrom.switch(self.email,name[0],self.password,cookie,pas)
        if switch is not None:
            self.username , self.Cookie = switch
            if self.Cookie is None:
                cursor.execute(f"UPDATE account SET insta = 'ban' WHERE email = '{self.email}' ")
                conn.commit()
                self.Chrom.bot.quit()
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ BAN ] : [ {self.email}:{pas} ]', 1))
            else:return 'success'
        else:return 'faild'

    def Start(self):
        if self.is_running == False :
            self.ui.Switch.setText("Stop")
            self.is_running = True
        elif self.is_running :
            self.ui.Switch.setText("Switch")
            self.is_running = False
        Successfully = 0
        Failed = 0
        while self.is_running :
            result = self.switch()
            if result == 'success':
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
                    self.Chrom.bot.quit()
                elif result == 'Error Edit':
                    print('Error Edit')
            elif result == 'Failed':
                print('Failed')
    def Update(self,successful,faild,time):
        self.ui.successful.setText(successful)
        self.ui.faild.setText(successful)
        self.ui.total.setText(successful+faild)
        self.ui.time.setText(time)

    def Edit(self):
        try:
            if self.ui.Add_Profile.isChecked() :
                result = self.Chrom.Add_Photo(self.addphoto)
                if result == "Ban" : return 'Ban'
            if self.ui.Add_Cover.isChecked() :self.Chrom.Add_Cover(self.addcover)
            if self.ui.Edit_Bio.isChecked() :self.Chrom.Edit_Bio(self.ui.lineEdit_10.text())
            if self.ui.Profrssional.isChecked() :
                type = self.Chrom.profrssional()
                if type == 'successfully': self.type = 'pro'
            return 'success'
        except : return 'Error Edit'
