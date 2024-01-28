from pages_functions.__init__ import *

class Follow:
    def __init__(self, url ,cookie):
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)

        try: self.id = re.search(r'/([^/]+)/$', url).group(1) 
        except: self = re.search(r'id=(\d+)', url).group(1) 

        try:self.url = url.replace("www", "mbasic")
        except:pass
    def Start(self):
        response = self.req.get(self.url)
        sleep(1)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            try :
                self.href = soup.select_one('a[href^="/a/subscribe.php?"]').get('href')
                sleep(1)
                return self.Follow_Profile()
            except: 
                return "Already followed"    
        else: return "Faild"

    def Follow_Profile(self):
        self.headers['referer'] = self.url
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        if response.status_code == 200 : 
            return (f'[ Done Follow ] : [ {self.id} ]')


