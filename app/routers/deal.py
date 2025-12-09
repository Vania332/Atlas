from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.deal import DealCreate, DealOut, DealUpdate

from app.crud import deal as crud_deal

router = APIRouter(prefix="/deals", tags=["Deals"])

# ============= get =============
@router.get("/", response_model=list[DealOut])
def get_deals(db: Session = Depends(get_db)):
    return crud_deal.get_deals(db)

@router.get("/{deal_id}", response_model=DealOut)
def get_deal(deal_id: int, db: Session = Depends(get_db)):
    deal = crud_deal.get_deal(db, deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal

# ============= post =============
@router.post("/", response_model=DealOut)
def create_deal(deal_create: DealCreate, db: Session = Depends(get_db)):
    exiting = crud_deal.get_deal_by_title_and_client(db, deal_create.title, deal_create.client_id)
    if exiting:
        raise HTTPException(status_code=400, detail="Deal with this title for this client already exists")
    return crud_deal.create_deal(db, deal_create)
    
# ============= put(patch) =============
@router.put("/{deal_id}", response_model=DealOut)
def update_deal(deal_id: int, payload: DealUpdate, db: Session = Depends(get_db)):
    updated = crud_deal.update_deal(db, deal_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Deal not found")
    return updated

# ============= delete =============
@router.delete("/{deal_id}", response_model=DealOut)
def delete_deal(deal_id: int, db: Session = Depends(get_db)):
    deleted = crud_deal.delete_deal(db, deal_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deleted
    