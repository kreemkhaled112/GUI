from init import *
from Edit import *
from Maokt import *
import sqlite3
class FacebooK:
    def __init__(self):
        self = self
        self.conn = sqlite3.connect('info.db')
        self.cursor = self.conn.cursor()
    def Email(self):
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        user = ''.join(random.choices(chrs, k=7))                   
        list = ["teml.net","tmail.ws","moakt.cc"]
        rand = random.choice(list)
        m = Maokt(user,rand)
        email = (f"{user}@{rand}")
        return m , email
    def creat(self):
        for i in range(100):
                Message , email = self.Email()

                self.cursor.execute('SELECT data FROM name ORDER BY RANDOM() LIMIT 1')

                random_item = self.cursor.fetchone()
                random_item = random_item[0]
                names = random_item.split()
                first_name = names[0]
                second_name = names[1]
                                                                        
                s = 2

                num = '0123456789'
                password = "015" + ''.join(random.choices(num, k=8))
      
                options = webdriver.ChromeOptions()
                chrome_prefs = {
                        "profile.default_content_setting_values.notifications": 2,  
                }
                # options.add_argument("--guest")
                options.add_experimental_option("prefs", chrome_prefs)
                options.add_experimental_option("detach", True)
                bot = webdriver.Chrome(options=options)
            
                try:
                        bot.get("https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr")  

                        firstname = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstname']")))
                        firstname.send_keys(first_name)
                                

                        lastname = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='lastname']")))
                        lastname.send_keys(second_name)
                                
                        reg_email__ = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='reg_email__']")))
                        reg_email__.send_keys(email)

                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='1']"))).click() 

                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div/div/div[2]/div[2]/table/tbody/tr/td/form/div[4]/div/div[1]/div[1]/div[2]/span/select[1]/option[{random.randrange(1,28)}]"))).click() 
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div/div/div[2]/div[2]/table/tbody/tr/td/form/div[4]/div/div[1]/div[1]/div[2]/span/select[2]/option[{random.randrange(1,11)}]"))).click()       
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div/div/div[2]/div[2]/table/tbody/tr/td/form/div[4]/div/div[1]/div[1]/div[2]/span/select[3]/option[{random.randrange(20,25)}]"))).click()
                        
                        passwo = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='reg_passwd__']")))
                        passwo.send_keys(password)
                        
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='submit']"))).click() 
                except Exception as e: 
                        print(e)          
                sleep(10)
                try:
                        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))
                        sleep(15)
                        try:
                                soup = BeautifulSoup(Message.Get_Message().content, 'html.parser')
                                message_elements = soup.find_all('div', class_='email-messages modal')
                                for element in message_elements:
                                        message = element.get_text().strip()
                                        code_pattern = r'FB-(\d+)'
                                        matches = re.findall(code_pattern, message)
                        except:
                                print("No Masseg")          

                        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))
                        button.send_keys(matches[0])
                               
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button"))).click()
                        sleep(5)
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div/a"))).click()
                        sleep(5)
                        cookies = bot.get_cookies()
                        format = {}
                        for cookie in cookies :
                                format[cookie['name']] = cookie['value']
                        cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
                        link = re.search(r'c_user=(\d+)', cookie_string).group(1)

                        try:     
                                Edit_Photo(f'photo\\{random.randrange(1,350)}.jpg',cookie_string).Edit_Photo()
                                self.cursor.execute('SELECT bio FROM bio ORDER BY RANDOM() LIMIT 1')
                                random_bio = self.cursor.fetchone()
                                Edit_bio(random_bio,cookie_string)
                                self.cursor.execute('SELECT data FROM city ORDER BY RANDOM() LIMIT 1')
                                random_city = self.cursor.fetchone()
                                Edit_City(random_city,cookie_string)
                                self.cursor.execute('INSERT INTO account (email, password, link ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?)', ( email, password, link, cookie_string,'Female'))
                                self.conn.commit()
                                print(f"Done Create Account ({email}:{password})")
                                bot.quit()
                        except Exception as e:
                                print(f"[?] Error photo:{email}..... \n {e}")
                                self.cursor.execute('INSERT INTO edit (email, password, link ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?)', ( email, password, link, cookie_string,'Female'))
                                self.conn.commit()
                                bot.quit()         
                except:
                        print(f"[?] Error:{email}:{password}..... \n")
                        if i == 30 :
                                bot.execute_script("window.open()")
                                bot.switch_to.window(bot.window_handles[-2])
                                bot.get("https://192.168.1.1/")
                                user = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[2]/div/div[1]/div/input")))
                                user.send_keys("admin")
                                sleep(1)
                                pas = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/input[1]")))
                                pas.send_keys("N7417937") 
                        sleep(60)
                        bot.quit()
                                 
FB = FacebooK()
FB.creat()
os.system('cls' if os.name == 'nt' else 'clear')
os.system(f"title Kreem @ 2024 - Xcrazyxx")
