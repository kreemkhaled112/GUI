from pages_functions.__init__ import *

class Comment_Like:
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
        response = self.req.get(self.url)
        sleep(1)
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.href  = soup.select_one('a[href^="/comment/replies/"]')['href']
                response = requests.get(f'https://mbasic.facebook.com{url}', cookies=cookies,headers=self.headers, timeout=30)
                soup = BeautifulSoup(response.text, "html5lib")
                if response.status_code == 200:
                    fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
                    jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
                    url2 = soup.select_one('form[action^="/a/comment.php?"]')['action']
                return self.Get_data()
            else: return "Faild Get_post" , 0
        except:
            open("html.html" , "w" , encoding="utf-8").write(response.text)
            return "failed Comment" , 0
        
    def Get_data(self):
        self.headers['origin'] = 'https://mbasic.facebook.com'
        self.headers['referer'] = self.href
        data = {
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'comment_text': comments[comments_index],
            }
        if response.status_code == 200: 
            response = requests.post(f'https://mbasic.facebook.com{url2}', cookies=cookies, data=data,headers=self.headers, timeout=30)
        if response.status_code == 200:
            return "Done Comment" , 1
