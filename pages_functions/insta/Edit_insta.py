from pages_functions.__init__ import *
from ui.Public.Edit_ui import Ui_Form
from pages_functions.Insta.Data.Chrome import *
from pages_functions.Public.Select import Select_insta

class Edit_Insta(QWidget):
    def __init__(self):
        super(Edit_Insta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.is_running = False
        self.type = 'normal'

        self.ui.widget_Password.hide()
        self.ui.Add_Cover.hide()
        self.ui.Add_Friend.hide()
        self.ui.Join_Group.hide()
        self.ui.Like.hide()
        self.ui.Add_Share.hide()

        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui.browes_photo.clicked.connect(self.Browes_photo)
        self.ui.browes_cover.clicked.connect(self.Browes_cover)
        self.ui.browes_post.clicked.connect(self.Browes_post)
        self.ui.Select_Account.clicked.connect(self.Select)

        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)

        self.ui.Add_Profile_Photo.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.Add_Post.stateChanged.connect(lambda state: self.toggle_page(state, 2))
        self.ui.Add_Bio.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.Follow.stateChanged.connect(lambda state: self.toggle_page(state, 6))
        self.ui.Profrssional.stateChanged.connect(lambda state: self.toggle_page(state, 9))
        self.ui.Change_Password.stateChanged.connect(lambda state: self.toggle_page(state, 10))

        self.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())

        self.checked_state = [False, False, False, False, False, False]

    def toggle_page(self, state, index):
        if state == 2: 
            self.checked_state[index] = True
            self.ui.stackedWidget.setCurrentIndex(index)
            self.ui.stackedWidget.widget(index).setVisible(True)
        elif self.checked_state[index]:
            self.checked_state[index] = False
            self.ui.stackedWidget.widget(index).setVisible(False)
            self.ui.stackedWidget.setCurrentIndex(0)

    def Browes_photo(self):
        folderPath = QFileDialog.getOpenFileName(self, "Open Folder", "")
        if folderPath[0]:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.lineEdit_photo.setText(folderPath)
            self.ui.number_photo.setText(f'{file_count}')
            self.addphoto = corrected_path + '\\' + random_file
    def Browes_cover(self):
        folderPath = QFileDialog.getOpenFileName(self, "Open Folder", "")
        if folderPath[0]:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.lineEdit_cover.setText(folderPath)
            self.ui.number_cover.setText(f'{file_count}')
            self.addcover = corrected_path + "\\" + random_file
    def Browes_post(self):
        folderPath = QFileDialog.getOpenFileName(self, "Open Folder", "")
        if folderPath[0]:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.number_post.setText(f'{file_count}')
            self.post_photo = corrected_path + "\\" + random_file
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
    def Password(self):
        if self.ui.lineEdit_password.text() : return self.ui.lineEdit_password.text()
        else:
            if self.ui.checkBox_password.isChecked() : return self.Generat_password()
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
    def Select(self):
        data = cursor.execute("SELECT * FROM insta").fetchall()
        table_dialog = Select_insta(self,data)
        table_dialog.exec_()

    def Start(self):
        if self.ui.Number_Account.text() == '0': QMessageBox.warning(self, 'No Account Selected', 'Please select an Account.')
        else:
            if self.is_running == False :
                self.ui.Start.setText("Stop")
                self.is_running = True
            elif self.is_running :
                self.ui.Start.setText("Start")
                self.is_running = False

            for i in self.info :
                if self.is_running :
                    self.username = i[1]
                    self.password = i[3]
                    self.Chrom = Chrom_Insta()
                    result = self.Chrom.login(self.username,self.password)
                    if result != 'Ban':
                        result = self.Edit()
                        if result == 'success': 
                            print(Colorate.Diagonal(Colors.green_to_blue, f'[ Done Update Account ] : [ {self.username}:{self.password} ]', 1))   
                            self.Chrom.bot.quit()
                        elif result == 'Ban':
                            print(Colorate.Diagonal(Colors.red_to_blue, f'[ Error Update Account ] : [ {self.username}:{self.password} ]', 1))
                            self.Chrom.bot.quit()
                        elif result == 'Error Edit':
                            print('Error Edit')
                    else:
                        cursor.execute(f'DELETE FROM insta WHERE username = "{self.username}" ') ; conn.commit()
                        print("Ban")
            print('Finesh')
            self.ui.Start.setText("Start")
            self.is_running = False

    def Edit(self):
        try:
            if self.ui.Add_Profile.isChecked() :
                result = self.Chrom.Add_Photo(self.addphoto)
                if result == "Ban": return 'Ban'
            if self.ui.Add_Cover.isChecked() :self.Chrom.Add_Cover(self.addcover)
            if self.ui.Edit_Bio.isChecked() :self.Chrom.Edit_Bio(self.ui.lineEdit_bio.text())
            if self.ui.Profrssional.isChecked() :
                type = self.Chrom.profrssional()
                if type == 'successfully':
                    try:cursor.execute(f"UPDATE insta SET type = 'pro' WHERE username = '{self.username}' ") ; conn.commit()
                    except:print(f"Faild Contect Database ")
            if self.ui.Change_Password.isChecked() :
                self.new_password = self.Password()
                result = self.Chrom.changepassword(self.password , self.new_password)
                if result == 'success' :
                    try:cursor.execute(f"UPDATE insta SET password = '{self.new_password}' WHERE username = '{self.username}' ") ; conn.commit()
                    except:print(f"Faild Contect Database ")
                    self.password = self.new_password
            return 'success'
        except : return 'Error Edit'
    def Update_info(self,info):
        self.ui.Number_Account.setText(str(len(info)))
        self.info = info