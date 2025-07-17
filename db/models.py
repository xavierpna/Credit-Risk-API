from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    gender = Column(String)
    email = Column(String)
    phone_number = Column(String)
    registration_date = Column(String)
    age = Column(Integer)
    estimated_monthly_income = Column(Integer)
    employment_status = Column(String)
    credit_score = Column(Integer)
    location = Column(String)
    group_member = Column(Boolean)
    device_type = Column(String)
    referral_source = Column(String)
    default_flag = Column(Float)
    risk = Column(String)