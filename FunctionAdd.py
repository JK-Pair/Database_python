from sqlalchemy import *
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base
db = create_engine('sqlite:///Database.sqlite')
Base = declarative_base()

class Profile(Base):
    __tablename__ = 'Profile'
    id = Column(Integer,primary_key=True)
    id_student = Column(String)
    Name = Column(String)
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
    activity = relationship("Activity")


class Activity(Base):
    __tablename__ = 'Activity'
    id = Column(Integer,primary_key=True)
    NameActivity = Column(String)
    Description = Column(String)
    Photo = Column(String)#change next time
    Type = Column(String)
    Advisor = Column(String)
    Date_Activity = Column(String)
    File = Column(String)#change next time
    Confirm = Column(String)
    profile_id = Column(Integer, ForeignKey("Profile.id"))



session = sessionmaker()
session.configure(bind=db)
Base.metadata.create_all(db)
s = session()
sth = Profile(Name = "something")
s.add(sth)
s.commit()









