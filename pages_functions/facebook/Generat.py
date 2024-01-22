from pages_functions.__init__ import *

from ui.pages_face.Generat_ui import Ui_Form
from pages_functions.__init__ import *
from pages_functions.function_face.Data.Edit import *
from pages_functions.function_face.Data.Email import *
from pages_functions.function_face.Data.Follow import *
from pages_functions.function_face.Data.AddFriend import *
from pages_functions.function_face.Data.JoinGroup import *
from pages_functions.function_face.Data.Chrome import *
from pages_functions.function_face.Data.Share import *

class Generat(QWidget):
    def __init__(self):
        super(Generat, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        with open("static\style.qss", "r",encoding='utf-8') as style_file:
            style_str = style_file.read()
        self.setStyleSheet(style_str)
        self.is_running = False
        self.Error = 3
        self.Error1 = 600
        self.mp3 = "Data\\error.mp3"
        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        for i in range(self.ui.stackedWidget.count()):
            self.ui.stackedWidget.widget(i).setVisible(False)
        self.ui.widget_2.hide()
        self.ui.widget_4.hide()
        self.ui.widget_6.hide()

        self.ui.Add_Profile.stateChanged.connect(lambda state: self.toggle_page(state, 0))
        self.ui.Add_Cover.stateChanged.connect(lambda state: self.toggle_page(state, 1))
        self.ui.Add_City.stateChanged.connect(lambda state: self.toggle_page(state, 2))
        self.ui.Add_Home.stateChanged.connect(lambda state: self.toggle_page(state, 3))
        self.ui.AddPost.stateChanged.connect(lambda state: self.toggle_page(state, 4))
        self.ui.Add_Friend.stateChanged.connect(lambda state: self.toggle_page(state, 5))
        self.ui.Add_Share.stateChanged.connect(lambda state: self.toggle_page(state, 6))
        self.ui.Join_Groub.stateChanged.connect(lambda state: self.toggle_page(state, 7))
        self.ui.Edit_Bio.stateChanged.connect(lambda state: self.toggle_page(state, 8))
        self.ui.Follow.stateChanged.connect(lambda state: self.toggle_page(state, 9))
        self.ui.Like.stateChanged.connect(lambda state: self.toggle_page(state, 10))
        self.ui.Creat.clicked.connect(lambda : Thread(target=self.Start).start())

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
                    return random_item , 'male'
                elif self.ui.radioButton_2.isChecked(): 
                    random_item = cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone()
                    return random_item , 'female'
                elif self.ui.radioButton_3.isChecked():
                    random_item = cursor.execute("SELECT data FROM name ORDER BY RANDOM() LIMIT 1").fetchone() 
                    return random_item
                else: QMessageBox.warning(self, 'No Name Selected', 'Please select an option.')
            else: QMessageBox.warning(self, 'No Name Selected', 'Please select an option.')
    def Email(self):
        if self.ui.lineEdit_2.text() : return self.ui.lineEdit_2.text() , 'text'
        else:
            if self.ui.checkBox_2.isChecked() :
                if self.ui.radioButton_4.isChecked():
                    chrs = 'abcdefghijklmnopqrstuvwxyz'
                    chrs = ''.join((chrs, '0123456789'))
                    user = ''.join(random.choices(chrs, k=random.randrange(8,12)))                   
                    list = ["teml.net","tmail.ws","moakt.cc"]
                    rand = random.choice(list)
                    self.Message = Maokt(user,rand)
                    email = (f"{user}@{rand}")
                    return email , 'Moakt'
                elif self.ui.radioButton_5.isChecked():
                    self.Message = Mohmal()
                    email = Message.Get_Random()
                    return email , 'Mohmal'
                elif self.ui.radioButton_6.isChecked():
                    return 'mailtm'
                else: QMessageBox.warning(self, 'No Email Selected', 'Please select an option.')
            else: QMessageBox.warning(self, 'No Email Selected', 'Please select an option.')
    def Password(self):
        if self.ui.lineEdit_3.text() : return self.ui.lineEdit_3.text()
        else:
            if self.ui.checkBox_3.isChecked() : return self.Generat_password()
            else:
                QMessageBox.warning(self, 'No Password Selected', 'Please select an option.')
    def Generat_password(self):
        chrs = ''
        text1 = self.ui.lineEdit_4.text() if self.ui.lineEdit_4.text() is not None else ''
        if self.ui.checkBox_4.isChecked() :
            chrs += '0123456789'
        if self.ui.checkBox_5.isChecked() :
            chrs += 'abcdefghijklmnopqrstuvwxyz'
        value =  int(self.ui.spinBox.value())
        password = text1 + ''.join(random.choices(list(chrs) if chrs else '', k=value))
        self.ui.Generat_Password_2.setText(password)
        return password
        
    def Start(self):
        if self.is_running == False :
            self.ui.Creat.setText("Stop")
            self.is_running = True
        elif self.is_running :
            self.ui.Creat.setText("Creat")
            self.is_running = False
        Successfully = 0
        Failed = 0
        while self.is_running :
            result = self.Creat()
            if result == 'success':
                result = self.Edit()
                if result == 'success':
                    self.bot.refresh()
                    WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                    cookies = self.bot.get_cookies()
                    format = {}
                    for cookie in cookies :
                            format[cookie['name']] = cookie['value']
                    cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
                    cursor.execute('INSERT INTO account (name , email, password, username ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?, ?)', ( self.name , self.email, self.password, self.username, cookie_string,self.gender)) ;conn.commit()
                    Successfully += 1
                    print(Colorate.Diagonal(Colors.green_to_blue, f'[ Done Create Account ] : [ {self.email}:{self.password} ]', 1))
                    self.Update(str(Successfully),str(Failed),time=str(0))
                    self.bot.quit()
                elif result == 'Error photo':
                    print(Colorate.Diagonal(Colors.yellow_to_red, f'[ Error photo ] : [ {self.email}:{self.password} ]', 1))
                    cursor.execute('INSERT INTO edit (name , email, password, username ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?, ?)', ( self.name , self.email, self.password, self.username, cookie_string,self.gender))
                    conn.commit()
                    self.Update(Successfully,Failed,time=0)
                    self.bot.quit()
                elif result == 'failed':
                    print(Colorate.Diagonal(Colors.red_to_blue, f'[ Error ] : [ {self.email}:{self.password} ]', 1))
                    conn.commit()
                    for i in range(60):
                        self.Update(Successfully,Failed,time=59-i)
                        sleep(1)
                    if Failed >= self.Error :
                        pygame.mixer.init()
                        pygame.mixer.music.load(self.mp3)
                        pygame.mixer.music.play()
                        for i in range(600):
                            self.Update(Successfully,Failed,time=599-i)
                            sleep(1)
                        Failed = 0
                    self.bot.quit()
            elif result == 'Failed Start Chrome':
                print('Failed Start Chrome')
            elif result == 'No Masseg':
                print('No Masseg')
            elif result == 'Failed':
                print('Failed')
    def Update(self,successful,faild,time):
        self.ui.successful.setText(successful)
        self.ui.faild.setText(successful)
        self.ui.total.setText(successful+faild)
        self.ui.time.setText(time)

    def Creat(self):
        Name , self.gender = self.Name()
        self.name = Name[0].split()
        first_name = self.name[0]
        second_name = self.name[1]

        self.email , type = self.Email()
        
        self.password = self.Password()
        try:
            options = webdriver.ChromeOptions()
            options.add_argument(f"--window-size=600,600")
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2,"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(options=options)
            bot = self.bot
            print(Colorate.Diagonal(Colors.blue_to_green, f'[ Createing ] : [ {self.email}:{self.password} ]', 1))
            try:
                bot.get("https://www.facebook.com/")  
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a"))).click()
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstname']"))).send_keys(first_name)    
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='lastname']"))).send_keys(second_name)
                
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='reg_email__']"))).send_keys(self.email)
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input"))).send_keys(self.email)  

                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input"))).send_keys(self.password)
        
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]/option[{random.randrange(1,11)}]"))).click() 
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]/option[{random.randrange(1,11)}]"))).click()       
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]/option[{random.randrange(20,25)}]"))).click()
                if self.gender == 'female':
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input"))).click()
                elif self.gender == 'male':
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input"))).click()
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button"))).click()
                try:
                    sleep(15)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))
                    sleep(15)
                    try:
                        if type == 'text' :
                            matches = [input('Enter Code : ')]
                        if  type == 'Moakt':
                            soup = BeautifulSoup(self.Message.Get_Message().content, 'html.parser')
                            message_elements = soup.find_all('div', class_='email-messages modal')
                            for element in message_elements:
                                message = element.get_text().strip()
                                code_pattern = r'FB-(\d+)'
                                matches = re.findall(code_pattern, message)
                        elif type == 'Mohmal':
                            soup = BeautifulSoup(self.Message.Get_Message().content, 'html.parser')
                            message_elements = soup.find_all('div', class_='email-messages modal')
                            for element in message_elements:
                                    message = element.get_text().strip()
                                    code_pattern = r'FB-(\d+)'
                                    matches = re.findall(code_pattern, message)
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input"))).send_keys(matches[0]) 
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button"))).click()
                        sleep(5)
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div/a"))).click()
                        sleep(5)
                        try:WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='OK']"))).click()
                        except:pass
                        cookies = bot.get_cookies()
                        format = {}
                        for cookie in cookies :
                                format[cookie['name']] = cookie['value']
                        self.cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
                        self.name = Get_Name(self.cookie_string).Get()
                        self.username = re.search(r'c_user=(\d+)', self.cookie_string).group(1)
                        return 'success'
                    except:
                        return "No Masseg"       
                except:
                    return 'Failed'
            except Exception as e: return 'Failed'
        except:
            return 'Failed Start Chrome'
    def Edit(self):
        return 'success'
