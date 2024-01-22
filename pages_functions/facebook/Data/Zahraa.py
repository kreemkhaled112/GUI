from init import *
from Edit import *
from Maokt import *
from Follow import *
from AddFriend import *
from JoinGroup import *
from Share import *
import sqlite3
import logging

class FacebooK:
    def __init__(self):
        self = self
        self.conn = sqlite3.connect('info.db')
        self.cursor = self.conn.cursor()
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system(f"title Kreem @ 2024 - Xcrazyxx")
        
    def Email(self):
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        user = ''.join(random.choices(chrs, k=6))                   
        list = ["teml.net","tmail.ws","moakt.cc"]
        rand = random.choice(list)
        m = Maokt(user,rand)
        email = (f"{user}@{rand}")
        return m , email
    def creat(self):
        Successfully = 0
        Failed = 0
        while True :
                Message , email = self.Email()
                self.cursor.execute('SELECT data FROM name ORDER BY RANDOM() LIMIT 1')

                random_item = self.cursor.fetchone()
                random_item = random_item[0]
                names = random_item.split()
                first_name = names[0]
                second_name = names[1]
                
                num = '0123456789'
                password = "Zahraa&3456"
                logging.getLogger('selenium').setLevel(logging.WARNING)
                
                options = webdriver.ChromeOptions()
                options.add_argument("--window-size=600,600")
                options.add_argument("--window-position=0,0")
                chrome_prefs = {"profile.default_content_setting_values.notifications": 2}
                # options.add_argument(f"--proxy-server=socks5://{proxy_ip}:{proxy_port}")
                options.add_experimental_option("prefs", chrome_prefs)
                options.add_experimental_option("detach", True)
                options.add_argument("--log-level=3")
                bot = webdriver.Chrome(options=options)
                print(Colorate.Diagonal(Colors.blue_to_green, f'[ Createing ] : [ {email}:{password} ]', 1))
                try:
                        bot.get("https://www.facebook.com/")  
                        try:
                                WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Allow all cookies']"))).click()
                        except:
                               pass
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a"))).click()

                        firstname = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='firstname']")))
                        firstname.send_keys(first_name)
                                

                        lastname = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='lastname']")))
                        lastname.send_keys(second_name)
                                
                
                        
                        reg_email__ = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='reg_email__']")))
                        reg_email__.send_keys(email)
                        reg_email__ = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input")))
                        reg_email__.send_keys(email)  
        
                        passwo = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input")))
                        passwo.send_keys(password)
                
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]/option[{random.randrange(1,11)}]"))).click() 
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]/option[{random.randrange(1,11)}]"))).click()       
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]/option[{random.randrange(20,25)}]"))).click()
                        
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input"))).click()
                        
                        
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button"))).click()
                except Exception as e: 
                        print(Colorate.Diagonal(Colors.white, f'[ Error ] : [ {e} ]', 1))
                        for i in range(60):
                                os.system(f"title Creat @ 2023 ^| Success: {Successfully} ^| Failed: {Failed} ^| Total: {(Failed + Successfully)} ^| Time: {59-i}")
                                sleep(1)
                        if Failed >= 3 :
                                input("........")
                        bot.quit()
                        continue
                try:
                        sleep(15)
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
                        try:
                               WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x6s0dn4 x78zum5 xl56j7k x1608yet xljgi0e x1e0frkt']"))).click()
                        except:
                               pass
                        cookies = bot.get_cookies()
                        format = {}
                        for cookie in cookies :
                                format[cookie['name']] = cookie['value']
                        cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
                        
                        name = Get_Name(cookie_string).Get()
                        username = re.search(r'c_user=(\d+)', cookie_string).group(1)
                        
                        try:
                                photo = Edit_Photo(f"photo\\{random.randrange(1,447)}.jpg",cookie_string).Edit_Photo()
                                if photo == "failed" :
                                       Failed += 1
                                       print(Colorate.Diagonal(Colors.red_to_blue, f'[ Error ] : [ {email}:{password} ]', 1))
                                       self.conn.commit()
                                       for i in range(60):
                                                os.system(f"title Creat @ 2023 ^| Success: {Successfully} ^| Failed: {Failed} ^| Total: {(Failed + Successfully)} ^| Time: {59-i}")
                                                sleep(1)
                                       if Failed >= 3 :
                                           pygame.mixer.init()
                                           pygame.mixer.music.load("error.mp3")
                                           pygame.mixer.music.play()
                                           input("........")
                                       bot.quit()
                                       continue
                                elif photo == "successfully" :
                                        Edit_Cover(f"cover\\{random.randrange(1,382)}.jpg",cookie_string)
                                        self.cursor.execute('SELECT bio FROM bio ORDER BY RANDOM() LIMIT 1')
                                        random_bio = self.cursor.fetchone()
                                        Edit_bio(random_bio,cookie_string)
                                        self.cursor.execute('SELECT data FROM city ORDER BY RANDOM() LIMIT 1')
                                        random_city = self.cursor.fetchone()
                                        Edit_City(random_city,cookie_string)
                                        Edit_Hometown(random_city,cookie_string)
                                        with open('test1.txt', 'r', encoding='utf-8') as file:
                                                all_lines = [line.strip() for line in file.readlines()]                                   
                                        random_lines = random.choice(all_lines)    
                                        Share(random_lines,"",cookie_string)
                                        id = ["100095218705319","Kreem.Khaled112"]
                                        Follow(id,cookie_string)
                                        try: 
                                                self.cursor.execute(f" SELECT username FROM account WHERE name IS NULL OR name = '' ORDER BY RANDOM() LIMIT 7 ") 
                                        except:
                                                self.cursor.execute('SELECT username FROM account ORDER BY RANDOM() LIMIT 7')
                                        id = self.cursor.fetchall()
                                        AddFriend(id,cookie_string)
                                        with open('group.txt', 'r', encoding='utf-8') as file:
                                                all_lines = [line.strip() for line in file.readlines()]                                    
                                        random_lines = random.sample(all_lines, 2)    
                                        random_lines.append("660551652726218")
                                        JoinGroup(random_lines,cookie_string)
                                        self.cursor.execute('INSERT INTO zahraa (name , email, password, username ,cookies) VALUES (  ?, ?, ?, ?, ?)', ( name , email, password, username, cookie_string))
                                        self.conn.commit()
                                        Successfully += 1
                                        print(Colorate.Diagonal(Colors.green_to_blue, f'[ Done Create Account ] : [ {email}:{password} ]', 1))
                                        os.system(f"title Creat @ 2023 ^| Success: {Successfully} ^| Failed: {Failed} ^| Total: {(Failed + Successfully)}")
                                        bot.quit()
                                else :
                                       input(f"[?] Error :{email}:{password}..... \n {e}")
                                       bot.quit()
                        except Exception as e:
                                Successfully += 1
                                print(Colorate.Diagonal(Colors.yellow_to_red, f'[ Error photo ] : [ {email}:{password} ]', 1))
                                os.system(f"title Creat @ 2023 ^| Success: {Successfully} ^| Failed: {Failed} ^| Total: {(Failed + Successfully)}")
                                self.cursor.execute('INSERT INTO edit (name , email, password, username ,cookies, gendar) VALUES ( ?, ?, ?, ?, ?, ?)', ( name , email, password, username, cookie_string,'Female'))
                                self.conn.commit()
                                bot.quit()         
                except:
                        Failed += 1
                        print(Colorate.Diagonal(Colors.red_to_blue, f'[ Error ] : [ {email}:{password} ]', 1))
                        self.conn.commit()
                        for i in range(60):
                                os.system(f"title Creat @ 2023 ^| Success: {Successfully} ^| Failed: {Failed} ^| Total: {(Failed + Successfully)} ^| Time: {59-i}")
                                sleep(1)
                        if Failed >= 3 :
                            pygame.mixer.init()
                            pygame.mixer.music.load("error.mp3")
                            pygame.mixer.music.play()
                            input("........")
                        bot.quit()
                                 
FB = FacebooK()
FB.creat()

