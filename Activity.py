import sqlite3
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
