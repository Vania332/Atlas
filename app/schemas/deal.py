from pydantic import BaseModel

class DealBase(BaseModel):
    title: str
    amount: int
    status: str
    client_id: int
    
class DealCreate(DealBase):
    pass

class DealOut(DealBase):
    id: int
    
    class Config:
        orm_mode=True
