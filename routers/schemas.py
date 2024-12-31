from turtle import title
from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True

# For PostDisplay

class User(BaseModel):
  username: str
  class Config():
    orm_mode = True

# For PostDisplay
class PostDisplay(BaseModel):
  title: str
  content: str
  timestamp: datetime
  user: User
  class Config():
    orm_mode = True
    
class PostBase(BaseModel):
  title: str
  content: str
  user_id: int

class UserAuth(BaseModel):
  id: int
  username: str
  email: str
