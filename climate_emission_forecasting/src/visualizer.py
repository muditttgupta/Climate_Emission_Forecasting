# Code for visualizing emissions and planning outputs
import folium
from folium.plugins import HeatMap
import pandas as pd

def generate_emission_heatmap(df, city_center=(28.6139, 77.2090)):
    # Create a dummy lat/lon mapping per zone
    zone_coords = {
        "Zone A": (28.6139, 77.2090),
        "Zone B": (28.62, 77.22),
        "Zone C": (28.6, 77.25),
        "Zone D": (28.63, 77.2),
        "Zone E": (28.61, 77.215),
    }

    map_df = df.groupby('zone')['co2_emission'].mean().reset_index()
    m = folium.Map(location=city_center, zoom_start=12)

    heat_data = []
    for _, row in map_df.iterrows():
        lat, lon = zone_coords.get(row['zone'], city_center)
        heat_data.append([lat, lon, row['co2_emission']])

    HeatMap(heat_data).add_to(m)
    m.save("assets/emission_heatmap.html")
    print("✅ Heatmap saved to assets/emission_heatmap.html")
