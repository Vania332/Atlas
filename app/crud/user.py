from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_create: UserCreate):
    hashed_password = get_password_hash(user_create.password)
    user =  User(
        email = user_create.email,
        name = user_create.name, 
        hashed_password = hashed_password,
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    
