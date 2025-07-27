import joblib
import os
import pandas as pd
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

MODEL_PATH = "models/model.pkl"

def train_model(df):
    """Trains an XGBoost model and returns it along with training metrics."""
    features = ['traffic_volume', 'temperature', 'humidity', 'industrial_activity',
                'zone_encoded', 'hour', 'dayofweek']
    
    target = 'co2_emission'
    X = df[features]
    y = df[target]

    model = XGBRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved to model.pkl")

    # Training metrics
    y_pred = model.predict(X)
    metrics = {
        "RMSE": mean_squared_error(y, y_pred) ** 0.5,
        "MAE": mean_absolute_error(y, y_pred),
        "R2": r2_score(y, y_pred)
    }

    return model, metrics

def predict_emission(input_df):
    """Loads model and predicts emissions on input data."""
    model = joblib.load(MODEL_PATH)

    # Drop any non-numeric or unused columns
    drop_cols = ['timestamp', 'zone', 'co2_emission']
    for col in drop_cols:
        if col in input_df.columns:
            input_df = input_df.drop(columns=col)

    return model.predict(input_df)
