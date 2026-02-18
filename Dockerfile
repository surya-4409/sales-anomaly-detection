# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Expose the ports for API (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# 7. Default command (will be overridden by docker-compose)
CMD ["python", "app/main.py"]