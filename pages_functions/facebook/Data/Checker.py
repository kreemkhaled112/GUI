from pages_functions.__init__ import *
from pages_functions.Facebook.Data.Edit import *

class Checker:
    def __init__(self, cookie) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.id = re.search(r'c_user=(\d+)', cookie).group(1)
        cookie = {'cookie':cookie}
        self.req.cookies.update(cookie)
    def start(self):
        response = self.req.get(f'https://mbasic.facebook.com/profile.php?id={self.id}')
        cookie_string = (';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", "")
        if 'Chat' in response.text or "دردشة" in response.text :
            return 'success' , cookie_string , Get_Name(cookie_string).Get()
        elif  "We suspended your account" in response.text :
            return "checkpoint" , cookie_string
        elif 'The email address or mobile number you entered isn&#039;t connected to an account' in response.text:
            return 'The email address or mobile number you entered is not connected to an account' , cookie_string
        elif 'The password that you&#039;ve entered is incorrect.' in response.text:
            return "The password that you've entered is incorrect" , cookie_string
        elif "You've entered an old password" in response.text :
            return "You've entered an old password" , cookie_string
        elif 'Choose a way to confirm that it&#039;s you' in response.text:
            return 'Two Factor Code Sended.....' , cookie_string
        else:
            print(cookie_string)
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            webbrowser.open('html.html')
