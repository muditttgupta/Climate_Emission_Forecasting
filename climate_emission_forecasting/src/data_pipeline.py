import pandas as pd
import numpy as np
import os

RAW_DATA_PATH = "data/raw/mock_emission_data.csv"
PROCESSED_DATA_PATH = "data/processed/processed_emission_data.csv"

def load_data(path=RAW_DATA_PATH):
    """Loads raw emission data from CSV."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Raw data file not found at: {path}")
    return pd.read_csv(path)

def preprocess_data(df):
    """Preprocesses the raw data for modeling."""
    df = df.copy()

    # Encode zone
    if 'zone' in df.columns:
        df['zone_encoded'] = df['zone'].astype('category').cat.codes
    else:
        raise ValueError("Missing 'zone' column in dataset.")

    # Convert timestamp and extract features
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df['hour'] = df['timestamp'].dt.hour.fillna(np.random.randint(0, 24))
        df['dayofweek'] = df['timestamp'].dt.dayofweek.fillna(np.random.randint(0, 7))
    else:
        df['hour'] = np.random.randint(0, 24, size=len(df))
        df['dayofweek'] = np.random.randint(0, 7, size=len(df))

    # Drop rows with missing emissions
    if 'co2_emission' in df.columns:
        df = df.dropna(subset=['co2_emission'])
    else:
        raise ValueError("Missing 'co2_emission' column in dataset.")

    # Save processed data
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)

    return df
