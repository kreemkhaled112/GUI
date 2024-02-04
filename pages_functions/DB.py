from __init__ import *

# تحديد من جدول واستخراج
# with open("name.txt", "w",encoding="UTF-8") as file:
#     data = cursor.execute("SELECT * FROM name  WHERE type = 'male' ").fetchall()
#     for i in data:
#         try:
#             file.write(f"{i[0]}")
#         except:pass

# تحديد من جدول واضافات الي جدول اخر وحذفه
# data = cursor.execute("SELECT * FROM account  WHERE groupname = 'wait' ").fetchall()
# for i in data:
#     cursor.execute('INSERT INTO Sell ( name , email, password,username, cookies) VALUES (?, ?, ?, ?, ?)', (i[1], i[2], i[3],i[4], i[5]))
#     cursor.execute(f'DELETE FROM account WHERE email = "{i[2]}" ')
# data = cursor.execute("SELECT * FROM account  WHERE groupname = 'wait' ").fetchall()

# حذف السجلات المكررة
# duplicate_rows_query = "SELECT email, COUNT(*) FROM account GROUP BY email HAVING COUNT(*) > 1"
# duplicate_rows = cursor.execute(duplicate_rows_query).fetchall()
# for row in duplicate_rows:
#     primary_key_value = row[0]
#     input(primary_key_value)
#     delete_query = f" DELETE FROM account WHERE email = '{primary_key_value}' "
#     cursor.execute(delete_query)

conn.commit()
