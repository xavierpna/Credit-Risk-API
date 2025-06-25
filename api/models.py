from pydantic import BaseModel

class CustomerInput(BaseModel):
    customer_id: str
    full_name: str
    gender: str
    email: str
    phone_number: str
    registration_date: str
    age: int
    estimated_monthly_income: int
    employment_status: str
    credit_score: int
    location: str
    group_member: bool
    device_type: str
    referral_source: str

class CustomerOutput(BaseModel):
    default_flag: float
    risk: str