from pages_functions.__init__ import *

from ui.Public.Edit_ui import Ui_Form
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.Action import *
from pages_functions.Public.Select import Select
from pages_functions.Public.Info import Info

class Edit(QWidget):
    def __init__(self):
        super(Edit, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.Info = Info()
        layout = QVBoxLayout(self.ui.widget_Info); layout.setContentsMargins(0, 0, 0, 0); layout.setSpacing(0); layout.addWidget(self.Info)
        self.is_running = False
        self.time = 10
        self.succes = 0
        self.failed = 0
        self.order = 0
        self.bot =''

        self.ui.widget_Password.hide()
        self.ui.Profrssional_check.hide()
        self.ui.widget_17.setVisible(False)
        self.Info.ui.table.setColumnHidden(3, True)

        self.ui.spinBox_2.textChanged.connect(self.filter)
        self.ui.spinBox_3.textChanged.connect(self.filter)
        self.ui.comboBox.currentIndexChanged.connect(self.filter)
        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui.browes_photo.clicked.connect(self.Browes_photo)
        self.ui.browes_cover.clicked.connect(self.Browes_cover)
        self.ui.browes_post.clicked.connect(self.Browes_post)
        self.ui.Select_Account.clicked.connect(self.Select)
        self.ui.checkBox_city.clicked.connect(self.Import_DB)
        self.ui.checkBox_hometown.clicked.connect(self.Import_DB)
        self.ui.checkBox_work.clicked.connect(self.Import_DB)
        self.ui.checkBox_school.clicked.connect(self.Import_DB)
        self.ui.checkBox_bio.clicked.connect(self.Import_DB)
        self.ui.checkBox_group.clicked.connect(self.Import_DB)
        self.ui.checkBox_share.clicked.connect(self.Import_DB)

        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)

        self.ui.Profile_Photo_check.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.Cover_check.stateChanged.connect(lambda state: self.toggle_page(state, 1))
        self.ui.Add_Post_check.stateChanged.connect(lambda state: self.toggle_page(state, 2))
        self.ui.City_check.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.Hometown_check.stateChanged.connect(lambda state: self.toggle_page(state, 4))
        self.ui.Work_check.stateChanged.connect(lambda state: self.toggle_page(state, 5))
        self.ui.School_check.stateChanged.connect(lambda state: self.toggle_page(state, 6))
        self.ui.Add_Post_check.stateChanged.connect(lambda state: self.toggle_page(state, 7))
        self.ui.Add_Bio_check.stateChanged.connect(lambda state: self.toggle_page(state, 8))
        self.ui.Add_Friend_check.stateChanged.connect(lambda state: self.toggle_page(state, 9))
        self.ui.Join_Group_check.stateChanged.connect(lambda state: self.toggle_page(state, 10))
        self.ui.Follow_check.stateChanged.connect(lambda state: self.toggle_page(state, 11))
        self.ui.Un_Follow_check.stateChanged.connect(lambda state: self.toggle_page(state, 12))
        self.ui.Like_Page_check.stateChanged.connect(lambda state: self.toggle_page(state, 13))
        self.ui.Like_check.stateChanged.connect(lambda state: self.toggle_page(state, 14))
        self.ui.Comment_check.stateChanged.connect(lambda state: self.toggle_page(state, 15))
        self.ui.Comment_Like_check.stateChanged.connect(lambda state: self.toggle_page(state, 16))
        self.ui.Share_check.stateChanged.connect(lambda state: self.toggle_page(state, 17))
        self.ui.Change_Password_check.stateChanged.connect(lambda state: self.toggle_page(state, 18))

        self.checked_state = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
        self.Info.ui.label.setText("welcom Account Edit")

    def toggle_page(self, state, index):
        if state == 2:
            self.checked_state[index] = True
            self.ui.stackedWidget.setCurrentIndex(index)
            self.ui.stackedWidget.widget(index).setVisible(True)
        elif self.checked_state[index]:
            self.checked_state[index] = False
            self.ui.stackedWidget.widget(index).setVisible(False)
            self.ui.stackedWidget.setCurrentIndex(2)

    def filter(self):
        selected_column = self.ui.comboBox.currentIndex()
        if selected_column == 0 :
            self.ui.label_3.setText("10 Second")
            self.ui.widget_17.setVisible(False)
            self.time = 10
        elif selected_column == 1 :
            self.ui.label_3.setText("5 Second")
            self.ui.widget_17.setVisible(False)
            self.time = 5
        elif selected_column == 2 :
            self.ui.label_3.setText("1 Second")
            self.ui.widget_17.setVisible(False)
            self.time = 1
        elif selected_column == 3 :
            self.ui.widget_17.setVisible(True)
            try:self.time = random.randrange(int(self.ui.spinBox_2.value()),int(self.ui.spinBox_3.value()))
            except:pass
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
    
    def Select(self):
        table_dialog = Select(self)
        table_dialog.exec()
    def Update_info(self,info):
        self.ui.Number_Account.setText(str(len(info)))
        self.data = queue.Queue(); [self.data.put(i) for i in info]

    def reaction_id(self):
        type = []
        if self.ui.Like_checkBox.isChecked() :
            type.append("Like")
        if self.ui.Love_checkBox.isChecked() :
            type.append("Love") 
        if self.ui.Care_checkBox.isChecked() :
            type.append("Care") 
        if self.ui.Haha_checkBox.isChecked() :
            type.append("Haha") 
        if self.ui.Wow_checkBox.isChecked() :
            type.append("Wow") 
        if self.ui.Sad_checkBox.isChecked() :
            type.append("Sad") 
        if type: type = random.choice(type)
        return type
    def Edit(self,name,email,password,cookie):
        try:
            if self.ui.Profile_Photo_check.isChecked() and self.is_running :
                self.Info.ui.label.setText(f"Try Change Profile Photo {name}.")
                result = Edit_Photo(self.get_random_file(self.profil_photo),cookie).Start()
                self.Info.Add(result[1],name,'Edit',"Profile Photo",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ;sleep(self.time) 
                if result[1] == 0: return 'Error photo'
            if self.ui.Cover_check.isChecked() and self.is_running :
                for _ in range(3) : 
                    self.Info.ui.label.setText(f"Try Change Cover Photo {name}.")
                    result = Edit_Cover(self.get_random_file(self.cover_photo),cookie).Start()
                    if result[1] == 1 :
                        self.Info.Add(result[1],name,'Edit',"Cover Photo",result[0])
                        break
                    self.Info.Add(result[1],name,'Edit',"Cover Photo",result[0]) 
                    sleep(1)
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.City_check.isChecked() and self.is_running :
                if self.ui.textEdit_city.toPlainText() :
                    city = random.choice(self.ui.textEdit_city.toPlainText().split('\n'))
                    self.Info.ui.label.setText(f"Try Add City {name}.")
                    result = Edit_City(city, cookie).Start()
                    self.Info.Add(result[1],name,'Edit',"City",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Hometown_check.isChecked() and self.is_running :
                if self.ui.textEdit_hometown.toPlainText() :
                    hometown = random.choice(self.ui.textEdit_hometown.toPlainText().split('\n'))
                    self.Info.ui.label.setText(f"Try Add Hometown {name}.")
                    result = Edit_Hometown(hometown, cookie).Start()
                    self.Info.Add(result[1],name,'Edit',"Hometown",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Work_check.isChecked() and self.is_running :
                if self.ui.textEdit_work.toPlainText() :
                    work = random.choice(self.ui.textEdit_work.toPlainText().split('\n'))
                    self.Info.ui.label.setText(f"Try Add Work {name}.")
                    result = Work(work, cookie).Start()
                    self.Info.Add(result[1],name,'Edit',"Work",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.School_check.isChecked() and self.is_running :
                if self.ui.textEdit_school.toPlainText() :
                    school = random.choice(self.ui.textEdit_school.toPlainText().split('\n'))
                    self.Info.ui.label.setText(f"Try Add School {name}.")
                    result = School(school, cookie).Start()
                    self.Info.Add(result[1],name,'Edit',"School",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Add_Bio_check.isChecked() and self.is_running :
                if self.ui.textEdit_bio.toPlainText() :
                    bio = random.choice(self.ui.textEdit_bio.toPlainText().split('\n'))
                    self.Info.ui.label.setText(f"Try Change Bio {name}.")
                    result = Edit_bio(bio, cookie).Start()
                    self.Info.Add(result[1],name,'Edit',"Bio",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Add_Friend_check.isChecked() and self.is_running :
                if self.ui.textEdit_friend.toPlainText():
                    id_friend = random.sample(self.ui.textEdit_friend.toPlainText().split('\n'), int(self.ui.spinBox_friend.value()))
                    self.Info.ui.label.setText(f"Try Add Friend {name}.")
                    for i in id_friend :
                        result = AddFriend(i, cookie).Start()
                        self.Info.Add(result[1],name,'Edit',"Add Friend",result[0])
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Join_Group_check.isChecked() and self.is_running :
                if self.ui.textEdit_group.toPlainText():
                    id_group = random.sample(self.ui.textEdit_group.toPlainText().split(), int(self.ui.spinBox_group.value()))
                    self.Info.ui.label.setText(f"Try Join Groub {name}.")
                    for i in id_group :
                        result = JoinGroup(i,cookie).Start()  
                        self.Info.Add(result[1],name,'Edit',"Join Groub",f'{result[0]} To {i}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Follow_check.isChecked() and self.is_running :
                if self.ui.textEdit_Follow.toPlainText():
                    id_follow = random.sample(self.ui.textEdit_Follow.toPlainText().split(), int(self.ui.spinBox_follow.value()))
                    self.Info.ui.label.setText(f"Try Follow {name}.")
                    for i in id_follow :
                        result = Follow(i, cookie).Start()
                        self.Info.Add(result[1],name,'Edit',"Follow",f'{result[0]}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Un_Follow_check.isChecked() and self.is_running :
                if self.ui.textEdit_un_Follow.toPlainText() :
                    id_un_follow = random.sample(self.ui.textEdit_un_Follow.toPlainText().split(), int(self.ui.spinBox_un_follow.value()))
                    self.Info.ui.label.setText(f"Try Un Follow {name}.")
                    for i in id_un_follow :
                        result = Un_Follow(i, cookie).Start()
                        self.Info.Add(result[1],name,'Edit',"Un Follow",f'{result[0]} {i}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Like_Page_check.isChecked() and self.is_running :
                if self.ui.textEdit_like_page.toPlainText() :
                    like_page = random.sample(self.ui.textEdit_like_page.toPlainText().split(), int(self.ui.spinBox_like_page.value()))
                    self.Info.ui.label.setText(f"Try Like Page {name}.")
                    for i in like_page :
                        result = Like_Page(i, cookie).Start()
                        self.Info.Add(result[1],name,'Edit',"Like Page",f'{result[0]} {i}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Like_check.isChecked() and self.is_running :
                if self.ui.textEdit_like.toPlainText() :
                    id_like = random.sample(self.ui.textEdit_like.toPlainText().split('\n'), int(self.ui.spinBox_like.value()))
                    self.Info.ui.label.setText(f"Try Like {name}.")
                    for i in id_like :
                        result = Like(i, self.reaction_id(), cookie).Start()  
                        self.Info.Add(result[1],name,'Edit',"Like",f'{result[0]} {i}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            if self.ui.Comment_check.isChecked() and self.is_running :
                if self.ui.textEdit_comment.toPlainText() :
                    if self.ui.checkBox_comment.isChecked():
                        comment = queue.Queue(); [comment.put(i) for i in random.sample(self.ui.textEdit_comment.toPlainText().split('\n'), len(self.ui.textEdit_comment.toPlainText().split('\n')))]
                    else:
                        comment = queue.Queue(); [comment.put(i) for i in self.ui.textEdit_comment.toPlainText().split('\n')]
                    if self.ui.checkBox_comment_link.isChecked():
                        id = random.sample(self.ui.textEdit_comment_link.toPlainText().split('\n'), int(self.ui.spinBox_comment.value()))
                    else:
                        id = [i for i in self.ui.textEdit_comment_link.toPlainText().split('\n')[:int(self.ui.spinBox_comment.value())]]

                    self.Info.ui.label.setText(f"Try Comment {name}.")
                    for i in id :
                        commet = comment.get()
                        result = Comment(i, commet, cookie).Start()  
                        self.Info.Add(result[1],name,'Edit',"Comment",f'{result[0]} {i}')
                        comment.put(commet)
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)    
            if self.ui.Share_check.isChecked() and self.is_running :
                if self.ui.textEdit_Share.toPlainText() :
                    id_share = random.sample(self.ui.textEdit_Share.toPlainText().split('\n'), int(self.ui.spinBox_share.value()))
                    self.Info.ui.label.setText(f"Try Share {name}.")
                    for i in id_share:
                        result = Share(i, '', cookie).Start()
                        self.Info.Add(result[1],name,'Edit',"Share",f'{result[0]} {i}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time) 
            if self.ui.Lock_Profile.isChecked() and self.is_running :
                self.Info.ui.label.setText(f"Try Lock Profile {name}.")
                result = lock_profile(cookie).Start()
                self.Info.Add(result[1],name,'Edit',"Lock Profile",f'{result[0]}')
                if result[1] == 1: self.succes += 1
                else: self.failed += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)  
            if self.ui.Change_Password_check.isChecked() and self.is_running :
                if not self.bot :
                    self.bot = yandex()
                new_password = self.Password()
                value = Chrom().change_password(password , new_password,cookie,self.bot)
                if value == "" : self.failed += 1
                else :
                    cursor.execute('UPDATE Account SET name = ? WHERE email = ?', (value[0], email))
                    cursor.execute('UPDATE Account SET password = ? WHERE email = ?', (value[1], email))
                    cursor.execute('UPDATE account SET cookies = ? WHERE email = ?', (value[2], email));conn.commit()
                    self.succes += 1
                self.Info.Update(s=self.succes,f=self.failed,o=self.order) ; self.Info.ui.label.setText(f"Waiting...") ; sleep(self.time)
            return 'succes'
        except Exception as e :
            self.Info.ui.label.setText(f"{name} Error Edit")
            self.Info.Add(0,name,'Edit',"Error",f'{e}')
    def Start(self):
        if self.ui.Number_Account.text() == '0': QMessage(text = 'No Account Selected').mainloop() ; self.ui.Start.setChecked(False)
        else:
            if self.is_running == False :
                self.ui.Start.setText("Stop")
                self.is_running = True
                self.Info.Update(0,0,0) ; self.succes=0 ; self.failed=0 
            elif self.is_running :
                self.ui.Start.setText("Start")
                self.ui.Start.setChecked(False)
                self.is_running = False ; self.bot=''
                return
            while not self.data.empty() :
                if self.is_running :
                    info = self.data.get()
                    self.Edit(info[1],info[2],info[3],info[5])
                else:break
                        
            self.Info.ui.label.setText("Finished")
            self.ui.Start.setText("Start")
            self.ui.Start.setChecked(False)
            self.is_running = False ; self.bot=''

    def Import_Text(self):
        button = self.sender()
        if button.objectName() == "checkBox_city" :
            with open("file_name", 'r', encoding='utf-8') as file:
                text_data = file.read()
            self.ui.textEdit_city.setPlainText(text_data)
        if button.objectName() == "checkBox_hometown" :
            with open("file_name", 'r', encoding='utf-8') as file:
                text_data = file.read()
            self.ui.textEdit_hometown.setPlainText(text_data)
        if button.objectName() == "checkBox_bio" :
            with open("file_name", 'r', encoding='utf-8') as file:
                text_data = file.read()
            self.ui.textEdit_bio.setPlainText(text_data)
        if button.objectName() == "checkBox_group" :
            with open("file_name", 'r', encoding='utf-8') as file:
                text_data = file.read()
            self.ui.textEdit_group.setPlainText(text_data)
        if button.objectName() == "checkBox_share" :
            with open("file_name", 'r', encoding='utf-8') as file:
                text_data = file.read()
            self.ui.textEdit_Share.setPlainText(text_data)
        
    def Import_DB(self):
        button = self.sender()
        if button.objectName() == "checkBox_city" :
            data = cursor.execute("SELECT * FROM city").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_city.setPlainText(text_data)
        if button.objectName() == "checkBox_hometown" :
            data = cursor.execute("SELECT * FROM city").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_hometown.setPlainText(text_data)
        if button.objectName() == "checkBox_work" :
            data = cursor.execute("SELECT * FROM Work").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_work.setPlainText(text_data)
        if button.objectName() == "checkBox_school" :
            data = cursor.execute("SELECT * FROM School").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_school.setPlainText(text_data)
        if button.objectName() == "checkBox_bio" :
            data = cursor.execute("SELECT * FROM bio").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_bio.setPlainText(text_data)
        if button.objectName() == "checkBox_group" :
            data = cursor.execute("SELECT * FROM groups").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_group.setPlainText(text_data)
        if button.objectName() == "checkBox_share" :
            data = cursor.execute("SELECT * FROM Share").fetchall()
            text_data = ""
            for row in data:
                text_data += f'{row[0]}\n'
            self.ui.textEdit_Share.setPlainText(text_data)