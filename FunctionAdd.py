from sqlalchemy import *
from sqlalchemy.orm import *
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


Session = sessionmaker(bind=db)
session = Session()
Base.metadata.create_all(db)

# # sth = Profile(id_student = "59340500021",Name = "Thipawan",Dateofbirth = "14/02/40",Birthplace = "Hospital",Nationality = "Thai",Education = "Bungkan",Disease = "None",Relative = "dad",PhoneforEmergency = "0967876",Phonestudent = "096235333" ,Address = "Buayai",Email = "pair@gmail.com")
# session.add(sth)
# session.commit()
query = session.query(Profile)
for user in query.filter_by(Name='Thipawan'):
    print(user.Email)







