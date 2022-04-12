from asyncio.format_helpers import _format_callback_source
from enum import unique
from typing import Counter
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, String,Boolean,ForeignKey
from .database import Base

#Definerar tabellstrukturen på tabellerna i postgressql

class User(Base):
    __tablename__= "users"
    id = Column(Integer,primary_key=True,nullable=False)
    #code = Column(String, nullable=False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Posts(Base):
    __tablename__= "posts"
    id = Column(Integer, primary_key=True,nullable=False)  
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    cat = Column(String,nullable=False)
    published = Column(Boolean,server_default='True',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    # skapar en relation mellan movies och users tabellerna
    owner_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)

    owner = relationship("User") #Skapar en relation till tabellen Users genom att kalla på modellen User. Används för att exempelvis presentera ett namn.

class Votes(Base):
    __tablename__="votes"
    user_id= Column(Integer,ForeignKey("users.id", ondelete = "CASCADE"),primary_key=True,nullable=False)
    post_id= Column(Integer,ForeignKey("posts.id", ondelete = "CASCADE"),primary_key=True,nullable=False)
  
