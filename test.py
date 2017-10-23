import sqlite3
from Profile import Profile
pro = Profile('{}.db'.format())
conne = pro.conne()
cursor = conne.cursor()


cursor.execute("SELECT * FROM PROFILE")
roww = cursor.fetchone()
pro.name(roww)
