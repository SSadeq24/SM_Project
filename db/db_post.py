from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import polymorphic_union
from sqlalchemy.orm.session import Session
from db.models import DbPost
from routers.schemas import PostBase
from routers.schemas import PostDisplay
from fastapi import HTTPException, status

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