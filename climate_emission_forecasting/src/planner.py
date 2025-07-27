# src/planner.py

def generate_recommendations(row):
    recs = []

    if 'traffic_volume' in row and row['traffic_volume'] > 600:
        recs.append("Promote public transport")

    if 'industrial_activity' in row and row['industrial_activity'] > 0.7:
        recs.append("Introduce green regulations for industries")

    if 'temperature' in row and row['temperature'] > 35:
        recs.append("Encourage use of green rooftops")

    return ", ".join(recs) if recs else "No immediate action needed"
