from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import polymorphic_union
from sqlalchemy.orm.session import Session
from db.models import DbPost
from routers.schemas import PostBase
from routers.schemas import PostDisplay
from fastapi import HTTPException, status
from database import save_post
from models import posts, users
from db_user import get_user_by_id

def create(request: PostBase, db: Session):
     new_post = DbPost(
        title = request.title,
        content = request.content,
        timestamp = datetime.now(),
        user_id = request.user_id
        
     )
     db.add(new_post)
     db.commit()
     db.refresh(new_post)
     return new_post

def get_all(db: Session):
  return db.query(DbPost).all()

def delete(id: int, db: Session):
   post = db.query(DbPost).filter(DbPost.id == id).first()
   if not post:
      return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail='Post with id {d} not found)')
   if post.user.id != id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
      detail='Only post creator can delete post')
   db.delete(post)
   db.commit()
   return 'ok'

def create_post(author: str, content: str):
    if author not in users:
        raise ValueError("Author not found")
    save_post(author, content)

def get_wall_posts(username: str):
    user = users.get(username)
    if not user:
        return []
    return [post for post in posts if post["author"] == username or post["author"] in user.get("friends", [])]

def get_wall_posts_by_user(author_id: int):
    return [post for post in posts if post["author_id"] == author_id]

def get_wall_for_user(user_id: int):
    user = get_user_by_id(user_id)
    return [post for post in posts if post["author"] in user.get("friends", [])]

def get_wall_post(id: int):
    #post = db.query(DBPost).filter(DBPost.id == id).first()
    #users.get(username)
    return {id: id}