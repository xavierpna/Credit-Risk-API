from fastapi import APIRouter
from api.models import ClientInput, ClientOutput
from api.utils import upload_model
import numpy as np

router = APIRouter()

# Cargar modelo y preprocesador
model, preprocessor = upload_model()

@router.post("/predict", response_model=ClientOutput)
def default_predict(client: ClientInput):
    # Convertir entrada a Df
    data = client.dict()
    input_df = preprocessor.transform([data])

    # Realizar prediccion
    prob = model.predict_prob(input_df)[0][1]
    risk = "HIGH" if prob >= 0.7 else "MODERATED" if prob >= 0.4 else "LOW"

    return {
        "default_probability": round(prob, 2),
        "risk": risk
    }