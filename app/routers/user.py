from fastapi import status, HTTPException,Depends,APIRouter
from ..import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session

#Routa om allt från @app till @router
router = APIRouter(
    prefix="/users",
    tags = ['USERS']
)

#Post request för att skapa ny användare
#path = http://127.0.0.1:8000/users
@router.post ("/", status_code=status.HTTP_201_CREATED, response_model = schemas.CreateUserResponse)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    
    #hasha lösenordet - user.password
    hashed_pw = utils.hash(user.password)
    user.password = hashed_pw

    new_user=models.User(**user.dict())

    #Felhantering om email redan finns
    user_check= db.query(models.User).filter(models.User.email == new_user.email).first()
    if user_check == None:

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    else:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail =  "an user account with this email already exists")

    return new_user
    
    


#path = http://127.0.0.1:8000/users/id
@router.get('/{id}',response_model = schemas.CreateUserResponse)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "user was not found")

    return user