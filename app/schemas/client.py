from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    phone: str
    email: str

class ClientCreate(ClientBase):
    # used for creating a client; can add password later if client login is needed
    pass

class ClientOut(ClientBase):
    id: int
    
    class Config:
        orm_mode=True