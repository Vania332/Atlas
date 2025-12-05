from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud import user as crud_user
from app.database import get_db
from app.database import Base, engine
from colorama import init, Fore
from app.models.user import User  


app = FastAPI()

