from pages_functions.__init__ import *

from ui.Public.Edit_ui import Ui_Form
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.AddFriend import *
from pages_functions.Facebook.Data.Share import *
from pages_functions.Facebook.Data.Like import *
from pages_functions.Facebook.Data.Comment import Comment
from pages_functions.Facebook.Data.JoinGroup import *
from pages_functions.Facebook.Data.Follow import *
from pages_functions.Facebook.Data.Un_Follow import *
from pages_functions.Public.Select import Select

class Edit(QWidget):
    def __init__(self,Info=None):
        super(Edit, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Info = Info
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.is_running = False

        self.ui.widget_Password.hide()
        self.ui.Profrssional_check.hide()

        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui.browes_photo.clicked.connect(self.Browes_photo)
        self.ui.browes_cover.clicked.connect(self.Browes_cover)
        self.ui.browes_post.clicked.connect(self.Browes_post)
        self.ui.Select_Account.clicked.connect(self.Select)

        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)

        self.ui.Add_Profile_Photo_check.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.Add_Cover_check.stateChanged.connect(lambda state: self.toggle_page(state, 1))
        self.ui.Add_Post_check.stateChanged.connect(lambda state: self.toggle_page(state, 2))
        self.ui.Add_Post_check.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.Add_Bio_check.stateChanged.connect(lambda state: self.toggle_page(state, 4))
        self.ui.Add_Friend_check.stateChanged.connect(lambda state: self.toggle_page(state, 5))
        self.ui.Join_Group_check.stateChanged.connect(lambda state: self.toggle_page(state, 6))
        self.ui.Follow_check.stateChanged.connect(lambda state: self.toggle_page(state, 7))
        self.ui.Un_Follow_check.stateChanged.connect(lambda state: self.toggle_page(state, 8))
        self.ui.Like_check.stateChanged.connect(lambda state: self.toggle_page(state, 9))
        self.ui.Comment_check.stateChanged.connect(lambda state: self.toggle_page(state, 10))
        self.ui.Comment_Like_check.stateChanged.connect(lambda state: self.toggle_page(state, 11))
        self.ui.Share_check.stateChanged.connect(lambda state: self.toggle_page(state, 12))
        self.ui.Change_Password_check.stateChanged.connect(lambda state: self.toggle_page(state, 14))

        self.checked_state = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        
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
        self.profil_photo = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if self.profil_photo:
            random_file = self.get_random_file(self.profil_photo)
            self.ui.lineEdit_photo.setText(random_file)
            files = [f for f in os.listdir(self.profil_photo) if os.path.isfile(os.path.join(self.profil_photo, f))]
            self.ui.number_photo.setText(str(len(files)))
    def Browes_cover(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        self.cover_photo = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if self.cover_photo:
            random_file = self.get_random_file(self.cover_photo)
            self.ui.lineEdit_cover.setText(random_file)
            files = [f for f in os.listdir(self.cover_photo) if os.path.isfile(os.path.join(self.cover_photo, f))]
            self.ui.number_cover.setText(str(len(files)))
    def Browes_post(self): 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  
        self.post = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)
        if self.post:
            random_file = self.get_random_file(self.post)
            self.ui.lineEdit_post.setText(random_file)
            files = [f for f in os.listdir(self.post) if os.path.isfile(os.path.join(self.post, f))]
            self.ui.number_cover.setText(str(len(files)))
    def get_random_file(self, folder_path):
        try:
            corrected_path = normpath(folder_path).replace('/', '\\')
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if files:return corrected_path + "\\" + random.choice(files)
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
            else: QMessageBox.warning(self, 'No Password Selected', 'Please select an option.')
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

    def Edit(self,name,cookie):
        try:
            if self.ui.Add_Profile_Photo_check.isChecked() :
                Profile = Edit_Photo(self.get_random_file(self.profil_photo),cookie)
                if Profile == "Ban": return 'Error photo'
            if self.ui.Add_Cover_check.isChecked() :
                while True:
                    cover = Edit_Cover(self.get_random_file(self.cover_photo),cookie)
                    if cover == "successfully" :  break       
            if self.ui.Add_Post_check.isChecked():
                pass
            if self.ui.Add_Bio_check.isChecked() :
                result = Edit_bio(self.Bio(), cookie) 
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Bio",result[0])
            if self.ui.Add_Friend_check.isChecked():
                result = AddFriend(self.id_friend, cookie)
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Add Friend",result[0])
            if self.ui.Join_Group_check.isChecked():
                result = JoinGroup(self.id_group,cookie).Start()  
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Join Groub",result[0])
            if self.ui.Follow_check.isChecked():
                result = Follow(self.id_follow, cookie).Start()
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Follow",result[0])
            if self.ui.Un_Follow_check.isChecked():
                result = Un_Follow(self.id_un_follow, cookie).Start()
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Un Follow",result[0])
            if self.ui.Like_check.isChecked():
                result = Like(self.id_like, type, cookie).Start()  
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Like",f'{result[0]} To {self.id_like}')
            if self.ui.Comment_check.isChecked():
                result = Comment(self.id_like, self.text_comment, cookie).Start()  
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Comment",f'{result[0]} To {self.id_like}')
            if self.ui.Share_check.isChecked():
                result = Share(self.id_like, "", cookie).Start()
                self.Info.ui.label.setText(f"{name} {result[0]}")
                self.Info.Add(result[1],name,"Share",f'{result[0]} To {self.id_like}')
            if self.ui.Change_Password_check.isChecked() :
                self.new_password = self.Password()
                result = Change_Password(self.password , self.new_password)
                if result == 'success' :
                    try:cursor.execute(f"UPDATE account SET password = '{self.new_password}' WHERE email = '{self.email}' ") ; conn.commit()
                    except:print(f"Faild Contect Database ")
                    self.password = self.new_password
            return 'succes'
        except Exception as e :
            self.Info.ui.label.setText(f"{name} Error")
            self.Info.Add(0,name,"None",f'{e}')
            return 'Error Edit'
    def Start(self):
        if self.ui.Number_Account.text() == '0': QMessage(text = 'No Account Selected').mainloop()
        else:
            for info in self.info :
                self.id_friend = self.ui.textEdit_Friend.toPlainText()
                self.id_group = self.ui.textEdit_Group.toPlainText()
                self.id_follow = self.ui.textEdit_Follow.toPlainText()
                self.id_un_follow = self.ui.textEdit_un_Follow.toPlainText()
                self.id_like = self.ui.textEdit_Like.toPlainText()
                self.text_comment = self.ui.textEdit_Like.toPlainText()
                self.id_share = self.ui.textEdit_Like.toPlainText()
                # url = self.ui.lineEdit_24.toPlainText()

                self.Edit(info[1],info[5])
    def Update_info(self,info):
        self.ui.Number_Account.setText(str(len(info)))
        self.info = info

    