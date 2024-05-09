from pages_functions.__init__ import *
from pages_functions.Facebook.Data.Edit import *

class Chrom:
    def __init__(self):
        self = self
        try:
            service = Service(executable_path="pages_functions/chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_extension('pages_functions/cookie.crx')
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2}
            # chrome_prefs = {"profile.default_content_setting_values.notifications": 2,"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(service=service , options=options)
        except Exception as e:
            print(f"Failed to start the browser : \n{e}")

    def Login(self,email, password):
        try:
            bot = self.bot
            bot.minimize_window()
            bot.get("https://business.facebook.com/login/")
            wait = WebDriverWait(bot, 2)
            try:bot.find_element(By.XPATH, '//button[@data-cookiebanner="accept_button"]').click()
            except:pass
            y = "document.cookie = " + "'" + 'wd=500x158' + "; domain=.facebook.com" + "'"
            bot.execute_script(y)
            sleep(.5)
            usinp = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
            sleep(0.3)
            usinp.send_keys(email.strip())
            usinp1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='pass']")))
            sleep(0.3)
            usinp1.send_keys(password.strip())
            sleep(0.3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='loginbutton']"))).click()
            sleep(7)
            cookies = bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            self.bot.quit()
            return 'success' , cookie_string , Get_Name(cookie_string).Get()
        except Exception as e : return e
        
    def View(self,cook,close=None):
        try:
            self.bot.get("https://mbasic.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://mbasic.facebook.com/profile.php?")
            cookie_string = self.update_cookie(cook)
            if close == 'close':self.bot.quit()
            return  Get_Name(cookie_string).Get() , cookie_string
        except : return ''
    def Epsilon(self,cook,yandex):
        try:
            self.bot.get("https://mbasic.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.refresh()
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
            cookie_string = self.update_cookie(cook)
            self.bot.quit()
            return Get_Name(cookie_string).Get() , cookie_string
        except Exception as e : print(e) ; return ''
    def Change(self,cook,yandex):
        try:
            self.bot.get("https://mbasic.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.refresh()
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
            cookie_string = self.update_cookie(cook)
            self.bot.quit()
            return Get_Name(cookie_string).Get() , cookie_string
        except Exception as e : print(e) ; return ''
    def update_cookie(self,cook):
        try:
            cookies = self.bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            try:
                cursor.execute(f"UPDATE account SET cookies = '{cookie_string} ' WHERE cookies = '{cook}'") ;conn.commit()
                return cookie_string
            except Exception as e : print(f"Faild Contect Database \n {e}")
        except : print("Faild Update Cookie")
    
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
