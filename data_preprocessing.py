import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

def preprocessing_data(file_path):
    df = pd.read_csv(file_path)

    # Ensure 'Churn' column exists (case-insensitive)
    churn_cols = [col for col in df.columns if col.lower() == "churn"]
    if not churn_cols:
        raise ValueError("No 'Churn' column found in the dataset.")
    churn_col = churn_cols[0]
    df[churn_col] = df[churn_col].astype(str).str.lower()

    # Drop unnecessary columns if present
    for col in ["customerID", "Unamed= 0"]:
        if col in df.columns:
            df.drop(columns=col, inplace=True)

    # Handle missing values
    if df.isnull().values.any():
        print("⚠️ Missing values detected!")
        print(df.isnull().sum())
        print("\n🧼 Please clean the dataset before proceeding.")
        raise ValueError("Pipeline stopped due to missing data.")

    # Encode categorical features (excluding churn label)
    categorical_cols = [col for col in df.columns if df[col].dtype == 'object' and col != churn_col]
    encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Extract features and label
    X = df.drop(columns=[churn_col])
    y = df[churn_col].map({'no': 0, 'yes': 1})  # ✅ MAP churn to 0/1

    # Scale numeric features
    numeric_cols = X.select_dtypes(include='number').columns
    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    return X, y, encoders, scaler, churn_col

def save_preprocessing_objects(encoders, scaler, path='encoder_scaler.pkl'):
    joblib.dump({'encoders': encoders, 'scaler': scaler}, path)

def load_preprocessing_objects(path='encoder_scaler.pkl'):
    return joblib.load(path)