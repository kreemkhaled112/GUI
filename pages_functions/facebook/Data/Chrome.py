from Data.init import *

class Chrom:
    def __init__(self):
        self = self
        try:
            options = webdriver.ChromeOptions()
            chrome_prefs = {"profile.default_content_setting_values.notifications": 2}  
            options.add_experimental_option("prefs", chrome_prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("--log-level=3")
            self.bot = webdriver.Chrome(options=options)
        except Exception as e:
            print(f"Failed to start the browser : \n{e}")
    def update_cookie(self,cook):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        cookies = cook.split(";")
        for cookie in cookies:
            cookie_parts = cookie.split("=")
            if len(cookie_parts) == 2:
                cookie_name, cookie_value = cookie_parts
                self.bot.add_cookie({'name': cookie_name, 'value': cookie_value})
        bot.get("https://www.facebook.com/profile.php?")
        cookies = bot.get_cookies()
        format = {}
        for cookie in cookies :
            format[cookie['name']] = cookie['value']
        cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
        
        bot.quit()
        return cookie_string

    def Get(self,email, password):
        bot = self.bot

        self.bot.get("https://mbasic.facebook.com/login/")

        try:
            username = WebDriverWait(self.bot, 20).until(
                EC.presence_of_element_located((By.ID, "m_login_email"))
            )
        except:
            username = WebDriverWait(self.bot, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )

        try:
            password_field = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located((By.NAME, "pass"))
            )
        except:
            password_field = WebDriverWait(self.bot, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[type='password']"))
            )
        log = WebDriverWait(bot, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[value='Log In']")))

        username.send_keys(email.strip())
        password_field.send_keys(password)
        log.click()

        try:
            WebDriverWait(self.bot, 10).until(EC.url_contains(
                "https://mbasic.facebook.com/login/save-device/?login_source="))
        except:
            pass
        url = self.bot.current_url

        if 'login/save-device/' or 'home.php?' in url:
            
            input("......")
            cookies = bot.get_cookies()
            format = {}
            for cookie in cookies :
                format[cookie['name']] = cookie['value']
            cookie_string = ";".join([f"{name}={value}" for name , value in format.items()])
            
            bot.quit()
            return cookie_string
        elif 'checkpoint' in url:
            print('Verification checkpoint!')
            return "continue"
        else:
            print('Email or password incorrect!')
            return "continue"
    def View(self,cook):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        cookies = cook.split(";")
        for cookie in cookies:
            cookie_parts = cookie.split("=")
            if len(cookie_parts) == 2:
                cookie_name, cookie_value = cookie_parts
                bot.add_cookie({'name': cookie_name, 'value': cookie_value})
        bot.get("https://www.facebook.com/profile.php?")

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

# with open("id.txt", 'r') as file:
#         id = [line.strip() for line in file.readlines()]
# Chrom().scrap(id,'m_page_voice=61552931475833;xs=39%3AypkGrvq2IIeNjA%3A2%3A1699300817%3A-1%3A-1;c_user=61552931475833;fr=0dyLywbOIibBP3V1P.AWX-Wm_ODWPeMvo5kJ6NuqvSXdU.BlSUXP.fu.AAA.0.0.BlSUXP.AWUg64nYPek;sb=z0VJZRar4k92ZEEQpkEaQNj1;datr=z0VJZcW10H1toQvmngrrxCC5')