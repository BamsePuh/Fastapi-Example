#from unittest import result
from sqlalchemy import func
from fastapi import  status, HTTPException,Depends, APIRouter
from ..import models,schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional

#Routa om allt från @app till @router
router = APIRouter(
    prefix="/posts",
    tags = ['POSTS'] 
)

#Get-req för att läsa ut alla posts genom en modell och en session som skapas av get_db


#path = http://127.0.0.1:8000/posts?limit=2&skip=2%search=str
#begränsar antal träffar från URL http://127.0.0.1:8000/posts?limit=3&search=pulp
#search = .contains(search)
#limit = .limit(limit)
#skip = .offset(skip)
#%20 är mellanslag i URL
@router.get ("/",   response_model= list[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user), 
limit: int = 50,skip: int = 0, search: Optional[str] = ""):

    #posts=db.query(models.Posts).filter(models.Posts.title.contains(search)).limit(
    #    limit).offset(skip).all()

    posts = db.query(models.Posts, func.count(models.Votes.post_id).label("likes")).join(
        models.Votes, models.Votes.post_id == models.Posts.id, isouter = True).group_by(models.Posts.id).filter(
            models.Posts.title.contains(search)).limit(
        limit).offset(skip).all()
        

    return posts

#path = http://127.0.0.1:8000/posts
#Skapa en variabel från modellen/schemat "CreatePosts" och packar upp alla kolumner genom **
@router.post ("/", status_code=status.HTTP_201_CREATED, response_model = schemas.PostResponse)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

#Konventera allt i modellen till en py-dict och packar upp alla kolumner genom **
#lägger till posten i databasen
#Committar posten till databasen
#lagrar committen till new_post för att presentera resultatet tillbaka i applikationen 
    new_post=models.Posts(owner_id = current_user.id,**post.dict())   
    db.add(new_post) 
    db.commit()
    db.refresh(new_post)        
    return new_post

 
#Get request för att plocka ut enstaka movies
#path = http://127.0.0.1:8000/posts/id
@router.get ("/{id}", response_model= schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    #post=db.query(models.Posts).filter(models.Posts.id == id).first() #filtrerar på id och returnerar första träffen via .first()

    post= db.query(models.Posts, func.count(models.Votes.post_id).label("likes")).join(
        models.Votes, models.Votes.post_id == models.Posts.id, isouter = True).group_by(models.Posts.id).filter(
            models.Posts.id == id).first()

    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")

    return post


#Delete post per id
#path = http://127.0.0.1:8000/posts/1
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    delete_post_query = db.query(models.Posts).filter(models.Posts.id == id)
    post = delete_post_query.first()
  
    if post == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found") 

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You can't delete this post")

    delete_post_query.delete(synchronize_session=False)
    db.commit()

    return {'Post was sucessfully deleted'}


#update Posts
#path = http://127.0.0.1:8000/posts/1
@router.put("/{id}",response_model = schemas.PostResponse)
def update_post(id: int,updated_post: schemas.UpdatePost,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    update_post = db.query(models.Posts).filter(models.Posts.id == id)

    post = update_post.first()

    if post == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found") # Skicka en 404 om id saknas

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You can't update this post")

    update_post.update(updated_post.dict(),synchronize_session=False)
    db.commit()

    return update_post.first()