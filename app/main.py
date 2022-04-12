from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import posts,user, auth,vote


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ["*"] = all domains
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Importera alla FASTapi routers från movies.py och user.py
app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#Path= http://127.0.0.1:8000 
@app.get("/") 
def root():
    return {"message": "HELLO :)"}











    #**********LEGACY***************
#from turtle import title, update
#from click import password_option
#from distutils.log import error
#from genericpath import exists
#from fastapi import Body, FastAPI, Response, status, HTTPException,Depends
#from sqlalchemy.orm import Session
#from .import models, schemas, utils
#from typing import Optional, List
#from enum import auto, unique
#from pydantic import BaseModel
#import time
#from random import randrange
#import psycopg2
#from psycopg2.extras import RealDictCursor

#array som lagrar data
#my_movies = []


#kodsnutt för att hitta indexet av en post i arrayn
#def find_index_movie(id):
 #   for i, p in enumerate(my_movies):
  #      if p['id'] == id:
   #         return i



#kodsnutt för att matcha inmatat id med lagrat id via en if sats
#def find_movie(id):
 #   for p in my_movies:
  #      if p["id"] == id:
   #         return p


#array som lagrar data i minnet
#my_movies = [{"title": "Game of thrones", "description": "You know nothing Jon Snow", "cat": "Fantasy","id": 1},
#{"title": "Star Wars", "description": "Luke, I am your father","cat": "SciFi","id": 2}]


#@app.post ("/movies", status_code=status.HTTP_201_CREATED)
#def create_posts(new_movie: movie):
#    print(new_movie.dict())
 #   post_dict = new_movie.dict() #omvandlar inmatningen till en python dict
  #  post_dict['id'] = randrange(0,1000000) #ansätter random int mellan 0-100000 för att härma SQL id från databasen
   # my_movies.append(post_dict)   #appendar till my_post array
    #return {"data": post_dict}  #returnera den skapade posten

#**********LEGACY***************


#**********LEGACY Psygocopg2 ***************
            #LÄS,SKRIV,DELETE och UPPDATERA GENOM ATT SKRIVA SQL 


#while loop för att försöka ansluta varannan sekund till sql servern
#while True:
#    try:
#        conn = psycopg2.connect(host= 'localhost', database= 'Fastapi', user='postgres', password= 'Kosha3817',
#        cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print("Database connection was successfull")
#        break
#    except Exception as error:
#        print("Connection to database failed")
#        print(error)
#        time.sleep(2)

#path = http://127.0.0.1:8000/movies
#Get alla movies genom att köra SQL queries via cursor.execute metoden
#@app.get ("/movies")
#def get_movies():
 #   cursor.execute("""SELECT * FROM movies""") #execute query with cursor.execute 
  #  movies = cursor.fetchall() #fetchall läser ut alla poster ur tabellen movies
   # return {"data": movies}


#Post request
#Inom funktionen create_movies används variabeln movie som anropar classen movie
#%s variabel inmatade värden från användaren. validering sker via movie.title (=första %s) och förhindrar SQL injections
#RETURNING * är en postgres funktion för att returnera värdet
#path = http://127.0.0.1:8000/movies
#@app.post ("/movies", status_code=status.HTTP_201_CREATED)
#def create_movie(movie: Movie):
 #   cursor.execute(""" INSERT INTO movies(title,description,cat) VALUES (%s,%s,%s) RETURNING *""",
  #  (movie.title,movie.description,movie.cat))

   # new_movie = cursor.fetchone()
    #conn.commit() # committar till databasen

    #return {"data": new_movie}



 #Get request för att plocka ut enstaka movies
#@app.get ("/movies/{id}")
#def get_movie(id: int):
 #   cursor.execute("""SELECT * FROM movies WHERE movies.id = %s""",(id,)) #(id,) eftersom det är en tuple som python inte kan tolka som en tuple utan ,
  #  movie = cursor.fetchone()
   # if movie==None:
    #    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"movie with id {id} was not found")
        #respons.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"post with id {id} was not found"}
    #return {"movie_detail": movie}   



#Delete movie per id
#@app.delete("/movies/{id}",status_code=status.HTTP_204_NO_CONTENT)
#def delete_post(id: int):
#
 #   cursor.execute("""DELETE FROM movies WHERE id = %s RETURNING* """,(id,))

#    deleted_movie = cursor.fetchone() # fetchar raden
 #   conn.commit() #committar delete till databasen

  #  if deleted_movie==None: 
   #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"movie with id {id} was not found") # Skicka en 404 om id saknas

    #return {'Message': f"movie was successfully deleted {deleted_movie}"}




#update movies
#@app.put("/movies/{id}",status_code=status.HTTP_204_NO_CONTENT)
#def update_movie(id: int,movie: Movie):

 #   cursor.execute("""UPDATE movies SET title = %s,description = %s,cat=%s WHERE id = %s RETURNING*""",(movie.title,movie.description,movie.cat,id))

  #  updated_movie=cursor.fetchone()
   # conn.commit()

    #if updated_movie == None: 
     #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"movie with id {id} was not found") # Skicka en 404 om id saknas

    #return {f"movie {movie.title} was updated"}

#**********LEGACY Psygocopg2 ***************





#***********LEGACY sqlalchemy*******

#läser alla poster ur databasen http://127.0.0.1:8000/sqlalchemy
#anropar movie modellen samt get_db för att skapa en session mot servern och databasen
#@app.get("/sqlalchemy")
#def test_posts(db: Session = Depends(get_db)):

 #   moviee=db.query(models.Movie).all()

  #  return {"Data": moviee}