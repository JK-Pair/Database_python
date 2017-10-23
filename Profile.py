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

    def phone(self,row):
        print("Phone = ",row[7])

    def address(self,row):
        print("Address = ",row[8])

    def email(self,row):
        print("E-maill = ",row[9])

    def alldata(self,row):
        for item in row:
            print(item)
