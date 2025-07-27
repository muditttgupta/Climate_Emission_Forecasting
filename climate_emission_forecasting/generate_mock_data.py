import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_samples = 500

timestamps = [datetime(2024, 1, 1) + timedelta(hours=i) for i in range(n_samples)]
zones = np.random.choice(['Zone A', 'Zone B', 'Zone C'], n_samples)
traffic_volume = np.random.randint(50, 500, n_samples)
temperature = np.random.uniform(15, 35, n_samples)
humidity = np.random.uniform(30, 90, n_samples)
industrial_activity = np.random.uniform(0.2, 1.0, n_samples)
co2_emission = (
    0.3 * traffic_volume +
    0.4 * temperature +
    0.2 * humidity +
    100 * industrial_activity +
    np.random.normal(0, 10, n_samples)
)

df = pd.DataFrame({
    'timestamp': timestamps,
    'zone': zones,
    'traffic_volume': traffic_volume,
    'temperature': temperature,
    'humidity': humidity,
    'industrial_activity': industrial_activity,
    'co2_emission': co2_emission
})

df.to_csv('data/raw/mock_emission_data.csv', index=False)
print("✅ Mock dataset saved as mock_emission_data.csv")
