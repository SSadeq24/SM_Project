from site import PREFIXES
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Auth.oauth2 import get_current_user
from routers.schemas import PostBase, PostDisplay
from db.database import get_db
from db import db_post
from typing import List
from routers.schemas import UserAuth
from fastapi import APIRouter
from db_post import create_post, get_wall_posts, get_wall_post
from pydantic import BaseModel
from typing import List, Optional

post_router = APIRouter()
class PostCreate(BaseModel):
    author: str
    content: str

class PostResponse(BaseModel):
    author: str
    content: str

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

@post_router.post("/")
async def create_new_post(post: PostCreate):
    create_post(post.author, post.content)
    return {"message": "Post created successfully"}

@post_router.get("/", response_model=List[PostResponse])
async def get_user_wall(posted_by: Optional[int] = None, user_id: Optional[int] = None):
    if posted_by is not None:
        return get_wall_posts_by_user(posted_by)
    if user_id is not None:
        return get_wall_for_user(user_id)
    
    return []#get_wall_posts(id)

@post_router.get("/{id}", response_model=List[PostResponse])
async def get_post(id: int):
    return get_wall_post(id)