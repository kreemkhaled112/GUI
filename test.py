from pages_functions.Facebook.Data.Follow import *
chrs = 'abcdefghijklmnopqrstuvwxyz'
chrs = ''.join((chrs, '0123456789'))
user = ''.join(random.choices(chrs, k=random.randrange(7,8)))  
while True:
     random_item = cursor.execute("SELECT data FROM name WHERE type='female' ORDER BY RANDOM() LIMIT 1").fetchone()
     input(f'{random_item[0].strip()} ' )
