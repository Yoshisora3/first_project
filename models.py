from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Notepad(Base):
    __tablename__ = 'notes'
    noteid = Column(Integer, primary_key=True)
    note = Column(String)
    userid = Column(String, ForeignKey('users.id'))

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    pw = Column(String)