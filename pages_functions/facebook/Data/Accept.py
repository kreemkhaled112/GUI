from pages_functions.__init__ import *

class Accept:
    def __init__(self, cookie ) -> None:
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.Get_profile()

    def Get_profile(self):
            response = self.req.get( f'https://mbasic.facebook.com/friends/center/requests/' )
            sleep(1)
            if response.status_code == 200:
                try:
                    soup = BeautifulSoup(response.content, 'html.parser')  
                    href = soup.select_one('a[href^="/a/notifications.php?confirm"]')["href"]
                    response = self.req.get( f'https://mbasic.facebook.com/{href}' )  

                    if response.status_code == 200 :
                        print(Colorate.Diagonal(Colors.green_to_cyan, f'[ Done Accept Friend ]', 1))
                except:
                    print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild Accept Account ]', 1))
            else:
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild Find Friend ]', 1))

        