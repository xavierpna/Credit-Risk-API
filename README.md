# Project: Customer Default Prediction via Multisource Smart API

---

## 🧱 Architecture

Based on a modular architecture with the main components:

- **Data Ingestion:** loading from files and databases.
- **Preprocessing:** automatic handling of missing data and encoding.
- **ML Model:** RandomForest trained with SMOTE balancing.
- **REST API:** service developed with FastAPI for querying and prediction.
- **Storage:** saving model and preprocessor in `.pkl` files.

---

## 📁 Project Structure

```bash
predictor_default/
│
├── api/
│   ├── main.py           # FastAPI API
│   ├── routes.py         # API Endpoints
│   ├── models.py         # Pydantic models for validation
│   └── utils.py          # Auxiliary functions
│
├── data/
│   └── sample.xlsx       # Initial dataset
│
├── model/
│   ├── train_model.py    # Training script
│   ├── predictor.pkl     # Trained model (serialized)
│   └── preprocessor.pkl  # Serialized preprocessor
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Requirements

- Python 3.8+
- Packages listed in requirements.txt (install with pip install -r requirements.txt)
- Initial dataset in Datasets/sample.xlsx

---

### Train Model

```bash
python train_model.py
```

This generates the files: 

- `model/predictor.pkl`
- `model/preprocessor.pkl`

--- 

## 📁 Project Structure

```bash
predictor_default/
│
├── api/
│   ├── main.py           # API FastAPI
│   ├── routes.py         # Endpoints de la API
│   ├── models.py         # Modelos Pydantic para validación
│   └── utils.py          # Funciones auxiliares
│
├── data/
│   └── sample.xlsx       # Dataset inicial
│
├── model/
│   ├── train_model.py    # Script de entrenamiento
│   ├── predictor.pkl     # Modelo entrenado (serializado)
│   └── preprocessor.pkl  # Preprocesador serializado
│
├── tests/
│   └── test_api.py       # Tests (por implementar)
│
├── requirements.txt
└── README.md
```
