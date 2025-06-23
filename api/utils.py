import joblib

def upload_model():
    model = joblib.load("model/predictor.pkl")
    preprocessor = joblib.load("model/preprocessor.pkl")
    return model, preprocessor