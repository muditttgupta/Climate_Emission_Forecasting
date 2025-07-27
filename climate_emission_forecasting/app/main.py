# Streamlit frontend for interactive dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_pipeline import load_data, preprocess_data
from src.model import train_model, predict_emission
from src.planner import generate_recommendations
from src.visualizer import generate_emission_heatmap

st.set_page_config(layout="wide")
st.title("🌍 Climate Emission Forecasting Dashboard")

uploaded = st.file_uploader("Upload zone-wise data (CSV)", type="csv")

if uploaded:
    df = pd.read_csv(uploaded, parse_dates=['timestamp'])
    st.write("### Raw Data", df.head())

    df = preprocess_data(df)

    # Model training + metrics
    model, metrics = train_model(df)

    preds = predict_emission(df.drop(columns=['co2_emission']))
    df['predicted_emission'] = preds
    df['recommendations'] = df.apply(generate_recommendations, axis=1)

    st.write("### Forecast Results", df[['timestamp', 'zone', 'predicted_emission', 'recommendations']].head())

    # 🔍 Show accuracy metrics
    st.subheader("📊 Model Forecast Accuracy")
    st.metric("RMSE", f"{metrics['RMSE']:.2f}")
    st.metric("MAE", f"{metrics['MAE']:.2f}")
    st.metric("R² Score", f"{metrics['R2']:.2f}")

    # 📈 Zone-wise CO₂ time series graph
    st.subheader("⏱️ Zone-wise CO₂ Emission Over Time")
    zones = df['zone'].unique()
    selected_zone = st.selectbox("Select Zone", zones)
    zone_df = df[df['zone'] == selected_zone]

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=zone_df, x='timestamp', y='predicted_emission', marker='o', label='Predicted CO₂', ax=ax)
    ax.set_title(f"Predicted CO₂ Emissions - {selected_zone}")
    ax.set_ylabel("CO₂ Emissions")
    ax.set_xlabel("Timestamp")
    ax.grid(True)
    st.pyplot(fig)

    # 🌍 Heatmap
    generate_emission_heatmap(df)
    st.components.v1.html(open("assets/emission_heatmap.html", 'r').read(), height=500)

    # 📥 Download
    st.download_button("Download Forecast CSV", df.to_csv(index=False), file_name="forecast_output.csv")
