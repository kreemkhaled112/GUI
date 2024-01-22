from Data.init import *

class share:
    def __init__(self, url ,message ,cookie) -> None:
        self.req = requests.Session()
        self.message = message
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.url = url
        try:self.url = self.url.replace("www", "mbasic")
        except:pass
    def Get_post(self):
            response = self.req.get(self.url)
            sleep(1)
            try:
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    self.href = soup.select_one('a[href^="/composer/mbasic/?"]').get('href')
                    self.Get_data(self.href)
                    return "successfully"
                else:
                    print("Faild Get_post")
            except:
                open("html.html" , "w" , encoding="utf-8").write(response.text)
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild Share ]', 1))
                return "failed"
    def Get_data(self,href):
        self.headers['sec-fetch-site'] = "same-origin"
        response = self.req.get( f'https://mbasic.facebook.com/{href}' )
        sleep(1)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            self.target = soup.find('input', {'name': 'target'}).get("value")
            self.csid = soup.find('input', {'name': 'csid'}).get("value")
            self.sid = soup.find('input', {'name': 'sid'}).get("value")
            self.shared_from_post_id = soup.find('input', {'name': 'shared_from_post_id'}).get("value")
            self.fb_dtsg = soup.find('input', {'name': 'fb_dtsg'}).get("value")
            self.jazoest = soup.find('input', {'name': 'jazoest'}).get("value")
            link = soup.select_one('form[action^="/composer/mbasic/?"]')["action"]
            self.Share_post(link)
            
    def Share_post(self,link):
        self.headers['origin'] = 'https://mbasic.facebook.com'
        self.headers['referer'] = self.href
        data = {
                "fb_dtsg" :{self.fb_dtsg},
                "jazoest" :{self.jazoest},
                "target" :{self.target},
                "csid" :{self.csid},
                "c_src": "share",
                "referrer" : "permalink",
                "ctype" : "advanced",
                "cver" : "amber_share",
                "waterfall_source" : "advanced_composer_timeline",
                "privacyx" : "300645083384735",
                "appid" : "0",
                "sid" : {self.sid},
                "m" : "self",
                "xc_message": {self.message},
                "view_post" : "Share",
                "shared_from_post_id":{self.shared_from_post_id},
                }
        response = self.req.post( f'https://mbasic.facebook.com/{link}', data=data)
        if response.status_code == 200 :
            print(Colorate.Diagonal(Colors.green_to_cyan, f'[ Done Share ]', 1))
        else:
            print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild Share ]', 1))
