from fastapi import Body, FastAPI, Response, status, HTTPException,Depends, APIRouter
from ..import models,schemas,utils, oauth2
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/vote",
    tags = ['VOTE'] 
)

#if post does not exist?

@router.post ("/", status_code = status.HTTP_201_CREATED)
def vote_on_post(vote: schemas.Vote,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post_check = db.query(models.Posts).filter(models.Posts.id == vote.post_id).first()
    if not post_check:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "Post does not exist")

    vote_query= db.query(models.Votes).filter(models.Votes.post_id == vote.post_id, models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()

    if (vote.direct == 1):
        if found_vote:
            raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail= f"user {current_user.id} has already voted on post {vote.post_id}")
        
        new_vote = models.Votes(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Successfully added vote"}
           
    else:
        if not found_vote:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Successfully deleted vote"}


