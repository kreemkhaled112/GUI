from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep ,time

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
with open("account.txt", "r",encoding="UTF-8") as file:
     lines = file.readlines()
     for line in lines:
        result = Chrom('headless').Login(line[0],line[1])
        if result == 'success':
            print(f'{line[0]}{line[1]}{result[1]}')
         