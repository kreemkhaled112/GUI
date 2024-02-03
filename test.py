from pages_functions.Facebook.Data.Email import *
chrs = 'abcdefghijklmnopqrstuvwxyz'
chrs = ''.join((chrs, '0123456789'))
user = ''.join(random.choices(chrs, k=random.randrange(8,12)))   
email = Mail_Tm(user,"1234567890")
print(email.address)
while True:
    input("Enter....")
    m = email.Get_Message()
    try:print(m['subject'])
    except:pass