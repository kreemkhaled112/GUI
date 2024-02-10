from pages_functions.__init__ import *

class Follow:
    def __init__(self, url ,cookie):
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
        response = self.req.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            try : 
                try: 
                    self.href = soup.select_one('a[href^="/a/subscribe.php?"]').get('href')
                    sleep(1)
                    return self.Follow_Profile()
                except : 
                    self.href = soup.select_one('a[href^="/a/subscriptions/remove?"]').get('href')
                    Update_cookies(self.cookie,(';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", ""))
                    return "Already followed" , 2
            except: 
                open("html.html" , "w" , encoding="utf-8").write(response.text)
                return "Faild Follow" , 0
        else: return "Faild Follow" , 0

    def Follow_Profile(self):
        self.headers['referer'] = self.url
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        if response.status_code == 200 :
            Update_cookies(self.cookie,(';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", ""))
            return (f'Done Follow : {self.id}') , 1


