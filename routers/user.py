from fastapi import APIRouter,Depends
import models, main, schemas
from crud_project import crud_user
import oauth2


router = APIRouter(tags=["Users"], prefix="/user")

@router.post('/', response_model=schemas.User)
def create_user(user: schemas.User, current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_user.create(user)

@router.get('/{id}', response_model=schemas.User)
def get_user(id: int, current_user:schemas.User = Depends(oauth2.get_current_user)):
    return crud_user.get(id)