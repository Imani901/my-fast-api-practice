from fastapi import FastAPI
from routers import blog_get
from routers import blog_post
from db import models
from db.database import engine
from routers import user

app= FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)

@app.get('/')
def index():
    return {'message':'Hello world'}

models.Base.metadata.create_all(engine)
