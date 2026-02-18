import plotly.graph_objects as go
import pandas as pd
import json

def create_plot(df):
    """
    Generates a Plotly chart with:
    1. Blue Line: Revenue over time.
    2. Red Dots: Detected anomalies.
    """
    # 1. The Main Line (Sales)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['date'], 
        y=df['revenue'],
        mode='lines',
        name='Revenue',
        line=dict(color='blue')
    ))

    # 2. The Anomalies (Red Dots)
    anomalies = df[df['is_anomaly']]
    if not anomalies.empty:
        fig.add_trace(go.Scatter(
            x=anomalies['date'],
            y=anomalies['revenue'],
            mode='markers',
            name='Anomaly',
            marker=dict(color='red', size=10, symbol='x')
        ))

    fig.update_layout(
        title="Sales Anomaly Detection",
        xaxis_title="Date",
        yaxis_title="Revenue ($)",
        template="plotly_white"
    )

    # Convert to JSON so the API can send it
    return json.loads(fig.to_json())