from Data.init import *

class AddFriend:
    def __init__(self, id, cookie ) -> None:
        self.conn = sqlite3.connect('info.db')
        self.cursor = self.conn.cursor()
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie': cookie }
        self.req.cookies.update(cookie)
        self.Get_profile(id)

    def Get_profile(self,id):
        response = self.req.get( f'https://mbasic.facebook.com/profile.php?id={id}' )
        try:
            self.cursor.execute(f'SELECT * FROM account where username = {id}')
            cookie = self.cursor.fetchone()
            sleep(1)
            if  "Content unavailable" in response.text :
                self.cursor.execute('INSERT INTO Bad ( email, password,link ,Cookies) VALUES (?, ?, ?, ?)', ( cookie[1], cookie[2], cookie[3] ,cookie[4]))
                try:self.cursor.execute(f"DELETE FROM account WHERE username = {id} ")
                except:pass
                print(Colorate.Diagonal(Colors.red_to_blue, f'[ Faild Account ] : [ {id} ]', 1))                     
            else:
                try:
                    soup = BeautifulSoup(response.content, 'html.parser')  
                    href = soup.select_one('a[href^="/a/friends/profile/add/"]')["href"]
                    response = self.req.get( f'https://mbasic.facebook.com/{href}' )  
                    if response.status_code == 200 :
                        print(Colorate.Diagonal(Colors.green_to_cyan, f'[ Done Friend ] : [ {id} ]', 1))
                except:
                    print(Colorate.Diagonal(Colors.yellow_to_red, f'[ Faild Account ] : [ {id} ]', 1))
        except:pass
        self.conn.commit()
        self.conn.close()