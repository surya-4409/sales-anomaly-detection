import pytest
import pandas as pd
import numpy as np
from app.analysis import detect_anomalies

def test_detect_anomalies_logic():
    # 1. Create fake data (constant revenue = 100)
    dates = pd.date_range(start="2024-01-01", periods=50)
    df = pd.DataFrame({
        "date": dates,
        "revenue": [100] * 50
    })
    
    # 2. Run logic
    result = detect_anomalies(df)
    
    # 3. Check: Should be NO anomalies
    assert result['is_anomaly'].sum() == 0
    
def test_detect_obvious_anomaly():
    # 1. Create data with ONE massive spike
    dates = pd.date_range(start="2024-01-01", periods=50)
    revenues = [100] * 50
    revenues[40] = 10000  # Huge spike at index 40
    
    df = pd.DataFrame({
        "date": dates,
        "revenue": revenues
    })
    
    # 2. Run logic
    result = detect_anomalies(df)
    
    # 3. Check: Index 40 MUST be an anomaly
    assert result.iloc[40]['is_anomaly'] == True
