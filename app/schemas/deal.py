from pydantic import BaseModel
from typing import Optional

class DealBase(BaseModel):
    title: str
    amount: int
    status: str
    client_id: int
    
class DealCreate(DealBase):
    pass

class DealUpdate(BaseModel):
    title: Optional[str]
    amount: Optional[int]
    status: Optional[str]
    client_id: Optional[int]

class DealOut(DealBase):
    id: int
    
    class Config:
        orm_mode=True
