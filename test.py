# from NamasteiG import Instagram
from pages_functions.Facebook.Data.Action import *
from pages_functions.__init__ import *
import json , sys , hashlib , os , time , marshal, getpass
from pages_functions.Facebook.Data.get_count import *

# chrs = 'abcdefghijklmnopqrstuvwxyz'
# chrs = ''.join((chrs, '0123456789'))
# ser = ''.join(random.choices(chrs, k=random.randrange(7,8)))  
# while True:
#       random_item = cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone()
#       input(f'{random_item[0].strip()} ' )


# with open("account.txt", "r",encoding="UTF-8") as file:
#      lines = file.readlines()

# with open("account.txt", "w",encoding="UTF-8") as file:
#      for line in lines:
#           if line.strip() and "𝔸𝟟𝕄𝔼𝔻 𝕆𝕄𝔸ℝ," not in line:
#               file.write(line.strip() + "\n")
# with open("32.txt", "r") as file:
#      lines = file.readlines()
#      for line in lines:
#           a = line.split("/")
#           input(a[-2])
# with open("pages_functions\\name.txt", "r",encoding="UTF-8") as file:
#     data = file.readlines()
#     for i in data:
#         elements = i.split(':')
#         print(elements[0].strip())
#         # cursor.execute('INSERT INTO name ( data , type) VALUES ( ?, ?)', (i, 'femalea'))
# conn.commit()

# class FaceBook_RegIster():
#     def __init__(self):
#         self.done = False
#         self.cookies = {
#             "lsd": "",
#             "jazoest": "",
#             "ccp": "",
#             "reg_instance": "",
#             "submission_request": "",
#             "reg_impression_id": ""
#         }
#         self.password = '016' + ''.join(random.choices("1234567890", k=6))    
#         self.email = "".join(random.choice("1234567890qpwoeirutyalskdjfhgmznxbcv") , k =7)
#         random_item = (cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone())[0].split()
#         self.Name = random_item[0]
#         self.Name2 = random_item[1]
#         self.admin()

#     def admin(self):
#         print("[+] get cookies ..")
#         self.get_cookies()
#         print('[+] Create The Account ..')
#         self.register()

#     def get_cookies(self):
#         url = "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr"
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, 'html.parser')
#         lsd = soup.select_one('input[name=lsd]')['value']
#         jazoest = soup.select_one('input[name=jazoest]')['value']
#         ccp = soup.select_one('input[name=ccp]')['value']
#         reg_instance = soup.select_one('input[name=reg_instance]')['value']
#         submission_request = soup.select_one('input[name=submission_request]')['value']
#         reg_impression_id = soup.select_one('input[name=reg_impression_id]')['value']
#         self.cookies['lsd'] = lsd
#         self.cookies['jazoest'] = jazoest
#         self.cookies['ccp'] = ccp
#         self.cookies['reg_instance'] = reg_instance
#         self.cookies['submission_request'] = submission_request
#         self.cookies['reg_impression_id'] = reg_impression_id

#     def save_to_text_file(self, username, email, password, status):
#         with open('account_info.txt', 'a') as file:
#             file.write(f'Username: {username}\n')
#             file.write(f'Email: {email}\n')
#             file.write(f'Password: {password}\n')
#             file.write(f'Status: {status}\n')
#             file.write('=' * 40 + '\n')

#     def register(self):
#         url = "https://mbasic.facebook.com/reg/submit/?cid=103"
#         headers = {
#             "Host": "mbasic.facebook.com",
#             "Cookie": f"datr={self.cookies['reg_instance']}",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#             "Accept-Language": "en-US,en;q=0.5",
#             "Referer": "https://mbasic.facebook.com/reg/?cid=103&refsrc=deprecated&_rdr",
#             "Content-Type": "application/x-www-form-urlencoded",
#             "Content-Length": "547",
#             "Origin": "https://mbasic.facebook.com",
#             "Dnt": "1",
#             "Upgrade-Insecure-Requests": "1",
#             "Sec-Fetch-Dest": "document",
#             "Sec-Fetch-Mode": "navigate",
#             "Sec-Fetch-Site": "same-origin",
#             "Sec-Fetch-User": "?1",
#             "Te": "trailers"
#         }
#         data = f"lsd={self.cookies['lsd']}&jazoest={self.cookies['jazoest']}&ccp={self.cookies['ccp']}&reg_instance={self.cookies['reg_instance']}&submission_request={self.cookies['submission_request']}&helper=&reg_impression_id={self.cookies['reg_impression_id']}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names%5B%5D=firstname&field_names%5B%5D=reg_email__&field_names%5B%5D=sex&field_names%5B%5D=birthday_wrapper&field_names%5B%5D=reg_passwd__&firstname={self.Name}&lastname={self.Name2}&reg_email__={self.email}%40hi2.in&sex={random.randint(1,2)}&custom_gender=&did_use_age=false&birthday_month={random.randint(1,12)}&birthday_day={random.randint(1,28)}&birthday_year={random.randint(1996,2005)}&age_step_input=&reg_passwd__={self.password}&submit=Sign+Up"
#         r = requests.post(url, headers=headers, data=data)
#         open("html.html" , "w" , encoding="utf-8").write(r.text)
#         webbrowser.open('html.html')
#         # if 'take you through a few steps to confirm your account on Facebook' in r.text:
#         #     print('[+] Done Create Account !')
#         #     print('[+] Username : Not Found ( Login Use Email )')
#         #     print("[+] Email :" + self.email + "@yopmail.com")
#         #     print("[+] Password : " + self.password)
#         #     print("[+] Status : Confirm")
#         #     print('=' * 40)
#         #     self.save_to_text_file('Not Found', f'{self.email}@yopmail.com', self.password, 'Confirm')
#         # elif 'There was an error with your registration. Please try registering again.' in r.text:
#         #     print('[X] Blocked From Facebook')
#         #     print('=' * 40)
#         #     self.save_to_text_file('Blocked', '', '', '')
#         # else:
#         #     try:
#         #         user_id = r.cookies['c_user']
#         #         print('[+] Done Create Account !')
#         #         print('[+] Username : '+user_id)
#         #         print("[+] Email :" + self.email + "@yopmail.com")
#         #         print("[+] Password : " + self.password)
#         #         print("[+] Status : Done Create Account")
#         #         print('=' * 40)
#         #         self.save_to_text_file(user_id, f'{self.email}@yopmail.com', self.password, 'Done Create Account')
#         #     except:
#         #         print("[X] Use Vpn")
#         #         print('=' * 40)
#         #         self.save_to_text_file('', '', '', 'Use VPN')
# with open("New.txt", "r") as file1:
#     text = file1.readlines()

# with open("t.txt", "r") as file2:
#     lines = file2.readlines()
#     non_matching_lines = [line for line in lines if not any(entry.split(':')[0] in line for entry in text)]

# with open("Newt.txt", "a") as output_file:
#     output_file.writelines(non_matching_lines)

# from pages_functions.Facebook.Data.Edit import *
# while True:
#      cookie_string = input("cookie:")
#      input(f"{cookie_string};i_user={Get_i_user(cookie_string).Get()};")
#      os.system('cls')

# chrs = 'abcdefghijklmnopqrstuvwxyz'
# user = ''.join(random.choices(chrs, k=random.randrange(8,10)))      
# list = ["teml.net","tmail.ws","moakt.cc"]
# rand = random.choice(list)
# input(f'{user}@{rand}')
# m = Maokt(user,rand)
# while True:
#      soup = BeautifulSoup(m.Get_Message().content, 'html.parser')
#      message_elements = soup.find_all('div', class_='email-messages modal')
#      try:
#           for element in message_elements:
#                input(element)
#                links = element.find_all('a', href=True)
#                for link in links:
#                     print(link['href'])
#                message = element.get_text().strip()
#                code_pattern = r'FB-(\d+)'
#                matches = re.findall(code_pattern, message)
#      except: pass
# تحديد من جدول واستخراج
# with open("account.txt", "w",encoding="UTF-8") as file:
#     data = cursor.execute("SELECT * FROM account  WHERE cookies = '' ").fetchall()
#     for i in data:
#         try:file.write(f"{i[2]}:{i[3].strip()}:\n")
#         except:pass

# تحديد من جدول واضافات الي جدول اخر وحذفه
data = cursor.execute("SELECT * FROM account  WHERE groupname = 'wait' ").fetchall()
for i in data:
    cursor.execute('INSERT INTO Sell ( name , email, password,username, cookies) VALUES (?, ?, ?, ?, ?)', (i[1], i[2], i[3],i[4], i[5]))
    cursor.execute(f'DELETE FROM Account WHERE email = "{i[2]}" ')

# حذف السجلات المكررة
# duplicate_rows_query = "SELECT email, COUNT(*) FROM account GROUP BY email HAVING COUNT(*) > 1"
# duplicate_rows = cursor.execute(duplicate_rows_query).fetchall()
# for row in duplicate_rows:
#     primary_key_value = row[0]
#     input(primary_key_value)
#     delete_query = f" DELETE FROM account WHERE email = '{primary_key_value}' "
#     cursor.execute(delete_query)
# تحديث بينات ف جدول
# with open("liked_Before.txt", "r") as file:
#      lines = file.readlines()
#      for line in lines:
#         a = line.split(':')
#         cursor.execute('UPDATE account SET groupname = ? WHERE email = ?', ('edit', a[0]))
# cooki = 'm_page_voice=100093428851762;sb=MmJjZtWPTRM6u3iHwnxnV5uY;datr=MmJjZrw8t1tugQ32eU0s30dH;c_user=100093428851762;ps_n=1;ps_l=1;wd=958x902;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1718211450895%2C%22v%22%3A1%7D;xs=14%3A31mau5lpYWPtOg%3A2%3A1686153706%3A-1%3A-1%3A%3AAcUug0kHLAmr4TY0708eoz9HHpqCr4HUg0U6xqlQeA;fr=10d9DuKvczVwjVtyh.AWUmeIxfiPsW5T6My8dVF9yBhI8.BmadN7..AAA.0.0.BmadN7.AWXTZhAQRAo;'
# a = get_comment('https://www.facebook.com/Add4Like/posts/pfbid02Yxn6pReG14byu15dBAahLWfii5r4BGeBMtNh28kQ5kKdU6bskobCFmxeyMFb167ml').Start()
# print(a)
conn.commit()
