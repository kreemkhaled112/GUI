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
		self.year = random.randint(1990,1999)
		self.month = random.randint(1,12)
		self.day = random.randint(1,20)
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
#		print(Response)
		try:
			self.mid = Response['mid']
			self.csrftoken = Response['csrftoken']
			self.ig_did = Response['ig_did']
			return True
		except:
			return False
	def CheckUsername(self):
		if Whisper.SetCookies():
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
					print('[1] Checking username')
					return True
					break
				else:
					print(f"Searching for available username")
	def CreateEmail(self):
		if Whisper.CheckUsername():
			self.email=self.email
#				if r == 303:
			print(f'[2] Creating Email : {self.email}')
			return True
#				else:
#					return False
		else:
			print('Missing Cookies ')
	def CheckBirthday(self):
		if Whisper.CreateEmail():
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
		else:
			print('Email Not Created')
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
		if Whisper.CheckBirthday():
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
		else:
			print('Error In Check Birthday')
	def GetCode(self):
		if Whisper.SendCode():
			while True:
					self.code = input('code: ')
					if self.code:
						return True
						break
					else:	
						print('\rResend',end='')
						Whisper.Retry_Send_Code(self.email)
						print(f'\r[4] Waiting Verification code',end='')
					#	sleper.sleep(5)
				
				
		else:
			print('Email Not sent')
	def CheckCode(self):
		if Whisper.GetCode():
			print('\n[5] Verifying The Code')
			url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/'
			data = f'code={self.code}&device_id=&email={self.email}'
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
		if Whisper.CheckCode():
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
		else:
			print('Faild To Create Account')
os.system('clear')
Whisper = Whisper()
try:
	count = int(input('[+] How Many Accounts : '))
except :
	count = 0
for i in range(count):
 t = threading.Thread(target=Whisper.CreateAccount()).start()