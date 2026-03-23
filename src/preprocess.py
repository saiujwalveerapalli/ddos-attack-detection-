import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def load_data(path):
    """Load CIC-IDS2018 network flow data."""
    df = pd.read_csv(path)
    return df

def preprocess(df):
    """Feature engineering and SMOTE for 15:1 class imbalance."""
    df = df.dropna()
    X = df.drop("Label", axis=1)
    y = df["Label"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X_scaled, y)
    return X_res, y_res
