import requests
import json

# 1. Setup
API_URL = "http://localhost:8000/analyze"
GOLDEN_FILE = "data/golden_anomalies.json"
DATA_FILE = "data/sales_history.csv"

def evaluate():
    print(f"📡 Connecting to API at {API_URL}...")
    
    try:
        # 2. Send the Data to the API
        with open(DATA_FILE, 'rb') as f:
            files = {'file': f}
            response = requests.post(API_URL, files=files)
            
        if response.status_code != 200:
            print(f"❌ API Error: {response.text}")
            return

        data = response.json()
        
        # 3. Extract Detected Anomalies
        chart_data = data['chart']['data']
        # Trace 1 contains the red 'markers' (anomalies)
        if len(chart_data) < 2: 
             print("❌ Error: No anomalies detected in chart.")
             return

        detected_dates = chart_data[1]['x'] 
        detected_dates = [d.split("T")[0] for d in detected_dates]
        
        print(f"✅ API found {len(detected_dates)} anomalies.")

        # 4. Compare with Golden Truth
        with open(GOLDEN_FILE, 'r') as f:
            golden = json.load(f)
            
        golden_dates = [item['date'] for item in golden['anomalies']]
        
        matches = 0
        for g_date in golden_dates:
            if g_date in detected_dates:
                matches += 1
                print(f"  ✅ Found Golden Anomaly: {g_date}")
            else:
                print(f"  ❌ Missed Golden Anomaly: {g_date}")
                
        # 5. Final Score
        score = matches / len(golden_dates)
        print(f"\n🏆 Final Score: {score*100:.1f}%")
        
        if score >= 0.8:
            print("🎉 PASSED! (Requirement > 80%)")
        else:
            print("⚠️ FAILED. Check Z-Score logic.")

    except Exception as e:
        print(f"❌ Evaluation Failed: {e}")

if __name__ == "__main__":
    evaluate()