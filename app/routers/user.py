from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserOut, UserCreate, UserUpdate

from app.crud import user as crud_user 


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    return user
    
@router.post("/", response_model=UserOut)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    exiting = crud_user.get_user_by_email(db, user_create.email)
    if exiting:
        raise HTTPException(status_code=400, detail="Email already registred")
    return crud_user.create_user(db, user_create)

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    updated = crud_user.update_user(db, user_id, payload)
       # определять что такие же поля используют другие юзеры raise HTTPException(status_code=400, detail="User already registred")
    if not updated:
        raise HTTPException(status_code=404, detail="User is not found")
    return updated

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud_user.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User is not found")
    return deleted
