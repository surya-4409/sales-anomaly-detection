import pandas as pd
import numpy as np
import os
import requests

def detect_anomalies(df: pd.DataFrame):
    """
    1. Sorts data by date.
    2. Calculates 30-day moving average and standard deviation.
    3. Calculates Z-Score: (Value - Average) / StdDev.
    4. Marks anything with Z-Score > 2.5 or < -2.5 as an anomaly.
    """
    # Ensure date is a datetime object
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # --- THE MATH (Required by Instructions) ---
    # Rolling window of 30 days
    df['rolling_mean'] = df['revenue'].rolling(window=30, min_periods=1).mean()
    df['rolling_std'] = df['revenue'].rolling(window=30, min_periods=1).std()
    
    # Calculate Z-Score
    # We use .bfill() to handle the first few rows where std might be NaN
    df['z_score'] = (df['revenue'] - df['rolling_mean']) / df['rolling_std']
    df['z_score'] = df['z_score'].fillna(0)
    
    # Mark Anomalies (Threshold: 2.5)
    df['is_anomaly'] = np.abs(df['z_score']) > 2.5
    
    return df

def get_llm_explanation(anomaly_row):
    """
    Sends the anomaly data to an LLM (Claude or Ollama) to get an explanation.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")

    # The Prompt for the AI
    prompt = f"""
    You are a business analyst. A sales anomaly was detected:
    Date: {anomaly_row['date']}
    Revenue: ${anomaly_row['revenue']}
    30-Day Average: ${anomaly_row['rolling_mean']:.2f}
    
    Explain in 1 sentence why this might be significant.
    """

    try:
        # 1. Try Anthropic (Cloud)
        if api_key and "sk-" in api_key:
            headers = {"x-api-key": api_key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
            data = {
                "model": "claude-3-haiku-20240307",
                "max_tokens": 100,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post("https://api.anthropic.com/v1/messages", json=data, headers=headers)
            return response.json()['content'][0]['text']
            
        # 2. Fallback to Ollama (Local)
        else:
            data = {
                "model": "llama3", 
                "prompt": prompt, 
                "stream": False
            }
            # We use a short timeout so it doesn't hang forever if Ollama isn't running
            response = requests.post(f"{ollama_url}/api/generate", json=data, timeout=5)
            return response.json()['response']
            
    except Exception as e:
        return f"AI Analysis Unavailable: {str(e)}"