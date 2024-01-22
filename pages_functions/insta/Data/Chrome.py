from pages_functions.__init__ import *

class Chrom_Insta:
    def __init__(self):
        self = self
        try:
            self.options = webdriver.ChromeOptions()
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2}
            self.options.add_experimental_option("prefs", chrome_prefs)
            self.options.add_experimental_option("detach", True)
            self.options.add_argument('--incognito')
            self.options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(options=self.options)
        except Exception as e:
            print(f"Failed to start the browser : \n{e}")
    def face(self,email,pas,cook):
        self.bot.get("https://www.facebook.com/")
        cookies = cook.strip().split(";")
        for cookie in cookies:
            cookie_parts = cookie.split("=")
            if len(cookie_parts) == 2:
                cookie_name, cookie_value = cookie_parts
                self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
        self.bot.get("https://www.facebook.com/profile.php?")

        if "checkpoint"  not in self.bot.current_url :
            try:
                elment = WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='_585r _50f4']")))
                if elment:
                    WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']"))).send_keys(email)
                    WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']"))).send_keys(pas)
                    WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Log in']"))).click()
                    if input('Delete or Skip : ')== '' :
                        self.update_cookies(cook)
                    else:
                        cursor.execute(f'DELETE FROM account WHERE cookies = "{cook}" ')
                        conn.commit()
                        return 'Faild'
            except:self.update_cookies(cook)
        else :
            if input('Delete or Skip : ') == '' :self.update_cookies(cook)
            else:
                cursor.execute(f'DELETE FROM account WHERE cookies = "{cook}" ')
                conn.commit()
                return 'Faild'
    def update_cookies(self,cook):
        try:
            cookies = self.bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            try:cursor.execute(f"UPDATE account SET cookies = '{cookie_string} ' WHERE cookies = '{cook}'") ;conn.commit()
            except Exception as e :print(f"Faild Contect Database \n {e}")
        except :print("Faild Update Cookie")
    
    def Get_cookie(self):
        cookies = self.bot.get_cookies()
        format = {}
        for cookie in cookies :
            format[cookie['name']] = cookie['value']
        cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
        return cookie_string
    
    def update_cookie(self, username, cook):
        try:
            cookie_string = self.Get_cookie()

            try: cursor.execute(f"UPDATE insta SET cookies = '{cookie_string} ' WHERE username = '{username}'") ;conn.commit()
            except Exception as e : print(f"Faild Contect Database \n {e}")
            
        except :print("Faild Get Cookie")

    def login(self,email, password):
        bot = self.bot
        bot.get("https://instagram.com/")
        try:
            sleep(random.randrange(2,5))
            username = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Phone number, username, or email']")))
            username.send_keys(email.strip())
            sleep(random.randrange(2,5))
            password_field = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Password']")))
            password_field.send_keys(password.strip())
            sleep(random.randrange(2,5))
            WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()    
            sleep(random.randrange(5,10))
            WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acas _aj1- _ap30']"))).click()    
        except : pass
        if input("Get_cookies OR Ban : ") == '':
            return self.Get_cookie()
        else:
            bot.quit()
            return 'Ban'
    
    def View(self,username,cook):
        bot = self.bot
        bot.get("https://www.instagram.com/")
        cookies = cook.split(";")
        for cookie in cookies:
            cookie_parts = cookie.split("=")
            if len(cookie_parts) == 2:
                cookie_name, cookie_value = cookie_parts
                bot.add_cookie({'name': cookie_name, 'value': cookie_value})
        bot.get("https://www.instagram.com")
        if input("Get_cookies OR Ban : ") == '':
            return  self.update_cookie(username,cook)
        else:
            bot.quit()
            return 'Ban'
        
    def switch(self,email,name,password,cook,pas):
        bot = self.bot
        f = self.face(email,pas,cook)
        if f == 'Faild':return None , None
        else:
            bot.get("https://www.instagram.com/")
            try:
                sleep(random.randrange(2,5))
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='_ab37']"))).click()
                sleep(random.randrange(2,5))
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/form/div/div[1]/div[1]/div/div/div[3]/button[1]"))).click()
                    sleep(random.randrange(5,10))
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acaq _acas _aj1- _ap30']"))).click()
                    sleep(random.randrange(5,10))
                    Password = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Password']")))
                    Password.send_keys(password.strip())
                    sleep(random.randrange(5,10))
                    Email = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Email']")))
                    Email.send_keys(email.strip())
                    sleep(random.randrange(5,10))
                    # Name = WebDriverWait(bot, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Full Name']")))
                    # Name.send_keys(Keys.CONTROL, 'a')
                    # Name.send_keys(Keys.DELETE)
                    # Name.send_keys(name.strip())
                    try:
                        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acao _acas _aj1- _ap30']"))).click()
                        sleep(random.randrange(10,15))
                    except:input('continue..')
                    Username = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Username']"))).get_attribute("value")
                    
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
                    sleep(20)
                    if "signup"  not in self.bot.current_url:
                        cookie_string = self.Get_cookie()
                        input("Get_cookies OR Ban : ")
                    else  :
                        cookie_string = self.login(email,password)
                    return Username , cookie_string
                except:
                    return None,None
            except Exception as e :print(e)
    def Add_Photo(self,photo):
        try:
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[1]/div/div/span"))).click()
            try:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Add a profile photo"]'))).click()
            except:
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt="Change profile photo"]'))).click()
                try:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="_a9-- _ap36 _a9_0"]'))).click()
                except:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="_a9-- _ap37 _a9_0"]'))).click()
            sleep(1)
            pg.write(photo)
            pg.press('enter')
            sleep(random.randrange(2,5))
            return 'successfully'
        except:return 'Ban'
    def Add_Cover(self,photo):
        try:
            try:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[2]/div[2]/div/div[4]"))).click()
            except:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/div/div[4]"))).click()
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acas _aj1- _ap30']"))).click()
            sleep(2)
            pg.write(photo)
            pg.press('enter')
            sleep(2)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div"))).click()
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div"))).click()
            sleep(1)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"))).click()
            sleep(random.randrange(5,10))
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Close']"))).click()
            sleep(random.randrange(2,5))
        except:pass
    
    def Edit_Bio(self,bio):
        try:
            self.bot.get('https://www.instagram.com/accounts/edit/')
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Close']"))).click()
            sleep(2)
            try:
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[id="pepBio"]'))).click();pg.write(bio.strip())
                sleep(1)
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Down chevron"]'))).click()
                sleep(1)
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[2]/div[1]"))).click()
                try:WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class=" _acan _acap _acas _acav _aj1- _ap30"]'))).click()
                except:pass
            except:
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="pepGender"]'))).send_keys('Male')
            WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/div/form/div[4]/div'))).click()
            sleep(random.randrange(2,5))
        except:pass
    
    def changepassword(self,old_password,password):
        try:
            self.bot.get('https://www.instagram.com/accounts/password/change/')
            try:WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Close']"))).click()
            except:pass
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='current-password']"))).send_keys(old_password)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[autocomplete='new-password']"))).send_keys(password)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='cppConfirmPassword']"))).send_keys(password)
            try:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[3]/div/form/div[4]/div/div/div"))).click()
            except:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/article/form/div[4]/div/div/div"))).click()
            sleep(random.randrange(5,10))
            return 'success'
        except:pass
    
    def profrssional(self):
        try:
            self.bot.get("https://www.instagram.com/accounts/convert_to_professional_account/")
            sleep(1)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div[1]/div[2]/div/div[1]/div[1]"))).click()
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acas _acav _aj1- _ap30']"))).click()
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acas _acav _aj1- _ap30']"))).click()
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='2201']"))).click()
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acas _acav _aj1- _ap30']"))).click()
            try:WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='_a9-- _ap36 _a9_0']"))).click()
            except:pass
            sleep(15)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acas _acav _aj1- _ap30']"))).click()
            return 'successfully'
        except:pass
    