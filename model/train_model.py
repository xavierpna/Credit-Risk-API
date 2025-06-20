import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE

# ----------------------------
# CONFIGURACIÓN GENERAL
# ----------------------------

DATA_PATH = Path("data/sample.xlsx")
MODEL_PATH = Path("model/predictor.pkl")
PREPROCESSOR_PATH = Path("model/preprocessor.pkl")


# ----------------------------
# FUNCIONES
# ----------------------------

def load_data(path: Path) -> pd.DataFrame:
    return pd.read_excel(path)


def preprocess_features(X: pd.DataFrame):
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object', 'category']).columns.tolist()

    numeric_transformer = SimpleImputer(strategy='median')
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, num_cols),
        ('cat', categorical_transformer, cat_cols)
    ])

    return preprocessor


def train_model(df: pd.DataFrame,
                model_path: Path,
                preprocessor_path: Path):
    # Separar variables
    X = df.drop(columns=['default_flag'])
    y = df['default_flag']

    # Preprocesar
    preprocessor = preprocess_features(X)
    X_processed = preprocessor.fit_transform(X)

    # Balancear clases
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_processed, y)

    # Dividir dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, test_size=0.3, random_state=42)

    # Entrenar modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluación
    y_pred = model.predict(X_test)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("Confussion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Guardar modelo y preprocesador
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    joblib.dump(preprocessor, preprocessor_path)

    print(f"\nModel saved in: {model_path}")
    print(f"Preprocessor saved in: {preprocessor_path}")


# ----------------------------
# EJECUCIÓN DIRECTA
# ----------------------------

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    train_model(df, MODEL_PATH, PREPROCESSOR_PATH)
