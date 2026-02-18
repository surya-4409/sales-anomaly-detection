
# 🕵️‍♀️ Sales Anomaly Detection System

A containerized full-stack application that detects sales anomalies using statistical analysis (Z-Score) and provides AI-powered explanations.

## 🚀 Overview
This project identifies unusual sales patterns in time-series data. It features a decoupled architecture with a **FastAPI backend** for logic and a **Streamlit frontend** for visualization, all orchestrated via **Docker**.

### Key Features
* **Automated Anomaly Detection:** Uses a 30-day rolling Z-Score (threshold ±2.5) to identify outliers.
* **Interactive Visualization:** Plots sales trends and highlights anomalies using Plotly.
* **AI Integration:** Connects to LLMs (Claude or local Ollama) to generate explanations for detected anomalies.
* **Robust Architecture:** Fully Dockerized with a health-checked API and decoupled UI.
* **Error Handling:** Gracefully handles API failures and missing data.

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Data Processing:** Pandas, NumPy
* **Visualization:** Plotly
* **Containerization:** Docker, Docker Compose
* **Testing:** Pytest

---

## 🏃‍♂️ How to Run

### Prerequisites
* Docker & Docker Compose installed on your machine.

### Quick Start
1.  **Clone/Unzip** the project folder.
2.  **Build and Run** the application:
    ```bash
    docker-compose up --build
    ```
3.  **Access the App:**
    * **Frontend (Streamlit):** [http://localhost:8501](http://localhost:8501)
    * **Backend Docs (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)

4.  **Test with Data:**
    * Upload the provided `data/sales_history.csv` file in the UI to see the analysis.

---

## 🧪 How to Test (Grading)

### 1. Run Unit Tests
To verify the statistical logic and API endpoints, run the test suite inside the container:
```bash
docker-compose exec app pytest tests/

```

*Expected Output: `2 passed*`

### 2. Verify Accuracy (Golden Dataset)

To evaluate the anomaly detection accuracy against the "Golden Truth" dataset:

```bash
python evaluate.py

```

*Expected Output: `🏆 Final Score: 100.0%*`

---

## ⚙️ Configuration (Optional)

The application uses a `.env` file for configuration.

* **ANTHROPIC_API_KEY:** (Optional) Key for Claude AI explanations.
* **OLLAMA_BASE_URL:** (Default: `http://host.docker.internal:11434`) URL for local LLM.

*Note: If no LLM is available, the UI will display a connection error message in the explanation box. This is expected behavior and demonstrates error handling.*

---

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py          # FastAPI Backend Entrypoint
│   ├── ui.py            # Streamlit Frontend
│   ├── analysis.py      # Z-Score Logic & LLM Integration
│   └── plotting.py      # Plotly Visualization Logic
├── data/
│   ├── sales_history.csv       # Test Data
│   └── golden_anomalies.json   # Ground Truth for Grading
├── tests/
│   └── test_analysis.py # Unit Tests
├── docker-compose.yml   # Service Orchestration
├── Dockerfile           # Container Definition
└── requirements.txt     # Python Dependencies

```

```

---

## 👨‍💻 Author
**Billakurti Venkata Suryanarayana (Surya)**
* **Roll Number:** 23MH1A4409
* **Project:** Sales Anomaly Detection System (FastAPI + Streamlit + Docker)