from init import *

class Checker:
    def __init__(self, cookie) -> None:
        self.conn = sqlite3.connect('info.db')
        self.cursor = self.conn.cursor()
        self.req = requests.Session()
        self.headers = Header()
        self.req.headers.update(self.headers)
        cookie = {'cookie':cookie}
        self.req.cookies.update(cookie)
    def Main(self,id):
        response = self.req.get(f'https://mbasic.facebook.com/profile.php?id={id}')
        if  "Content unavailable" in response.text :
            self.cursor.execute(f'SELECT * FROM account where link = {id}')
            cookie = self.cursor.fetchone()
            self.cursor.execute('INSERT INTO Bad ( email, password,link ,Cookies) VALUES (?, ?, ?, ?)', ( cookie[0], cookie[1], cookie[2] ,cookie[3]))
            self.cursor.execute(f"DELETE FROM account WHERE link = {id} ")
            print(Colorate.Diagonal(Colors.red_to_blue,   f'[ Unavailable ] : [{id}]', 1))
            return "unavailable"
        else:
            match = re.search(r'<title>(.*?)</title>', response.text).group(1)
            print(Colorate.Diagonal(Colors.green_to_cyan, f"[  available  ] : [{id}] : [{match}]", 1))
            return "available"
