from fastapi import APIRouter, status, HTTPException, Response, Depends
import schemas, main, models
from typing import Optional,List
from crud_project import crud_post
import oauth2
router = APIRouter(tags=["Posts"], prefix="/post")

@router.get('/', response_model=List[schemas.Post],status_code=200)
def get_all(current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_post.get_all()


@router.post('/', response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
def create_an_post(post: schemas.Post, current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_post.create(post)

@router.get('/{post_id}',response_model=schemas.Post,status_code=status.HTTP_200_OK)
def get_an_post(post_id: int, current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_post.get_post(post_id)

@router.put('/edit/{post_id}',response_model=schemas.Post,status_code=status.HTTP_200_OK)
def update_an_post(post_id:int,post:schemas.Post, current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_post.update(post_id, post)


@router.delete('/delete/{post_id}')
def delete_post(post_id: int, current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_post.delete(post_id)