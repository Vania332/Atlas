from sqlalchemy.orm import Session
from models.client import Client
from schemas.client import ClientCreate

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def create_client(db: Session, client_create: ClientCreate):
    client = Client(
        name = client_create.name,
        phone = client_create.phone,
        email = client_create.email,
    )
    db.add(client)
    db.commit()
    db.refresh(client)
    return client