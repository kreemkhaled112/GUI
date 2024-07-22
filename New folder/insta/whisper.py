import requests,random,threading,json,sys,os
from string import ascii_letters, ascii_lowercase, digits
from datetime import datetime
from uuid import uuid4
import time as sleper
from user_agent import generate_user_agent as ua
requests.packages.urllib3.disable_warnings()

class Whisper:
	def __init__(self):
		self.start_time = sleper.time()
		self.time = int(datetime.now().timestamp())
		Numbers = '123456789'
		self.chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
		username  = ''.join(random.choices(self.chars, k=random.randrange(6,7)))
		self.email = f'fb2e+{username}@yandex.com'
		self.length = random.randint(6,8)
		self.Created = 0
		self.Status = None
		self.password = ''.join(random.choices(self.chars, k=random.randrange(7,9))) 
		self.APPID = str("".join(random.choice(Numbers)for i in range(15)))
		self.year = random.randint(2000,2005)
		self.month = random.randint(1,12)
		self.day = random.randint(1,20)
		print(f'{self.email}:{self.password}')
	def SendToBot(self,message):
		try:
			with open('bot.json', 'r') as f:
				data = json.load(f)
				self.id = data['id']
				self.token = data['token']
				requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text={message}')
		except :
			pass
	
	def SetCookies(self):
		url = 'https://i.instagram.com/api/v1/public/landing_info/'
		headers  = {
		'User-Agent': ua()
		}
		Response = requests.get(url,headers=headers).cookies
		# print(Response)
		try:
			self.mid = Response['mid']
			self.csrftoken = Response['csrftoken']
			self.ig_did = Response['ig_did']
		except:
			pass
	def CheckUsername(self):
			url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
			headers = {
				'User-Agent':ua(),
				'X-IG-App-ID':f'{self.APPID}',
				'Content-Type':'application/x-www-form-urlencoded',
				'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
				'X-CSRFToken':f'{self.csrftoken}'
			}
			while True:
				self.username = str("".join(random.choice(self.chars)for i in range(self.length)))
				data = f'email=&username={self.username}&first_name=&opt_into_one_tap=false'
				response = requests.post(url,headers=headers,data=data)
				if 'username_is_taken' not in response.text and response.status_code == 200 :
					print(f'[1] Checking username : {self.username}')
					return True
					break
				else:
					print(f"Searching for available username")
	def CreateEmail(self):
			res = requests.get("https://email.catdns.in", headers={'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",'cache-control': "max-age=0",'sec-ch-ua': "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",'sec-ch-ua-mobile': "?1",'sec-ch-ua-platform': "\"Android\"",'upgrade-insecure-requests': "1",'sec-fetch-site': "same-origin",'sec-fetch-mode': "navigate",'sec-fetch-user': "?1",'sec-fetch-dest': "document",'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6",'priority': "u=0, i"}).text
			id=res.split('"$ACTION_ID_')[1].split('"')[0]
			self.email=res.split('name="mail" value="')[1].split('"')[0]
			r = requests.post("https://email.catdns.in", files=[(f'1_$ACTION_ID_{id}', (None, '')),('1_mail', (None, self.email)),('0', (None, '["$K1"]'))],headers={'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",'Accept': "text/x-component",'sec-ch-ua': "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",'next-router-state-tree': "%5B%22%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2F%22%2C%22refresh%22%5D%2C%22modal%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",'sec-ch-ua-mobile': "?1",'next-action':id,'sec-ch-ua-platform': "\"Android\"",'origin': "https://email.catdns.in",'sec-fetch-site': "same-origin",'sec-fetch-mode': "cors",'sec-fetch-dest': "empty",'referer': "https://email.catdns.in/",'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6",'priority': "u=1, i"}).status_code
#				if r == 303:
			print(f'[2] Creating Email : {self.email}')
			return True
#				else:
#					return False
	def CheckBirthday(self):
			url = 'https://www.instagram.com/web/consent/check_age_eligibility/'
			data = f'day={self.day}&month={self.month}&year={self.year}'
			headers = {
			'User-Agent':ua(),
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}	
			check = requests.post(url,headers=headers,data=data)
			if '"status":"ok"' in check.text:
				return True
			else:
				return False
	def Retry_Send_Code(self,email):
			url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
			data = f'device_id=&email={email}'
			headers = {
			'User-Agent':ua(),
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			send = requests.post(url,headers=headers,data=data)
	def Account_Status(self,username):
		url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
		headers = {
			'User-Agent':ua(),
			'X-IG-App-ID':'1217981644879628',	
			'X-ASBD-ID':'198387'
		}
		response = requests.get(url,headers=headers)
		if 'id' in response.text:
			return 'Active'
		else:
			return 'Suspend'
	def SaveInfo(self,Account,Session):
		with open('Whisper-accounts.txt','a') as f:
			f.write(f'{Account}\n')
		with open('Whisper-sessions.txt','a') as s:
			s.write(f'session:{Session}\n')
	def SendCode(self):
			url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
			data = f'device_id=&email={self.email}'
			headers = {
			'User-Agent':ua(),
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			send = requests.post(url,headers=headers,data=data)
			if '"email_sent":true' in send.text:		
				print('[3] Sending Verification code')
				#sleper.sleep(4)
				return True
			else:
				return False
	def GetCode(self):
			while True:
				for i in range(5):
					response = requests.get(f'https://email.catdns.in/api/{self.email}/email')
					if 'Instagram' in response.text:
						for messages in response.json()['data']['mails']:
							subject = messages['subject']
							self.code = subject.split(' is your Instagram code')[0]
							return True
							break
					else:				
						print(f'\r[4] Waiting Verification code',end='')
					#	sleper.sleep(5)
				print('\rResend',end='')
				Whisper.Retry_Send_Code(self.email)
				
	def CheckCode(self):
			print('\n[5] Verifying The Code')
			url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/'
			code = input('code: ')
			data = f'code={code}&device_id=&email={self.email}'
			headers = {
			'User-Agent':ua(),
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			response = requests.post(url,headers=headers,data=data)
			if 'signup_code' in response.text:
				self.signup_code = response.json()['signup_code']
				return True
			else:
				print(response.text)
				return False
		
	def CreateAccount(self):
			print('[6] Creating Account')
			url = 'https://www.instagram.com/accounts/web_create_ajax/'
			time = int(datetime.now().timestamp())
			data = f'enc_password=#PWD_INSTAGRAM_BROWSER:0:{time}:{self.password}&email={self.email}&username={self.username}&first_name=Created By Whisper\n&month={self.month}&day={self.day}&year={self.year}&client_id=&seamless_login_enabled=1&tos_version=row&force_sign_up_code={self.signup_code}'
			headers = {
			'User-Agent':ua(),
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			response = requests.post(url,headers=headers,data=data)
			if 'user_id' in response.text:
				self.end_time = sleper.time()
				self.elapsed_time = int(self.end_time - self.start_time)
				Session = response.cookies['sessionid']
				Account = f'{self.username}:{self.password}'
				message = f'[√] UserName : {self.username}\n[√] PassWord : {self.password}\n[√] E-mail : {self.email}\n[+] Account Status : {Whisper.Account_Status(self.username)}'
				print('='*30)
				print(message)
				print('='*30)
				Whisper.SaveInfo(Account,Session)
				Whisper.SendToBot(message)
				
			else:
				print('-'*40)
				print(response.text)
				print('-'*40)

os.system('clear')
Whisper = Whisper()
try:
	count = int(input('[+] How Many Accounts : '))
except :
	count = 0
for i in range(count):
	Whisper.SetCookies()
	input('....')
	Whisper.CheckUsername()
	input('....')
	Whisper.CheckBirthday()
	input('....')
	Whisper.SendCode()
	input('....')
	Whisper.CheckCode()
	input('....')
	Whisper.CreateAccount()