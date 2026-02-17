from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def index():
    return {'message':'Hello world'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return{'message':f'This is a blog with {id}'}

@app.get('blog/all')
def get_all_blog():
    return {'message': 'These are all the blogs'}



