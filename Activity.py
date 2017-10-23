
class Activity:
    def __init__(self,file):
        self.file = file

    def conne(self):
        return sqlite3.connect("{}".format(self.file))

    def idAct(self,row):
        print("ID student = ",row[0])

    def nameAct(self,row):
        print("Name Activity = ",row[1])

    def description(self,row):
        print("Description = ",row[2])

    def photo(self,row):
        print("Photo = ",row[3])

    def type(self,row):
        print("Type = ",row[4])

    def advisor(self,row):
        print("Adisor = ",row[5])

    def dateAct(self,row):
        print("Date = ",row[6])

    def file(self,row):
        print("File = ",row[7])
