from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.client import ClientCreate, ClientOut, ClientUpdate

from app.crud import client as crud_client


router = APIRouter(prefix="/clients", tags=["Clients"])

# ============= get =============
@router.get("/",response_model=list[ClientOut])
def get_clients(db: Session = Depends(get_db)):
    return crud_client.get_clients(db)

@router.get("/{client_id}", response_model=ClientOut)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = crud_client.get_client(db, client_id)

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

# ============= post =============
@router.post("/", response_model=ClientOut)
def create_client(client_create: ClientCreate, db: Session = Depends(get_db)):
    exiting = crud_client.get_client_by_email(db, client_create.email)
    if exiting:
        raise HTTPException(status_code=400, detail="Email already registred")
    return crud_client.create_client(db, client_create)

# ============= put(patch) =============
@router.put("/{client_id}", response_model=ClientOut)
def update_client(client_id: int, payload: ClientUpdate, db: Session = Depends(get_db)):
    updated = crud_client.update_client(db, client_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Client not found")
    return updated

# ============= delete =============
@router.delete("/{client_id}", response_model=ClientOut)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted = crud_client.delete_client(db, client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client not found")
    return deleted
