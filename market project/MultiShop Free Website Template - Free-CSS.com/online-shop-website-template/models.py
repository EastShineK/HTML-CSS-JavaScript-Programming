from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    client_id = Column(String)
    client_secret = Column(String)
    
class UserInfo(Base):
    __tablename__ = "userinfos"
    
    id = Column(Integer, primary_key=True)
    userid = Column(String)
    password = Column(String)
    name = Column(String)
    membertype = Column(String) 
    
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    place = Column(String)
    phonenum = Column(String)
    auction = Column(String)
    purchased = Column(String)
    progress = Column(String)