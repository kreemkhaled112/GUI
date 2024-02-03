from __init__ import *

with open("name.txt", "w",encoding="UTF-8") as file:
    data = cursor.execute("SELECT * FROM name  WHERE type = 'male' ").fetchall()
    for i in data:
        try:
            file.write(f"{i[0]}")
        except:pass
    

