import datetime

a = datetime.datetime.strptime("05/2004", "%m/%Y")
print(a.date())


import sqlite3

conn = sqlite3.connect("RSKT.db")
cur = conn.cursor()
sql = "select paid_for from receipt"
cur.execute(sql)
items = cur.fetchall()
conn.commit()
conn.close()


import threading
threading.Thread(target=print, args=(5, )).start()