FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema para geopy
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]