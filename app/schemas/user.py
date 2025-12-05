from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str # поле для ввода пароля пользователем
    
class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    password: Optional[str] = None

class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # для Pydantic v2 вместо orm_mode

    