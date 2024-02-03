from pages_functions.__init__ import *

class Comment:
    def __init__(self, url ,message ,cookie) -> None:
        self.req = requests.Session()
        self.message = message
        self.headers = Header()
        self.req.headers.update(self.headers)
        self.cookie = cookie
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.url = url
        try:self.url = self.url.replace("www", "mbasic")
        except:pass
    def Start(self):
        if not self.message :
            return
        response = self.req.get(self.url)
        sleep(1)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.href = soup.select_one('form[action^="/a/comment.php?"]')['action']
                self.fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
                self.jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
                return self.Get_data()
            else: return "Faild Get_post" , 0
        except:
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return "failed Comment" , 0
        
    def Get_data(self):
        self.headers['origin'] = 'https://mbasic.facebook.com'
        self.headers['referer'] = self.url
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'comment_text': self.message,
        }
        response = requests.post(f'https://mbasic.facebook.com{self.href}',  data=data)
        if response.status_code == 200:
            return "Done Comment" , 1

