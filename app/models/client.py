from app.database import Base
from sqlalchemy import Integer, Column, String

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    phone = Column(String(255), unique=True)    
    email = Column(String(255), unique=True, index=True)