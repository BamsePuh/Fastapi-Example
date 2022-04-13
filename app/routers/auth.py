#### Hanterar allt kring autentisering

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(
    tags = ['AUTH']
)
#http://127.0.0.1:8000/login
@router.post('/login', response_model = schemas.Token)
def login(user_login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

#{
    #"username": " "
    #"password": " "
#}
#Kollar om lösenordet stämmer överens med databasen
#utils.verify är en egen funktion som hashar det inmatade lösenordet och jämför med det lagrade hashade lösenordet
    user_check = db.query(models.User).filter(models.User.email == user_login.username).first()
    if user_check == None:
         raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify(user_login.password, user_check.password):
         raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "Invalid credentials")
    # Create token
    # Return token
    access_token = oauth2.create_access_token(data = {"user_id": user_check.id})

    return {"access_token": access_token, "token_type": "bearer"}



    
    

