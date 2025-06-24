from fastapi import APIRouter
from api.models import CustomerInput, CustomerOutput
from api.utils import upload_model
import numpy as np
import pandas as pd

router = APIRouter()

# Cargar modelo y preprocesador
model, preprocessor = upload_model()

@router.post("/predict", response_model=CustomerOutput)
def default_predict(client: CustomerInput):
    # Convertir entrada a Df
    data = pd.DataFrame([client.dict()])

    # Preprocesar
    input_df = preprocessor.transform(data)

    # Realizar prediccion
    prob = model.predict_proba(input_df)[0][1]
    risk = "HIGH" if prob >= 0.7 else "MODERATED" if prob >= 0.4 else "LOW"

    return {
        "default_probability": round(prob, 2),
        "risk": risk
    }