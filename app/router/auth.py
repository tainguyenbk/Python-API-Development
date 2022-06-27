from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app import models, schemas, utils, oauth2

from .. import database

router = APIRouter(tags = ['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create a token

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    #return token
    return {"access_token": access_token, "token_type": "bearer"}