from pages_functions.__init__ import *

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
class Message:
    message_ids = []

    def message_list(self):
        url = "https://api.mail.tm/messages"
        headers = { 'Authorization': 'Bearer ' + self.token }
        response = self.session.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return  [
                    msg for i, msg in enumerate(data['hydra:member']) 
                        if data['hydra:member'][i]['id'] not in self.message_ids
                ]
    def message(self, idx):
        url = "https://api.mail.tm/messages/" + idx
        headers = { 'Authorization': 'Bearer ' + self.token }
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def Get_Message(self):
        for message in self.message_list():
            self.message_ids.append(message['id'])
            message = self.message(message['id'])
            return message
class Mail_Tm(Message):
    token = ""
    domain = ""
    address = ""
    session = requests.Session()

    def __init__(self , username ,password):
        self.username = username
        self.password = password
        if not self.domains():
            print("Failed to get domains")
        self.register()

    def domains(self):
        url = "https://api.mail.tm/domains"
        response = self.session.get(url)
        response.raise_for_status()
        try:
            data = response.json()
            for domain in data['hydra:member']:
                if domain['isActive']:
                    self.domain = domain['domain']
                    return True
            raise Exception("No Domain")
        except: return False

    def register(self):
        url = "https://api.mail.tm/accounts"
        payload = {
            "address": f"{self.username}@{self.domain}",
            "password": self.password
        }
        headers = { 'Content-Type': 'application/json' }
        response = self.session.post(url, headers=headers, json=payload)
        response.raise_for_status()

        data = response.json()
        try: self.address = data['address']
        except: self.address = f"{self.username}@{self.domain}"
        self.get_token(self.password)
        if not self.address:
            raise Exception("Failed to make an address")

    def get_token(self, password):
        url = "https://api.mail.tm/token"
        payload = {
            "address": self.address,
            "password": password
        }
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(url, headers=headers, json=payload)
        response.raise_for_status()
        try: self.token = response.json()['token']
        except: raise Exception("Failed to get token")
