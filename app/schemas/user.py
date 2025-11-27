from pydantic import BaseModel

# base schema
class UserBase(BaseModel):
    email: str
    name:str
    
class UserCreate(UserBase):
    password: str # used for creating a user; store hashed_password in DB
    
class UserOut(UserBase):
    id: int
    
    class Config:
        orm_mode = True
    