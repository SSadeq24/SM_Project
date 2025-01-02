from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbUser
from routers.schemas import UserDisplay
from db import db_user
from routers.schemas import UserBase

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db_user import create_user, get_user_by_username

user_router = APIRouter()


router = APIRouter(
    prefix='/user',
    tags=['user']
)
@router.post('',response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)

    
        
class UserCreate(BaseModel):
    username: str
    password: str

@user_router.post("/")
async def register_user(user: UserCreate):
    if get_user_by_username(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    user = create_user(user.username, user.password)
    return user #{"message": "User registered successfully"}
