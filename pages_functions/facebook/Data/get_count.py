from pages_functions.__init__ import *

class get_follower:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header_www()
        self.req.headers.update(self.headers)
        self.url = url.strip()
        with open('pages_functions\cookie.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            random_line = random.choice(lines)  
        self.cookie = random_line.strip()
        cookie = cookie_format(self.cookie)
        self.req.cookies.update(cookie)

    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"text":"([\d.,]+)\s+Follower"', response.text)
            if not match:
                match = re.search(r'"text":"([\d.,]+)\s+Personen\s+sind\s+Follower"', response.text)
            if match:
                number_of_followers = int(match.group(1).replace(",", "").replace(".", ""))
                return "" , number_of_followers
            else:
                return 'No match found' , self.url
    
class get_likes:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header_www()
        self.req.headers.update(self.headers)
        try:self.url = url.replace("www", "mbasic")
        except:pass
        with open('pages_functions\cookie.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            random_line = random.choice(lines)  
        self.cookie = random_line.strip()
        cookie = cookie_format(self.cookie)
        self.req.cookies.update(cookie)

    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:

            match = re.search(r'aria-label="([\d,.]+) ', response.text)
            if match: return '' , int(match.group(1).replace(",", "").replace(".", ""))
            else:
                soup = BeautifulSoup(response.text, 'html.parser')
                match = re.search(r'(\d+) weitere Personen', str(soup))
                if match:
                    likes = int(match.group(1)) +1
                    return '' , likes
                else:
                    return '' , 1
                
            return 'No match found' , self.url
class get_share:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header_www()
        self.req.headers.update(self.headers)
        self.url = url
        with open('pages_functions\cookie.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            random_line = random.choice(lines)  
        self.cookie = random_line.strip()
        cookie = cookie_format(self.cookie)
        self.req.cookies.update(cookie)
    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"i18n_share_count":"(\d+)"', response.text)
            if match: return '' , int(match.group(1).replace(",", "").replace(".", ""))
            else:
                return 'No match found', self.url
class get_comment:
    def __init__(self, url ):
        self.req = requests.Session()
        self.headers = Header_www()
        self.req.headers.update(self.headers)
        self.url = url
        with open('pages_functions\cookie.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  
            random_line = random.choice(lines)  
        self.cookie = random_line.strip()
        cookie = cookie_format(self.cookie)
        self.req.cookies.update(cookie)
    def Start(self):
        response = self.req.get(self.url)
        if response.status_code == 200:
            match = re.search(r'"comment_rendering_instance":{[^}]*"total_count":(\d+)[^}]*}', response.text)
            print(match.group(1).replace(",", "").replace(".", ""))
            if match: return '',int(match.group(1).replace(",", "").replace(".", ""))
            else:
                return 'No match found' , self.url

