import requests

mail=requests.get('https://email.catdns.in/api/coach-wage@catway.org/email').json()
print(mail)