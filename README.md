# 🌍 Climate Emission Forecasting Dashboard

A machine learning-powered dashboard for forecasting zone-wise CO₂ emissions using weather, traffic, and industrial activity data — designed to assist in eco-friendly urban planning aligned with **SDG 13: Climate Action**.

---

## 📌 Project Overview

This project was developed during a hackathon challenge under **UN Sustainable Development Goal 13 (Climate Action)**. It uses AI to:

- **Forecast CO₂ emissions** for each city zone
- **Visualize emission levels** via interactive maps and time series plots
- **Recommend urban planning actions** to reduce emissions
- **Display forecasting accuracy** using key ML metrics

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** – Dashboard interface
- **XGBoost** – Emission forecasting model
- **scikit-learn** – Evaluation metrics
- **pandas / numpy** – Data wrangling
- **matplotlib / seaborn / folium** – Visualizations
- **joblib** – Model serialization

---

## 🔄 Project Structure
```

climate_emission_forecasting/
│
├── app/
│ └── main.py # Streamlit dashboard
│
├── data/
│ ├── raw/ # Uploaded CSVs
│ └── processed/ # Cleaned datasets
│
├── models/
│ └── model.pkl # Trained XGBoost model
│
├── assets/
│ └── emission_heatmap.html # HTML heatmap
│
├── src/
│ ├── data_pipeline.py # Data preprocessing
│ ├── model.py # Training + prediction + metrics
│ ├── planner.py # Planning recommendations
│ └── visualizer.py # Plotting & heatmaps
│
├── requirements.txt
└── README.md
```
## 📁 Input Format

Your CSV must contain the following columns:

| Column               | Type     | Description                              |
|----------------------|----------|------------------------------------------|
| `timestamp`          | datetime | Date and time of the observation         |
| `zone`               | string   | Name of the city zone                    |
| `traffic_volume`     | float    | Traffic density                          |
| `temperature`        | float    | Ambient temperature (°C)                 |
| `humidity`           | float    | Relative humidity (%)                    |
| `industrial_activity`| float    | Normalized index of industrial output    |
| `co2_emission`       | float    | Measured CO₂ emission (g/m³)             |

---

## 📊 Dashboard Features

- ✅ Upload your zone-wise dataset as CSV  
- 🔁 Automatic preprocessing and model training  
- 📈 Forecast zone-wise CO₂ emissions using XGBoost  
- 📊 View forecast accuracy metrics:
  - RMSE (Root Mean Squared Error)
  - MAE (Mean Absolute Error)
  - R² Score (Model Fit)
- 📉 Explore zone-wise time series CO₂ plots  
- 🗺️ Visualize heatmap of emissions across zones  
- 💡 Receive eco-friendly urban planning suggestions  
- 📥 Download prediction output as a CSV file  

---

## 📈 Forecast Accuracy Metrics

Displayed post-training:

| Metric | Description                 |
|--------|-----------------------------|
| RMSE   | Root Mean Squared Error     |
| MAE    | Mean Absolute Error         |
| R²     | Coefficient of Determination|

---

## 🧠 Model Overview

- Uses `XGBRegressor` trained on:
  - `traffic_volume`, `temperature`, `humidity`, `industrial_activity`
  - Encoded `zone`
  - Extracted `hour`, `dayofweek` from `timestamp`
- Model saved at: `models/model.pkl`
- Automatically retrained when new data is uploaded

---

## 🌱 SDG 13 Impact Statement

This dashboard equips planners with real-time environmental intelligence, enabling:
- Anticipation of high-emission zones  
- Data-driven policy creation to reduce urban emissions  
- Smart, sustainable city planning  

It directly supports **Sustainable Development Goal 13: Climate Action**, by empowering evidence-based, eco-conscious decision-making.

---

## 📦 Requirements

```bash
streamlit
xgboost
pandas
numpy
scikit-learn
matplotlib
seaborn
folium
joblib
```

Install via:

```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Mudit Gupta**  
GitHub: [github.com/your-username](https://github.com/your-username)  
LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

