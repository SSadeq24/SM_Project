from turtle import title
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

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

class DbFriendship(Base):
    __tablename__ = "friendship"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    # friend_id = Column(Integer, ForeignKey('users.id'))
    # friendships = relationship("DbFriendship", foreign_keys="[DbFriendship.user_id]")
    friend_id = Column(Integer) 
   
class DbFriendships(Base):
     __tablename__ = "friendships"
     id = Column(Integer, primary_key=True, index=True)
     user_id = Column(Integer, ForeignKey('users.id'))
    # friend_id = Column(Integer, ForeignKey('users.id'))
    # friendships = relationship("DbFriendship", foreign_keys="[DbFriendship.user_id]")
     friends_id = Column(Integer) 
     friends_request = Column(Integer)

