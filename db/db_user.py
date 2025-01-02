from urllib import request
from fastapi import HTTPException, status
from db.models import DbFriendship, DbUser
from routers.schemas import User, UserBase, Friend_Request
from sqlalchemy.orm import Session
from db.hashing import Hash


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

def get_friends(db: Session, id: int):
    user = db.query(DbFriendship).filter(DbFriendship.user_id == id).first()
    return user.friends_id

# id is my id, request I want to be your friend
def send_request( id: int, request:User, db: Session):
    user = db.query(DbUser).filter(DbUser.id == request.id) 
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {request.id} not found")
    
    friendship = db.query(DbFriendship).filter(DbFriendship.user_id == request.id)
    
    if not friendship.first():
        friendship.create({
            DbFriendship.user_id: request.id,
            DbFriendship.friends_id: [],
            DbFriendship.requests: [id]
        })
        db.commit()
    else:
        request_list = friendship.first().requests
        friendship.update({
            DbFriendship.requests: request_list.append(id)
        })
    request_list = set( user.first().requests)
    request_list.add(id)
    
    user.update({
        DbUser.requests: list (request_list)
     })
    db.commit()
    
    return f"Request was sent to user with id {request.id}  "

def approve_request(id: int, request: Friend_Request, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id)  

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {request.id} not found")  
    
    request_list = set(user.first().requests) 
    if request.new_friend_id in request_list:
        request_list.remove(request.new_friend_id)
        
    friends_list = set( user.first().friends )
    friends_list.add(request.new_friend_id)
        
    user.update({
        DbUser.requests: list( request_list),
        DbUser.friends: list( friends_list)
        })
    requestUser = db.query(DbUser).filter(DbUser.id == request.new_friend_id)
    requestUser_friends= set()
 
    if not requestUser.first().friends is None:
         requestUser_friends = set(requestUser.first().friends)

    requestUser_friends.add(user.first().id)
    requestUser.update({DbUser.friends: list(requestUser_friends)})
 
    db.commit()
    
    return f"Friend with id {request.new_friend_id} was added to your friends list "

def deny_request(id: int, request: Friend_Request, db: Session):
    user = db.query(DbUser).filter(DbUser.id == id)  

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {request.id} not found")  
    
    request_list = user.first().requests 
    if request.new_friend_id in request_list:
        request_list.remove(request.new_friend_id)
        
       
    user.update({
        DbUser.requests: request_list
      
    })
    db.commit()
    
    return f"Friend with id {request.new_friend_id} was remoadded to your friends list "
       