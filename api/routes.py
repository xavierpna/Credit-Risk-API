from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.models import CustomerInput, CustomerOutput
from api.utils import upload_model
from db.crud import save_customer
from db.db import SessionLocal
import numpy as np
import pandas as pd

router = APIRouter()

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()

# Cargar modelo y preprocesador
model, preprocessor = upload_model()

@router.post("/predict", response_model=CustomerOutput)
def default_predict(customer: CustomerInput):
    # Convertir entrada a Df
    data = pd.DataFrame([customer.dict()])

    # Preprocesar
    input_df = preprocessor.transform(data)

    # Realizar prediccion
    prob = model.predict_proba(input_df)[0][1]
    risk = "HIGH" if prob >= 0.7 else "MODERATED" if prob >= 0.4 else "LOW"

    return {
        "default_flag": round(prob, 2),
        "risk": risk
    }

@router.post("/customer/save", response_model=CustomerInput)
def save_customer_data(customer: CustomerInput, db: Session = Depends(get_db)):
    customer_data = pd.DataFrame([customer.dict()])

    # Calcular prediccion
    input_df = preprocessor.transform([customer.dict()])
    prob = model.predict_proba(input_df)[0][1]
    risk = "HIGH" if prob >= 0.7 else "MODERATED" if prob >= 0.4 else "LOW"
    customer_data["default_flag"] = round(prob, 2)
    customer_data["risk"] = risk

    saved_customer = save_customer(db, customer_data)
    return saved_customer