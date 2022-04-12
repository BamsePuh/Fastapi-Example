from fastapi import Path
from pydantic import BaseSettings
from dotenv import load_dotenv

my_file = load_dotenv('E:\Fastapi\.env')


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    class config:
        my_file



settings = Settings()