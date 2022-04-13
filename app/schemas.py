from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint


class CreateUser(BaseModel):
    email: EmailStr
    password: str

class CreateUserResponse(BaseModel): #Extenda inte CreateUser eftersom den innehåller password
        email: EmailStr

        class Config:
            orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Skapa en class för att definera hur en POST request ska hanteras
class PostBase(BaseModel):
    title: str
    content: str
    cat: str
    published: bool = True #Default till true om det inte ansätts i anropet
    

class CreatePost(PostBase):
    pass

class UpdatePost(PostBase):
   pass

# Skapa en class/schema som definerar hur svaret till användaren ser ut
class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: CreateUserResponse #Returnerar en pyndatic modell av klassen CreateUserReponse

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Posts: PostResponse
    likes: int
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    direct: conint(ge=0,le=1)
    #@validator('direct')
    #def must_be_one_or_zero(cls,value):
     #   if value not in(0,1):
      #      raise ValueError("Must be either 1 or 0")
       # return value
