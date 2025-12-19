from pydantic import BaseModel
from typing import Optional

class ClientBase(BaseModel):
    name: str
    phone: str
    email: str

class ClientCreate(ClientBase):
    # used for creating a client; can add password later if client login is needed
    pass

class ClientUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    email: Optional[str]

class ClientOut(ClientBase):
    id: int
    
    class Config:
        from_attributes = True