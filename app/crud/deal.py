from sqlalchemy.orm import Session
from app.models.deal import Deal
from app.schemas.deal import DealCreate, DealUpdate


# ============= READ =============
def get_deal(db: Session, deal_id: int):
    return db.query(Deal).filter(Deal.id == deal_id).first()

def get_deals(db: Session):
    return db.query(Deal).all()

# ============= CREATE =============
def create_deal(db: Session, deal_create: DealCreate):
    deal = Deal(
        title = deal_create.title,
        amount = deal_create.amount,
        status = deal_create.status,
        client_id = deal_create.client_id,
    )
    db.add(deal)
    db.commit()
    db.refresh(deal)
    return deal

# ============= UPDATE =============
def update_deal(db: Session, deal_id: int, deal_update: DealUpdate):
    deal = get_deal(db, deal_id)
    if not deal:
        return None
    
    if deal_update.title is not None:
        deal.title = deal_update.title
        
    if deal_update.amount is not None:
        deal.amount = deal_update.amount   

    if deal_update.status is not None:
        deal.status = deal_update.status
        
    if deal_update.client_id is not None:
        deal.client_id = deal_update.client_id
    
    db.commit()
    db.refresh(deal)
    return deal

# ============= UPDATE =============
def delete_deal(db: Session, deal_id: int):
    deal = get_deal(db, deal_id)
    if not deal:
        return None
    
    db.delete(deal)
    db.commit()
    return deal