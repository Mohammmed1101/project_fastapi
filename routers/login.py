from fastapi import APIRouter, status, HTTPException, Depends
import schemas, main, models
import jwToken
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends()):
    user = main.db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")

    # if not hashing.Hash.verify(user.password, request.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")

    access_token = jwToken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}