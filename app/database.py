from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#'postgresql://<username>:<password>@<zip-adress/hostname>/<database_name>'
#Hämtas från environment variables som körs lokalt i .env filen istället för globalt
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}' 

#Ansvarar för att etablera anslutning
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Pratar med databasen
sessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()


#dfunktion som skapar en session till servern/databasen, exekverar kod och stänger anslutningen
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()