import sqlite3
class Profile:
    def __init__(self,file):
        self.file = file

    def conne(self):
        return sqlite3.connect("{}".format(self.file))

    def idstudent(self,row):
        print("ID = ",row[0])

    def name(self,row):
        print("name = ",row[1])

    def date(self,row):
        print(" Date of birth = ",row[2])

    def birthplace(self,row):
        print("Birthplace = ",row[3])

    def nation(self,row):
        print("Nationality = ",row[4])

    def education(self,row):
        print("Education = ",row[5])

    def disease(self,row):
        print("Disease = ",row[6])

    def relative(self,row):
        print("Relative = ",row[7])

    def phone(self,row):
        print("Phone = ",row[8])

    def address(self,row):
        print("Address = ",row[9])

    def email(self,row):
        print("E-maill = ",row[10])

    def alldata(self,row):
        for item in row:
            print(item)
