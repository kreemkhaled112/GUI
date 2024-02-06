from pages_functions.__init__ import *
from pages_functions.Facebook.Data.Edit import *

class Chrom:
    def __init__(self):
        self = self
        try:
            service = Service(executable_path="pages_functions/chromedriver.exe")
            options = webdriver.ChromeOptions()
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2,"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(service=service , options=options)
        except Exception as e:
            print(f"Failed to start the browser : \n{e}")

    def Login(self,email, password):
        try:
            bot = self.bot
            self.bot.get("https://mbasic.facebook.com/login/")
            try: WebDriverWait(self.bot, 20).until(EC.presence_of_element_located((By.ID, "m_login_email"))).send_keys(email.strip())
            except: WebDriverWait(self.bot, 20).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(email.strip())

            try: WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.NAME, "pass"))).send_keys(password)
            except: WebDriverWait(self.bot, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))).send_keys(password)
            WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Log In']"))).click()
            
            try:WebDriverWait(self.bot, 10).until(EC.url_contains("https://mbasic.facebook.com/login/save-device/?login_source="))
            except:pass
            url = self.bot.current_url
            if 'login/save-device/' or 'home.php?' in url:
                cookies = bot.get_cookies()
                format = {}
                for cookie in cookies :
                    format[cookie['name']] = cookie['value']
                cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
                return 'success' , cookie_string , Get_Name(cookie_string).Get()
            elif 'checkpoint' in url:
                print('Verification checkpoint!')
                return "Failed"
            else:
                print('Email or password incorrect!')
                return "Failed"
        except: return "Failed"
        
    def View(self,cook):
        try:
            self.bot.get("https://www.facebook.com/")
            cookies = cook.strip().split(";")
            for cookie in cookies:
                cookie_parts = cookie.split("=")
                if len(cookie_parts) == 2:
                    cookie_name, cookie_value = cookie_parts
                    self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
            self.bot.get("https://www.facebook.com/profile.php?")
            cookie_string = self.update_cookie(cook)
            return cookie_string
        except: return "Failed"
    
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
