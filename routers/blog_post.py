from fastapi import APIRouter, Query, Body
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


@router.post('/new/{id}/comment')      
def create_comment(blog: BlogModel,
                    id:int, 
                    comment_id:int= Query(None,
                    title= 'Id of the comment',
                    description='Some decription for comment_id',
                    alias='commentId',
                    deprecated= True
                    ),
                    content: str= Body(...,
                                       min_length=10,
                                       max_length=20
                                       )
  
                    ):
    return{
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content
    }
    
    