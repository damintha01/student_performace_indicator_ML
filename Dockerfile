FROM python:3.10-bullseye

WORKDIR /app

# System dependencies for ML libs
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only required files first (layer caching)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Now copy app code
COPY . .

CMD ["python", "app.py"]
