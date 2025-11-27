from app.database import Base
from sqlalchemy import Integer, Column, String

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, unique=True)    
    email = Column(String, unique=True, index=True)