from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///DatabaseOne.db')
Base = declarative_base()

class Profile(Base):
    __tablename__ = 'Profile'
    id_student = Column(Integer,primary_key=True,nullable=False)
    Name = Column(String,nullable=False)
    Surname = Column(String,nullable=False)
    Sex = Column(String,nullable=False)
    Year = Column(Integer)
    Dateofbirth = Column(String)
    Birthplace = Column(String)
    Nationality = Column(String)
    Education = Column(String)
    Relative = Column(String)
    PhoneforEmergency = Column(String)
    Phonestudent = Column(String)
    Address = Column(String)
    Email = Column(String)

class Disease(Base):
    __tablename__ = 'Disease'
    id_student = Column(Integer,primary_key=True)
    Disease = Column(String,primary_key=True)

class Activity(Base):
    __tablename__ = 'Activity'
    id_student = Column(Integer,primary_key=True)
    NameActivity = Column(String,primary_key=True)
    Description = Column(String)
    Photo = Column(String)#change next time
    Type = Column(String)
    Advisor = Column(String)
    Date_Activity = Column(String)
    File = Column(String)#change next time
    Confirm = Column(String)



Session = sessionmaker(bind=db)
session = Session()
# Base.metadata.create_all(db)

query = session.query(Disease)
query = session.query(Profile)
Acque = session.query(Activity)
disquery = session.query(Disease)

class return_Method:

    def __init__(self,data):
        self.data = data

    def name(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Name

    def date(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Dateofbirth

    def birth(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Birthplace

    def nation(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Nationality

    def education(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Education

    def disease(self):
        box = []
        for user in disquery.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Disease)
        return box

    def relative(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return  user.Relative

    def PhoneEmer(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.PhoneforEmergency

    def Phonestu(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Phonestudent

    def address(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            return user.Address

    def email(self):
        for user in query.filter_by(id_student = "{}".format(self.data)):
            return user.Email

    def Act_name(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.NameActivity)
        return box

    def Act_des(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Description)
        return box

    def Act_photo(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Photo)
        return box

    def Act_type(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Type)
        return box

    def Act_advisor(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Advisor)
        return box

    def Act_Date(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Date_Activity)
        return box

    def Act_file(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.File)
        return box

    def Act_confirm(self):
        box = []
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            box.append(user.Confirm)
        return box

class Add_Method:

    def __init__(self,id):
        self.id = id

    def id_stu(self,method):
        sth = method(id_student = "{}".format(self.id))
        session.add(sth)
        session.commit()

    def name(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Name = "{}".format(data)
        session.add(addData)
        session.commit()

    def fullname(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Fullname = "{}".format(data)
        session.add(addData)
        session.commit()

    def date(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Dateofbirth = "{}".format(data)
        session.add(addData)
        session.commit()

    def nation(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Nationality = "{}".format(data)
        session.add(addData)
        session.commit()

    def education(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Education = "{}".format(data)
        session.add(addData)
        session.commit()

    def disease(self,data):
        sth = Disease(id_student = "{}".format(self.id),Disease = "{}".format(data))
        session.add(sth)
        session.commit()

    def relative(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Relative = "{}".format(data)
        session.add(addData)
        session.commit()

    def phoneEmer(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.PhoneforEmergency = "{}".format(data)
        session.add(addData)
        session.commit()

    def phonestu(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Phonestudent = "{}".format(data)
        session.add(addData)
        session.commit()

    def address(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Address = "{}".format(data)
        session.add(addData)
        session.commit()

    def email(self,data):
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.EmailDateofbirth = "{}".format(data)
        session.add(addData)
        session.commit()

    def nameAct(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.NameActivity = "{}".format(data)
        session.add(addData)
        session.commit()


    def descrip(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.Description = "{}".format(data)
        session.add(addData)
        session.commit()

    def photo(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.Photo = "{}".format(data)
        session.add(addData)
        session.commit()

    def type(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.Type = "{}".format(data)
        session.add(addData)
        session.commit()

    def advisor(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.Advisor = "{}".format(data)
        session.add(addData)
        session.commit()

    def dateAct(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.Date_Activity = "{}".format(data)
        session.add(addData)
        session.commit()

    def file(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.File = "{}".format(data)
        session.add(addData)
        session.commit()

    def confirm(self,data):
        addData = session.query(Activity).filter_by(id_student="{}".format(self.id)).one()
        addData.Confirm = "{}".format(data)
        session.add(addData)
        session.commit()

    def Dicdisease(self,Disease = None):
        dataAct = []
        for item in Disease:
            dicAct = {'id_student' : self.id, 'Disease ' : item}
            dataAct.append(dicAct)
        return dataAct

    def DicAct(self,NameAct = None, Descrip = None, Photo = None, Type = None, Advisor = None, Date = None, File = None, Confirm = None ):
        dataAct = []
        for item in range(len(NameAct)):
            dicAct = {'Name Activity' : NameAct[item], 'Description' : Descrip[item], 'Photo' : Photo[item], 'Type' : Type[item], 'Advisor' : Advisor[item], 'Date_Activity' : Date[item], 'File' : File[item], 'Confirm' : Confirm[item]}
            dataAct.append(dicAct)
        return dataAct
#
add = Add_Method(59340500017)
# # re = return_Method(59340500017)
# # print(add.Dicdisease(re.disease()))
#
# # re = return_Method(59340500035)
# add = Add_Method(59340500035)
# # print(add.DicAct(re.Act_name(), re.Act_des(), re.Act_photo(), re.Act_type(), re.Act_advisor(), re.Act_Date(), re.Act_file(), re.Act_confirm()))
#
add.id_stu(Activity,59340500017)
