from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///Database.db')
Base = declarative_base()

class Profile(Base):
    __tablename__ = 'Profile'
    id_student = Column(Integer,primary_key=True)
    Name = Column(String)
    Fullname = Column(String)
    Dateofbirth = Column(String)
    Birthplace = Column(String)
    Nationality = Column(String)
    Education = Column(String)
    Disease = Column(String)
    Relative = Column(String)
    PhoneforEmergency = Column(String)
    Phonestudent = Column(String)
    Address = Column(String)
    Email = Column(String)
    # activity = relationship("Activity")


class Activity(Base):
    __tablename__ = 'Activity'
    id_student = Column(Integer,primary_key=True)
    NameActivity = Column(String)
    Description = Column(String)
    Photo = Column(String)#change next time
    Type = Column(String)
    Advisor = Column(String)
    Date_Activity = Column(String)
    File = Column(String)#change next time
    Confirm = Column(String)
    # profile_id = Column(Integer, ForeignKey("Profile.id"))

Session = sessionmaker(bind=db)
session = Session()
Base.metadata.create_all(db)
query = session.query(Profile)
Acque = session.query(Activity)

class Method:

    def __init__(self,data):

        self.data = data

    def name(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Name)
            return user.Name

    def date(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Dateofbirth)
            return user.Dateofbirth

    def birth(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Birthplace)
            return user.Birthplace

    def nation(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Nationality)
            return user.Nationality

    def education(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Education)
            return user.Education

    def disease(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Disease)
            return user.Disease

    def relative(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Relative)
            return  user.Relative

    def PhoneEmer(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.PhoneforEmergency)
            return user.PhoneforEmergency

    def Phonestu(self):
        for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Phonestudent)
            return user.Phonestudent

    def address(self):
         for user in query.filter_by(id_student="{}".format(self.data)):
            print(user.Address)
            return user.Address

    def email(self):
        for user in query.filter_by(id_student = "{}".format(self.data)):
            print(user.Email)
            return user.Email


    def Act_name(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.NameActivity)
            return user.NameActivity

    def Act_des(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.Description)
            return user.Description

    def Act_photo(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.Photo)
            return user.Photo

    def Act_type(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.Type)
            return user.Type

    def Act_advisor(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.Advisor)
            return user.Advisor

    def Act_Date(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.Date_Activity)
            return user.Date_Activity

    def Act_file(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.File)
            return user.File

    def Act_confirm(self):
        for user in Acque.filter_by(id_student = "{}".format(self.data)):
            print(user.Confirm)
            return user.Confirm

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
        addData = session.query(Profile).filter_by(id_student="{}".format(self.id)).one()
        addData.Disease = "{}".format(data)
        session.add(addData)
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


add = Add_Method(59340500008)
add.nameAct("Chakputtana")