import sqlite3
class Profile:
    def __init__(self,file):
        self.file = file

    def conne(self):
        return sqlite3.connect("{}".format(self.file))

    def name(self,row):
        print("name = ",row[0])

    def date(self,row):
        print(" Date of birth = ",row[1])

    def birthplace(self,row):
        print("Birthplace = ",row[2])

    def nation(self,row):
        print("Nationality = ",row[3])

    def education(self,row):
        print("Education = ",row[4])

    def disease(self,row):
        print("Disease = ",row[5])

    def relative(self,row):
        print("Relative = ",row[6])

    def phoneforEmer(self,row):
        print("Phone for Emergency : ",row[7])

    def phone(self,row):
        print("Phone = ",row[8])

    def address(self,row):
        print("Address = ",row[9])

    def email(self,row):
        print("E-maill = ",row[9])

    def alldata(self,row):
        for item in row:
            print(item)

class Activity:
    def __init__(self,file):
        self.file = file

    def conne(self):
        return sqlite3.connect("{}".format(self.file))

    def nameAct(self,row):
        print("Name Activity = ",row[0])

    def description(self,row):
        print("Description = ",row[1])

    def photo(self,row):
        print("Photo = ",row[2])

    def type(self,row):
        print("Type = ",row[3])

    def advisor(self,row):
        print("Adisor = ",row[4])

    def dateAct(self,row):
        print("Date = ",row[5])

    def file(self,row):
        print("File = ",row[6])

class AcademicTable:
    def __init__(self,file):
        self.file = file

    def conne(self):
        return sqlite3.connect("{}".format(self.file))

    def subID(self,row):
        print("Subject ID = ",row[1])

    def subName(self,row):
        print("Name subject = ",row[2])

    def credit(self,row):
        print("Credits = ",row[3])

    def acaReg(self,row):
        print("Academic regcord = ",row[4])

    def alldata(self,row):
        for item in row:
            print(item)

class Table:

    def call_profile(self):
        pro = Profile('59340500017.db')
        connePro = pro.conne()
        cursorPro = connePro.cursor()
        cursorPro.execute("SELECT * FROM PROFILE")
        roww = cursorPro.fetchone()
        return pro.name(roww) # You have to change name follow function in class Profile.

    def call_activity(self):
        act = Activity('59340500021.db')
        conneAct = act.conne()
        cursorAct = conneAct.cursor()
        cursorAct.execute("SELECT * FROM ACTIVITY")
        roww = cursorAca.fetchone()
        return act.photo(roww) # You have to change photo follow function in class Profile.

    def call_academic(self):
        aca = AcademicTable('59340500035.db')
        conneAca = aca.conne()
        cursorAca = conneAca.cursor()
        cursorAca.execute("SELECT * FROM '2/2559'") #You have to change 2/2559 follow term and year that study.
        roww = cursorAca.fetchone()
        return aca.subID(roww) # You have to change subID follow function in class Profile.
