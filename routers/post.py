from site import PREFIXES
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Auth.oauth2 import get_current_user
from routers.schemas import PostBase, PostDisplay
from db.database import get_db
from db import db_post
from typing import List
from routers.schemas import UserAuth





router = APIRouter(
  prefix='/post',
  tags=['post']
)

@router.post("",response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends (get_db),get_current_user: UserAuth = Depends(get_current_user)):
    return db_post.create(request, db)

@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
  return db_post.get_all(db)   

@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), create_user: UserAuth = Depends(get_current_user)):
   return db_post.delete(id, db)