from pages_functions.__init__ import *

class AddFriend:
    def __init__(self, url, cookie ) :
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)

        self.id = (re.search(r'/([^/]+)$', url) or re.search(r'facebook.com/([^/]+)', url) or re.search(r'id=(\d+)', url) or "").group(1)

        try:self.url = url.replace("www", "mbasic")
        except:pass

    def Start(self):
        response = self.req.get(self.url )
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')  
            href = soup.select_one('a[href^="/a/friends/profile/add/"]')["href"]
            sleep(1)
            response = self.req.get( f'https://mbasic.facebook.com/{href}' )  
            if response.status_code == 200 :  
                Update_cookies(self.cookie,(';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", ""))
                return f'Done Friend   :  {self.id} ' , 1
        else: return f'Faild Friend  :  {self.id} ' , 0
        