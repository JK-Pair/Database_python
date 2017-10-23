import sqlite3
from Profile import Profile
from Profile import Activity
pro = Activity('59340500021.db')
conne = pro.conne()
conne.row_factory = sqlite3.Row
cursor = conne.cursor()
cursor.execute("SELECT * FROM PROFILE")
roww = cursor.fetchone()
pro.nameAct(roww)
