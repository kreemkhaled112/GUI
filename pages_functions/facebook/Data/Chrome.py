from pages_functions.__init__ import *
from pages_functions.Facebook.Data.Edit import *

class Chrom:
    def __init__(self ,headless=None):
        self = self
        try:
            service = Service(executable_path="pages_functions/chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_extension('pages_functions/cookie.crx')
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2}
            # chrome_prefs = {"profile.default_content_setting_values.notifications": 2,"profile.managed_default_content_settings.images": 2}
            if headless:
                options.add_argument("--headless")
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            self.bot = webdriver.Chrome(service=service , options=options)
        except Exception as e:
            print(f"Failed to start the browser : \n{e}")

    def Login(self,email, password):
        try:
            self.bot.get("https://business.facebook.com/login/")
            wait = WebDriverWait(self.bot, 5)
            try:self.bot.find_element(By.XPATH, '//button[@data-cookiebanner="accept_button"]').click()
            except:pass
            y = "document.cookie = " + "'" + 'wd=500x158' + "; domain=.facebook.com" + "'"
            self.bot.execute_script(y)
            sleep(.5)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys(email)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='pass']"))).send_keys(password)
            sleep(1)
            try:wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='loginbutton']"))).click()
            except:pass
            sleep(4)
            self.bot.get("https://mbasic.facebook.com/profile.php?") ; sleep(3)
            cookies = self.bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            name = self.bot.title
            if name == "" :
                name =  "CheckPoint" 
            self.bot.quit()
            return 'success' , cookie_string , name
        except Exception as e : return e
        
    def View(self,cook,view=None,close=None):
        try:
            cookies = cook.replace(" ", "").split(";")
            if view == 'view':
                self.bot.get("https://www.facebook.com/")
                for cookie in cookies:
                    cookie_parts = cookie.split("=")
                    if len(cookie_parts) == 2:
                        cookie_name, cookie_value = cookie_parts
                        self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://mbasic.facebook.com/")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://mbasic.facebook.com/profile.php?") ; sleep(3)
            
            name = self.bot.title
            if name == "" :
                name =  "CheckPoint" 
            cookie_string = self.update_cookie(cook)
            if close == 'close':self.bot.quit()
            return  name , cookie_string
        except Exception as e : print(e) ; return ''
    def Epsilon(self,cook,yandex):
        try:
            self.bot.get("https://mbasic.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://mbasic.facebook.com/profile.php?")
            if 'checkpoint' in self.bot.current_url :
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[7]/a"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[3]/a"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/form/div/div[3]/input"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/form/div/div[4]/input"))).click()
                sleep(20)
                yandex.refresh()
                sleep(5)
                soup = BeautifulSoup(yandex.page_source, 'html.parser')
                message_elements = soup.find_all('div', class_='ns-view-container-desc mail-MessagesList js-messages-list')
                for element in message_elements:
                    message = element.get_text().strip()
                    match = re.search(r'Your security code is: (\d+)', message)
                    if match:
                        code = match.group(1)
                        break
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[2]/form/div[1]/div/div/input"))).send_keys(code)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[2]/form/div[3]/input"))).click() ; sleep(1)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[3]/a"))).click() ; sleep(1)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[4]/a"))).click() ; sleep(1)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[4]/a"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[7]/a"))).click()
            self.bot.get("https://mbasic.facebook.com/profile.php?") ; sleep(3)
            
            cookie_string = self.update_cookie(cook)
            name = self.bot.title
            if name == "" :
                name =  "CheckPoint" 
            self.bot.quit()
            return name , cookie_string
        except Exception as e : print(e) ; return ''
    def Moakt(self,user,cook):
        try:
            self.bot.get('https://moakt.com/ar')
            sleep(1)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/span[3]/input"))).send_keys(user)
            WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/input[2]"))).click()
            self.bot.execute_script("window.open()")
            self.bot.switch_to.window(self.bot.window_handles[-1])
            self.bot.get("https://mbasic.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://mbasic.facebook.com/profile.php?")
            if 'checkpoint' in self.bot.current_url :
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[7]/a"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[3]/a"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/form/div/div[3]/input"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/form/div/div[4]/input"))).click()
                code = input("code: ")
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[2]/form/div[1]/div/div/input"))).send_keys(code)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[2]/form/div[3]/input"))).click() ; sleep(1)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[3]/a"))).click() ; sleep(1)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[4]/a"))).click() ; sleep(1)
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[4]/a"))).click()
                WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[7]/a"))).click()
            input("......")
            cookie_string = self.update_cookie(cook)
            name = self.bot.title
            if name == "" :
                name =  "CheckPoint" 
            self.bot.quit()
            return name , cookie_string
        except Exception as e : print(e) ; return ''
    def Change(self,email,cook,yandex):
        try:
            self.bot.get("https://mbasic.facebook.com/settings/email/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.refresh()
            WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Add email address')]"))).click()
            WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))).send_keys(email)
            WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='save']"))).click()
            WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/span[2]/div/a'))).click()
            sleep(20)
            yandex.refresh()
            sleep(5)
            soup = BeautifulSoup(yandex.page_source, 'html.parser')
            message_elements = soup.find_all('div', class_='ns-view-container-desc mail-MessagesList js-messages-list')
            for element in message_elements:
                message = element.get_text().strip()
                match = re.search(r'this confirmation code: (\d+)', message)
                if match:
                    code = match.group(1)
                    break
            if not code :
                code = input("Enter Code")
            WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='code']"))).send_keys(code) ; sleep(2)
            pyautogui.press('enter') ; sleep(5)
            try:WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='submit']"))).click() 
            except:pass
            self.bot.get("https://mbasic.facebook.com/profile.php?") ; sleep(3)
            cookie_string = self.update_cookie(cook)
            name = self.bot.title
            if name == "" :
                name =  "CheckPoint" 
            self.bot.quit()
            return name ,email, cookie_string
        except Exception as e : print(e) ; return ''
    def change_password(self,old,new,cook,yandex):
        try:
            cookie(cook,self.bot)
            self.bot.get("https://accountscenter.facebook.com/password_and_security/password/change")

            WebDriverWait(self.bot, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/span[2]'))).click()
            WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[3]/div/div/div[1]/input"))).send_keys(old)
            WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[4]/div/div/div[1]/input"))).send_keys(new)
            WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[5]/div/div/div[1]/input"))).send_keys(new)
            # checkbox = WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='checkbox']")))
            # if checkbox.is_selected():
            #     checkbox.click()
            WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[4]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/span/span"))).click() ; sleep(5)
            try:
                WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/form/div/div/div/div/div[1]/input")))
                sleep(10)
                yandex.refresh()
                sleep(5)
                soup = BeautifulSoup(yandex.page_source, 'html.parser')
                message_elements = soup.find_all('div', class_='ns-view-container-desc mail-MessagesList js-messages-list')
                for element in message_elements:
                    message = element.get_text().strip()
                    match = re.search(r'Your security code is: (\d+)', message)
                    if match:
                        code = match.group(1)
                        break
                if not code :
                    code = input("Enter Code")
                WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/form/div/div/div/div/div[1]/input"))).send_keys(code)
                WebDriverWait(self.bot, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/span/span'))).click() 
            except: pass
            sleep(10) ; self.bot.get("https://mbasic.facebook.com/profile.php?") ; sleep(3)
            cookie_string = self.update_cookie(cook)
            name = self.bot.title
            if name == "" :
                name =  "CheckPoint" 
            self.bot.quit()
            return name ,new, cookie_string
        except Exception as e : print(e) ; return ''
    def update_cookie(self,cook):
        cookies = self.bot.get_cookies()
        format = {}
        for cookie in cookies :
            format[cookie['name']] = cookie['value']
        cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
        try:
            cursor.execute(f"UPDATE account SET cookies = '{cookie_string} ' WHERE cookies = '{cook}'") ;conn.commit()
            return cookie_string
        except Exception as e : print(f"Faild Contect Database \n {e}")
        
    
    def scrap(self,id,cook):
        bot = self.bot
        files_in_folder = os.listdir('photo')
        largest_number = None
        for file_name in files_in_folder:
            numbers = file_name.replace(".jpg", "")
            numbers = [int(num) for num in numbers.split()]
            if numbers:
                current_largest = max(numbers)
                if largest_number is None or current_largest > largest_number:
                    largest_number = current_largest
        bot.get("https://www.facebook.com/")
        self.Add_cookie(cook)
        
        for user in id :
            bot.get(f"https://www.facebook.com/profile.php?id={user}")
            sleep(2)
            try:
                button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='x1jx94hy x14yjl9h xudhj91 x18nykt9 xww2gxu x1iorvi4 x150jy0e xjkvuk6 x1e558r4']")))
                button.click()
                sleep(2)
                imag = bot.find_elements(By.CSS_SELECTOR, "img[class='x1bwycvy x193iq5w x4fas0m x19kjcj4']")

                p = [element.get_attribute('src') for element in imag]
                response = requests.get(p[0])
                open(f"photo/{largest_number+1}.jpg", "wb").write(response.content)
                largest_number += 1
            except:
                print("Not Found Photo")
