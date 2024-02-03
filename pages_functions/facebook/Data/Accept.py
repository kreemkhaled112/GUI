from pages_functions.__init__ import *

class Accept:
    def __init__(self, cookie ) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.Get_profile()

    def Get_profile(self):
        response = self.req.get( f'https://mbasic.facebook.com/friends/center/requests/' )
        sleep(1)
        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')  
                href = soup.select_one('a[href^="/a/notifications.php?confirm"]')["href"]
                response = self.req.get( f'https://mbasic.facebook.com/{href}' )  

                if response.status_code == 200 :
                    Update_cookies(self.cookie,(';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", ""))
                    return f'Done Accept Friend', 1
            except: return f'Faild Accept Account', 0
        else: return f'Faild Find Friend', 0

        