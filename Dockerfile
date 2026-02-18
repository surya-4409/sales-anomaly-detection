# 1. Base Image
FROM python:3.9-slim

# 2. Set Working Directory
WORKDIR /app

# --- CRITICAL FIX: Install curl for Healthcheck ---
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 3. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Code
COPY . .

# 5. Expose Ports (API & UI)
EXPOSE 8000
EXPOSE 8501

# 6. Run Command (Start API in background, then Streamlit)
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run app/ui.py --server.port 8501 --server.address 0.0.0.0