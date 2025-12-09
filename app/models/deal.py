from app.database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

class Deal(Base):
    __tablename__ = "deals"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    amount = Column(Integer)
    status = Column(String(255), default="new", index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    
    client = relationship("Client")