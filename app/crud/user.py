from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

def get_password_hash(password: str):
    return pwd_context.hash(password)

# ============= READ =============
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()

# ============= CREATE =============
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

# ============= UPDATE =============
def update_user(db: Session, user_id: int, user_update: UserUpdate):
    user = get_user(db, user_id)
    if not user:
        return None
    
    if user_update.email is not None:
        user.email = user_update.email
        
    if user_update.name is not None:
        user.name = user_update.name

    if user_update.password is not None:
        user.hashed_password = get_password_hash(user_update.password)

    
    db.commit()
    db.refresh(user)
    return user

# ============= DELETE =============
def delete_user(db: Session, user_id:int):
    user = get_user(db, user_id)
    if not user:
        return None
    
    db.delete(user)
    db.commit()
    return user
    
    
    