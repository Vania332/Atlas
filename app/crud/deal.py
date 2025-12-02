from sqlalchemy.orm import Session
from app.models.deal import Deal
from app.schemas.deal import DealCreate


def get_deal(db: Session, deal_id: int):
    return db.query(Deal).filter(Deal.id == deal_id).first()

def get_deals(db: Session):
    deals = db.query(Deal).all()
    return deals

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