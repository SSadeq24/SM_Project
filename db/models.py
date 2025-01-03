from turtle import title
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import List, Dict


class DbUser(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbPost', back_populates='user')

class DbPost(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  timestamp = Column(DateTime)
  user_id = Column(Integer, ForeignKey('user.id'))
  user = relationship('DbUser', back_populates='items')

class DbPost(Base):
    __tablename__ = 'post'  
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class DbUser(Base):
    __tablename__ = 'user' 
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

user = relationship('DbUser', back_populates='items')