from fastapi import FastAPI
from db import models
from db.database import engine, Base
from routers import user, friends, post
from routers import post
from Auth import authentication
from db.models import Base 


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(friends.router)

@app.get('/')
def root():
    return {"message": "Welcome to LinkUp, a social network project by Samar, Sadeq, Serhiy, and Ali"}

models.Base.metadata.create_all(engine)

Base.metadata.create_all(engine)

