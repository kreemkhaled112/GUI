
import hashlib, threading , sqlite3 , random , string , requests , json , gzip , re , time , webbrowser , os
from faker import Faker
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, ConnectTimeout
from pystyle import *

success = 0
fails = 0
conn = sqlite3.connect('info.db',check_same_thread=False)
cursor = conn.cursor()
class Login:
    def __init__(self,email,password):
        self.req = requests.Session()
        self.email = email
        self.password = password
        headers = {
            'Host': 'www.facebook.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Connection': 'close',
        }
        self.req.headers.update(headers)

    def Start(self):
        try:
            response = self.req.get('https://www.facebook.com/')
            time.sleep(5)
            fr=response.cookies['fr']
            sb=response.cookies['sb']
            _datr=response.text.split('"_js_datr","')[1].split('"')[0]
            _token=response.text.split('privacy_mutation_token=')[1].split('"')[0]
            _jago=response.text.split('"jazoest" value="')[1].split('"')[0]
            _lsd=response.text.split('name="lsd" value="')[1].split('"')[0]

            cookie = {'fr': fr,'sb': sb,'_js_datr': _datr,'wd': '717x730','dpr': '1.25'}
            self.req.cookies.update(cookie)

            data = urlencode({
                'jazoest': _jago,
                'lsd': _lsd,
                'email': self.email,
                'login_source': 'comet_headerless_login',
                'next': '',
                'encpass': f'#PWD_BROWSER:0:{round(time.time())}:{self.password}',
            })

            headers = {
                'Host': 'www.facebook.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'https://www.facebook.com/',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Content-Length': str(len(data)),
                'Origin': 'https://www.facebook.com',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
            self.req.headers.update(headers)

            response = self.req.post(f'https://www.facebook.com/login/?privacy_mutation_token={_token}', data=data)
            if 'Enter the code from your email' in response.text :
                code = input(Colorate.Horizontal(Colors.white_to_blue,'code: '))
                req = BeautifulSoup(response.content, 'html.parser')
            
                id = re.search('"USER_ID":"(.*?)",',str(req)).group(1)
                haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
                rev = re.search('{"rev":(.*?)}',str(req)).group(1)
                hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
                dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
                jazoest = req.find('input', {'name': 'jazoest'}).get("value")
                lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
                spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
                spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
                params = {'next': 'https://www.facebook.com/?sk=welcome','cp': self.email,'from_cliff': '1','conf_surface': 'hard_cliff','event_location': 'cliff'}
                data = {'jazoest': jazoest,'fb_dtsg': dtsg,'code': code,'source_verified': 'www_reg','confirm': '1','__user': id,'__a': '1','__req': '2','__hs': haste,'dpr': '1','__ccg': 'EXCELLENT','__rev': rev,'__s': 'v3a4u6:hvmttj:6hpnww','__hsi': hsi,'lsd': lsd,'__spin_r': spinr,'__spin_b': 'trunk','__spin_t': spint}
                response = self.req.post('https://www.facebook.com/confirm_code/dialog/submit/',params=params,data=data)

                response = self.req.get('https://www.facebook.com')
                cookie_string = (';'.join([f"{key}={value}" for key, value in self.req.cookies.get_dict().items() ])).replace("cookie=", "").strip()
                print(Colorate.Horizontal(Colors.green_to_yellow, '[5] Verifying The Code'))

                with open("account.txt", "a",encoding="UTF-8") as file:
                    file.write(f'{self.email}:{self.password}:{cookie_string}' + "\n")
                return 'succes'
            else:
                open("html.html" , "w" , encoding="utf-8").write(response.text)
                webbrowser.open('html.html')
                print(Colorate.Horizontal(Colors.red_to_white, f'[+] Faield {email}:{password}')) 
        except (ReadTimeout, ConnectTimeout):
            print(Colorate.Horizontal(Colors.red_to_white, f'[+] Faield {email}:{password}')) 
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_white, e))

def Header_www():
    headers  = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
    return headers
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def create_mail_tm_account():
    chrs = 'abcdefghijklmnopqrstuvwxyz'
    fake = Faker()
    username  = ''.join(random.choices(chrs, k=random.randrange(6,7)))
    chrs = ''.join((chrs, '0123456789'))
    password = ''.join(random.choices(chrs, k=random.randrange(7,9))) 
    birthday = fake.date_of_birth(minimum_age=10, maximum_age=24)
    random_item = cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone()
    name = random_item[0].split(' ')
    first_name = name[0]
    last_name = name[1]
    return f"Fb1e+{username}@yandex.com", password, first_name, last_name, birthday
def register_facebook_account(email, password, first_name, last_name, birthday):
    global  success, fails
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = 'F'
    req = {'api_key': api_key,'attempt_login': False,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': False}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    print(Colorate.Horizontal(Colors.green_to_white, f'[+] Creating {email}:{password}'))
    reg = _call(api_url, req)
    try:
        id=reg['new_user_id']
        a = Login(email,password).Start()
        if a == 'succes':
            success += 1
        else: fails += 1
        os.system(f'title Facebook Create by @kareem ^| success: {success} fails: {fails}')
    except:
        print(Colorate.Horizontal(Colors.red_to_white, f'[+] Faield {email}:{password}')) ; fails += 1
        os.system(f'title Facebook Create by @kareem ^| success: {success} fails: {fails}')

def _call(url, params, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/417.0.0.33.65;FBBV/480086274;FBDM/{density=1.5,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/CoolTEL Aps;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/9;FBOP/1;FBCA/x86:armeabi-v7a;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

os.system("cls" if os.name == "nt" else "clear") ; os.system(f'title Facebook Create by @kareem ^| success: {success} fails: {fails}')
for i in range(int(input(Colorate.Horizontal(Colors.white_to_blue,'[+] How Many Accounts : ')))):
    email, password, first_name, last_name, birthday = create_mail_tm_account()
    if email and password and first_name and last_name and birthday:
        register_facebook_account(email, password, first_name, last_name, birthday)
