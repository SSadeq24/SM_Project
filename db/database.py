from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from db.models import DbUser, DbPost
from post import posts
import user
 
SQLALCHEMY_DATABASE_URL = 'sqlite:///./Together.db'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_user(username: str, hashed_password: str):
    user[username] = {"password": hashed_password, "posts": []}

def save_post(author: str, content: str):
    posts.append({"author": author, "content": content})       