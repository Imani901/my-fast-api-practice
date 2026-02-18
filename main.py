from fastapi import FastAPI
from routers import blog_get
from routers import blog_post

app= FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

@app.get('/')
def index():
    return {'message':'Hello world'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return{'message': 'theses are all the blogs'}

