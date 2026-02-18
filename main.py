from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app= FastAPI()

@app.get('/')
def index():
    return {'message':'Hello world'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return{'message': 'theses are all the blogs'}

@app.get(
        '/blog/all',
        tags=['blog'],
        summary='Retrieves all blogs',
        description='This API call simulates fetching all blogs',
        response_description='The list of available blogs'
        )
def get_all_blogs(page=1 , pagesize : Optional[int]= None):
    return {'message': f'All {pagesize } blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}', tags=['blog','comment'])
def get_comment(id:int, comment_id:int, valid: bool = True, Username: Optional[str]= None):
    """
    Simulates retrieving a BLog

    - **id** mandatory path parameter
    - **coment_id** mandatory path parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {Username}'}

class Blogtype(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get('/blog/type/{type}',tags=['blog'])  
def get_blog_type(type: Blogtype):  
    return {'massage':f"Blog type {type}"}

@app.get('/blog/{id}' ,status_code= status.HTTP_200_OK,tags=['blog'])
def get_blog(id: int, response= Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return{'message':f'This is a blog with id {id}'}

# @app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)
# def get_blog(id: int):
#     if id > 5:
#         return {'error': f'Blog with id {id} not found'}
#     else:
#         return {'message': f'This is th blog with id {id}'}
    
    







