from pages_functions.__init__ import *

from ui.Public.Edit_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.AddFriend import *
from pages_functions.Facebook.Data.Share import *
from pages_functions.Facebook.Data.Like import *
from pages_functions.Facebook.Data.JoinGroup import *
from pages_functions.Facebook.Data.Follow import *
from pages_functions.Public.Select import Select

class Edit_Face(QWidget):
    def __init__(self):
        super(Edit_Face, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Info = Info()
        QVBoxLayout(self.ui.widget_Info).addWidget(self.Info)
        self.is_running = False

        self.ui.widget_Password.hide()
        self.ui.Profrssional_check.hide()

        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui.browes_photo.clicked.connect(self.Browes_photo)
        self.ui.browes_cover.clicked.connect(self.Browes_cover)
        self.ui.browes_post.clicked.connect(self.Browes_post)
        self.ui.Select_Account.clicked.connect(self.Select)
        # self.ui.Start.clicked.connect(lambda : Thread(target=self.Start).start())

        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)

        self.ui.Add_Profile_Photo_check.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.Add_Cover_check.stateChanged.connect(lambda state: self.toggle_page(state, 1))
        self.ui.Add_Post_check.stateChanged.connect(lambda state: self.toggle_page(state, 2))
        self.ui.Add_Bio_check.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.Add_Friend_check.stateChanged.connect(lambda state: self.toggle_page(state, 4))
        self.ui.Join_Group_check.stateChanged.connect(lambda state: self.toggle_page(state, 5))
        self.ui.Follow_check.stateChanged.connect(lambda state: self.toggle_page(state, 6))
        self.ui.Like_check.stateChanged.connect(lambda state: self.toggle_page(state, 7))
        self.ui.Share_check.stateChanged.connect(lambda state: self.toggle_page(state, 8))
        self.ui.Change_Password_check.stateChanged.connect(lambda state: self.toggle_page(state, 10))

        self.checked_state = [False,False,False,False,False,False,False,False,False,False,False]
        
    def toggle_page(self, state, index):
        if state == 2:
            self.checked_state[index] = True
            self.ui.stackedWidget.setCurrentIndex(index)
            self.ui.stackedWidget.widget(index).setVisible(True)
        elif self.checked_state[index]:
            self.checked_state[index] = False
            self.ui.stackedWidget.widget(index).setVisible(False)
            self.ui.stackedWidget.setCurrentIndex(2)

    def Browes_photo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        folderPath = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if folderPath:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.lineEdit_photo.setText(folderPath)
            self.ui.number_photo.setText(f'{file_count}')
            self.profil_photo = corrected_path + '\\' + random_file
    def Browes_cover(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        folderPath = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if folderPath:
            corrected_path = normpath(folderPath).replace('/', '\\')
            random_file,file_count = self.get_random_file(folderPath)
            self.ui.lineEdit_cover.setText(folderPath)
            self.ui.number_cover.setText(f'{file_count}')
            self.cover_photo = corrected_path + "\\" + random_file
    def Browes_post(self): 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        folderPath = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if folderPath:
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
    def Bio(self):
        if self.ui.lineEdit_bio.text() : return self.ui.lineEdit_bio.text()
        else:
            if self.ui.checkBox_bio.isChecked() : 
                bio = cursor.execute('SELECT bio FROM bio ORDER BY RANDOM() LIMIT 1').fetchone()
                return bio[0]
            else: QMessageBox.warning(self, 'No Bio Selected', 'Please select an option.')
    
    def Select(self):
        data = cursor.execute("SELECT * FROM account").fetchall()
        table_dialog = Select(self,data)
        table_dialog.exec()

    def Edit(self,cookie,profil_photo=None,cover_photo=None,id_friend=None,url=None,text=None,id_group=None,id_like=None,type=None,id_follow=None):
        try:
            result = ['success']
            if self.ui.Add_Profile_Photo_check.isChecked() :
                Profile = Edit_Photo(profil_photo,cookie)
                if Profile == "Ban":  result.append(Profile) 
                return 'Ban'
            else: result.append(None)
            if self.ui.Add_Cover_check.isChecked() :
                while True :
                    cover = Edit_Cover(cover_photo,cookie)
                    if cover == "successfully" : result.append(cover) ; break
            else: result.append(None)
            result.extend([
                "" if self.ui.Add_Post_check.isChecked() else None,
                Edit_bio(self.Bio(), cookie) if self.ui.Add_Bio_check.isChecked() else None,
                AddFriend(id_friend, cookie) if self.ui.Add_Friend_check.isChecked() else None,
                JoinGroup(id_group, cookie) if self.ui.Join_Group_check.isChecked() else None,
                Follow(id_follow, cookie) if self.ui.Follow_check.isChecked() else None,
                Like(id_like, type, cookie).Start() if self.ui.Like_check.isChecked() else None,
                share(url, text, cookie) if self.ui.Share_check.isChecked() else None
            ])
            if self.ui.Change_Password_check.isChecked() :
                self.new_password = self.Password()
                result = Change_Password(self.password , self.new_password)
                if result == 'success' :
                    try:cursor.execute(f"UPDATE account SET password = '{self.new_password}' WHERE email = '{self.email}' ") ; conn.commit()
                    except:print(f"Faild Contect Database ")
                    self.password = self.new_password
            else: result.append(None)
            return result
        except Exception as e : 
            print(e)
            return 'Error Edit'

    def Update_info(self,info):
        self.ui.Number_Account.setText(str(len(info)))
        self.info = info

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
                    self.email = i[2]
                    self.password = i[3]
                    self.cookie = i[5]
                    id_friend = self.ui.textEdit_Friend.toPlainText()
                    id_group = self.ui.textEdit_Group.toPlainText()
                    id_follow = self.ui.textEdit_Follow.toPlainText()
                    id_like = self.ui.textEdit_Like.toPlainText()

                    result = self.Edit(self.cookie)
                    if result == 'success': print(Colorate.Diagonal(Colors.green_to_blue, f'[ Done Update Account ] : [ {self.email}:{self.password} ]', 1))   
                    elif result == 'Ban': print(Colorate.Diagonal(Colors.red_to_blue, f'[ Error Update Account ] : [ {self.email}:{self.password} ]', 1))
                    elif result == 'Error Edit': print('Error Edit')
                    
            print('Finesh')
            self.ui.Start.setText("Start")
            self.is_running = False