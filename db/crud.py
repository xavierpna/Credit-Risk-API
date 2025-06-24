from sqlalchemy.orm import Session
from db.models import Customer

def save_customer(db: Session, customer_data: dict):
    customer = Customer(**customer_data)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer