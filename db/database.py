from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from db.models import DbUser, DbPost, DbFriendship, DbFriendships
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

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
        
        


# Simulated database (dictionary)
users_db = {}

# Function to get a user or create one if not exists
def get_user(username: str) -> user:
    if username not in users_db:
        users_db[username] = User(username)
    return users_db[username]




# Define the SQLite database URL
DATABASE_URL = "sqlite:///mydatabase.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)  # `echo=True` will log all SQL statements

# Create a base class for our models
Base = declarative_base()

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




