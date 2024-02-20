from pages_functions.__init__ import *

from ui.Public.Generat_ui import Ui_Form
from pages_functions.Public.Info import Info
from pages_functions.Public.Edit import Edit
from pages_functions.Facebook.Data.Edit import *
from pages_functions.Facebook.Data.Email import *
from pages_functions.Facebook.Data.Follow import *
from pages_functions.Facebook.Data.AddFriend import *
from pages_functions.Facebook.Data.JoinGroup import *
from pages_functions.Facebook.Data.Chrome import *
from pages_functions.Facebook.Data.Share import *

class Generat_Face(QWidget):
    def __init__(self):
        super(Generat_Face, self).__init__()
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
        self.ui_Edit.ui.widget_Select.hide()
        self.ui_Edit.Info.ui.table.setColumnHidden(3, True)

        self.ui_Edit.ui.Start.setText("Creat")
        self.ui_Edit.Info.ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("Name : Password"))
        self.ui_Edit.Info.ui.table.setColumnWidth(2, 200)

        self.ui.Generat_Password_2.clicked.connect(self.Generat_password)
        self.ui_Edit.ui.Start.clicked.connect(lambda : Thread(target=self.Generat).start())
        
    def Name(self):
        if self.ui.lineEdit.text() : return self.ui.lineEdit.text() , self.Gender()
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
                    return random_item ,"female"
                else: QMessage( text = 'No Gender Selected \n Please select an option.').mainloop() ;return None , None
            else: QMessage( text = 'No Name Selected \n Please select an option.').mainloop() ;return None , None
    def Gender(self):
        if self.ui.radioButton.isChecked():
            return "male"
        elif self.ui.radioButton_2.isChecked():
            return "female"
        elif self.ui.radioButton_3.isChecked():
            return "female"
        else: QMessage( text = ' No Gender Selected \n Please select an option.').mainloop() ;return None
    def Email(self):
        if self.ui.lineEdit_2.text() : return self.ui.lineEdit_2.text() , 'text'
        else:
            if self.ui.checkBox_2.isChecked() :
                chrs = 'abcdefghijklmnopqrstuvwxyz'
                # chrs = ''.join((chrs, '0123456789'))
                user = ''.join(random.choices(chrs, k=random.randrange(8,10)))
                if self.ui.radioButton_4.isChecked():        
                    list = ["teml.net","tmail.ws","moakt.cc"]
                    rand = random.choice(list)
                    self.Message = Maokt(user,rand)
                    email = (f"{user}@{rand}")
                    return email , 'Moakt'
                elif self.ui.radioButton_5.isChecked():
                    self.Message= Mail_Tm(user,"123456789")
                    return self.Message.address , 'Mail'
                elif self.ui.radioButton_6.isChecked():
                    return 'mailtm'
                else: QMessage(text = 'No Email Selected \n Please select an option.').mainloop() ;return None , None
            else: QMessage(text = 'No Email Selected \n Please select an option.').mainloop() ;return None , None
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
    
    def Creat(self):
        self.name , self.gender = self.Name()
        if not self.name : return "stop"
        if not self.gender : return "stop"
        self.email , type = self.Email()
        if not self.email: return "stop"
        self.password = self.Password()
        if not self.password : return "stop"

        self.name = self.name[0].split()
        first_name = self.name[0]
        second_name = self.name[1]

        self.ui_Edit.Info.ui.label.setText(f"Createing {self.email}:{self.password}")
        try:
            service = Service(executable_path="pages_functions/chromedriver.exe")
            options = webdriver.ChromeOptions()
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2,"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(service=service , options=options)
            bot = self.bot
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
                    sleep(20)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))
                    sleep(15)
                except:
                    self.failed +=1
                    self.message(0,"Checkpoint")
                    self.bot.quit()
                    return
                try:
                    if type == 'text' :
                        matches = [input('Enter Code : ')]
                        self.ui.lineEdit_2.setText("")
                    if  type == 'Moakt':
                        soup = BeautifulSoup(self.Message.Get_Message().content, 'html.parser')
                        message_elements = soup.find_all('div', class_='email-messages modal')
                        for element in message_elements:
                            message = element.get_text().strip()
                            code_pattern = r'FB-(\d+)'
                            matches = re.findall(code_pattern, message)
                    elif type == 'Mail':
                        m = self.Message.Get_Message()
                        matches = re.findall(r'FB-(\d+)', m['subject'])
                except:
                    self.failed +=1
                    self.message(2,"No Message")
                    return
                    
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
                self.username = re.search(r'c_user=(\d+)', self.cookie_string).group(1)
                try: 
                    result = self.ui_Edit.Edit(first_name,self.cookie_string)
                    if result == 'succes' :
                        self.bot.refresh()
                        WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                        cookies = self.bot.get_cookies()
                        format = {}
                        for cookie in cookies :
                                format[cookie['name']] = cookie['value']
                        cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
                        cursor.execute('INSERT INTO account (groupname, name , email, password, username ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?, ?, ?)', ( "Generat" ,f'{first_name} {second_name}' , self.email, self.password, self.username, cookie_string,self.gender)) ;conn.commit()
                        self.success += 1
                        self.message(1,'Done Create Account')
                        self.bot.quit()
                    elif result == 'Error photo':
                        cursor.execute('INSERT INTO edit (groupname, name , email, password, username ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?, ?, ?)', ( "Generat" ,self.name , self.email, self.password, self.username, cookie_string,self.gender)) ;conn.commit()
                        self.failed +=1
                        self.message(2,"Error photo")
                        self.bot.quit()
                    elif result == 'Error Edit':
                            self.failed +=1
                            self.message(2,"Error Edit")
                            self.bot.quit()
                except Exception as e:
                    self.failed +=1
                    self.message(2,f"Error Edit {e}")
            except Exception as e: 
                self.failed +=1
                self.message(0,e)
        except Exception as e :  
            self.message(0,"Failed Start Chrome")
            self.ui_Edit.ui.Start.setText("Creat")
            self.ui_Edit.ui.Start.setChecked(False)
            self.is_running = False
             
    def Generat(self):
        if self.is_running == False :
            self.ui_Edit.ui.Start.setText("Stop")
            self.is_running = True
        elif self.is_running :
            self.ui_Edit.ui.Start.setText("Creat")
            self.ui_Edit.ui.Start.setChecked(False)
            self.is_running = False
        self.success = 0
        self.failed = 0
        while self.is_running :
            result = self.Creat()
            if result == "stop" :
                self.ui_Edit.ui.Start.setText("Creat")
                self.ui_Edit.ui.Start.setChecked(False)
                self.is_running = False
