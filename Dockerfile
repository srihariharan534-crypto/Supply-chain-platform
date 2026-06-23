FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Run the API by default, or modify for Streamlit
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
