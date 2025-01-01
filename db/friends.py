from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import db_user
from db.database import get_db
from db.models import DbUser
from schemas import Friend_Request, User

router = APIRouter(
    prefix="/friends",
    tags=["friends"]
)

@router.get('/{id}')
def get_friends(id: int, db: Session = Depends(get_db)):
    return db_user.get_friends(id, db)


@router.put("/{id}/send")
def send_friend_request(id: int, request: User, db: Session = Depends(get_db)):
    return db_user.send_request(id, request, db) 


@router.put("/{id}/aprove")
def approve_friend_request(id: int, request: Friend_Request, db: Session = Depends(get_db)):
    return db_user.approve_request(id, request, db) 


@router.put("/{id}/deny")
def dreny_friend_request(id: int, request: Friend_Request, db: Session = Depends(get_db)):
    return db_user.deny_request(id, request, db)