from pages_functions.__init__ import *
class Mohmal:
    def __init__(self, name ,type):
        pass
class Maokt:
    def __init__(self, name ,type):
        self.req = requests.Session()
        self.name = name
        self.type = type
        self.Get_site()
    def Get_site(self):
        try:
            self.headers = {
                'authority': 'moakt.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            }
            self.req.headers.update(self.headers)

            response = self.req.get('https://moakt.com/ar')
            self.Get_Email()
        except Exception as e:
            print(e)
    def Get_Email(self):
        try:
            self.cookies = {
                '__utma': '213295240.1981965866.1697386554.1697386554.1697386554.1',
                '__utmc': '213295240',
                '__utmz': '213295240.1697386554.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                '__utmb': '213295240.1.10.1697386554',
            }
            self.req.cookies.update(self.cookies)
            self.headers['origin'] = 'https://moakt.com'
            self.headers['referer'] = 'https://moakt.com/ar'
            self.req.headers.update(self.headers)


            data = {
                'domain': self.type ,
                'username': self.name ,
                'setemail': 'انشئ الآن',
                'preferred_domain': self.type,
            }

            response = self.req.post('https://moakt.com/ar/inbox', data=data)
            if response.status_code == 200 and "تم إنشاء بريدك المؤقت" in response.text :
                self.Get_Message()
        except:
            pass
    def Get_Random(self):
        try:
            self.cookies = {
                '__utma': '213295240.1981965866.1697386554.1697386554.1697386554.1',
                '__utmc': '213295240',
                '__utmz': '213295240.1697386554.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                '__utmb': '213295240.1.10.1697386554',
            }
            self.req.cookies.update(self.cookies)
            self.headers['origin'] = 'https://moakt.com'
            self.headers['referer'] = 'https://moakt.com/ar'
            self.req.headers.update(self.headers)

            data = {
                'domain': 'moakt.cc',
                'username': '',
                'random': 'انشئ بريد عشوائي',
                'preferred_domain': 'moakt.ws',
            }

            response = self.req.post('https://moakt.com/ar/inbox', data=data)
            if response.status_code == 200 and "تم إنشاء بريدك المؤقت" in response.text :
                soup = BeautifulSoup(response.text, 'html.parser')
                email_element = soup.find('div', {'id': 'email-address'})
                self.Get_Message()
        except:
            pass
    def Get_Message(self):
        try:
            response = self.req.get('https://moakt.com/ar/inbox')
            return response
        except:
            pass
