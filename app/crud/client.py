from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate

# ============= READ =============
def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_clients(db: Session):
    return db.query(Client).all()

# ============= CREATE =============
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

# ============= UPDATE =============
def update_client(db:  Session, client_id: int, client_update: ClientUpdate):
    client = get_client(db, client_id)
    if not client:
        return None
    
    if client_update.email is not None:
        client.email = client_update.email
        
    if client_update.name is not None:
        client.name = client_update.name

    if client_update.phone is not None:
        client.phone = client_update.phone
    
    
    db.commit()
    db.refresh(client)
    return client

# ============= DELETE =============
def delete_client(db: Session, client_id: int):
    client = get_client(db, client_id)
    if not client:
        return None
    
    db.delete(client)
    db.commit()
    return client