import models, main, schemas
from passlib.context import CryptContext
from fastapi import status, HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create(user: schemas.User):
    hashed_pass = pwd_context.hash(user.password)
    new_user = models.User(
        username=user.name,
        email=user.email,
        password=hashed_pass,
    )

    main.db.add(new_user)
    main.db.commit()
    main.db.refresh(new_user)
    return new_user

def get(id: int):
    user = main.db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not Available")
    return user