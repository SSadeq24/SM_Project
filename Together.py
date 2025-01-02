from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user
from routers import post
from Auth import authentication
from user import user_router
from post import post_router
from .db.models import DbUser, DbPost
from routers.post import DbPost
from routers.user import DbUser

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)

# Include routes
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(post_router, prefix="/posts", tags=["Posts"])

@app.get('/')
def root():

    return {"message": "Welcome to the Social Network API (ToGether), by: Samar, Sadeq, Serhiy and Ali "}

models.Base.metadata.create_all(engine)