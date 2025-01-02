from urllib import request
from db.models import DbUser
from routers.schemas import UserBase
from sqlalchemy.orm import Session
from db.hashing import Hash
from database import save_user
from db.hashing import hash_password
from models import users


def create_user(request: UserBase, db: Session):
    new_user = DbUser(username=request.username, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
  user = db.query(DbUser).filter(DbUser.username == username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with username {username} not found')
  return user

def create_user(username: str, password: str):
    hashed_password = hash_password(password)
    save_user(username, hashed_password)

def get_user_by_username(username: str):
    return users.get(username)

def get_user_by_id(user_id: int):
    return users.get()#where id == user_id