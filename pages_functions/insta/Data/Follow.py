from Data.init import *

class Follow:
    def __init__(self, id ,cookie) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.Get_Profile(id)
    def Get_Profile(self,id):
        self.url = f"https://mbasic.facebook.com/profile.php?id={id}"
        response = self.req.get(self.url)
        sleep(1)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            try :
                self.href = soup.select_one('a[href^="/a/subscribe.php?"]').get('href')
                sleep(1)
                self.Follow_Profile(id)
            except:
                print("Already followed")     
        else:
            print("Faild Get_Profile")

    def Follow_Profile(self,id):
        self.headers['referer'] = self.url
        self.req.headers.update(self.headers)

        response = self.req.get( f'https://mbasic.facebook.com/{self.href}' )
        
        if response.status_code == 200 :
            print(Colorate.Diagonal(Colors.green_to_cyan, f'[ Done Follow ] : [ {id} ]', 1))
            sleep(1)

