import sqlite3
from Profile import Profile
conne = sqlite3.connect("Profiledata.db")
conne.row_factory = sqlite3.Row
cursor = conne.cursor()
cursor.execute("SELECT * FROM PROFILE")

pro = Profile()
roww = cursor.fetchone()
pro.alldata(roww)
