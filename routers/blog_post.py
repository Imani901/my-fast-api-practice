from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

class BlogModel(BaseModel):
    title: str
    content: str
    no_of_comments: int
    published: Optional[bool]

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id = int, version: int= 1):
    return {
        'id': id,
        'version': version,
        'data': blog
        }