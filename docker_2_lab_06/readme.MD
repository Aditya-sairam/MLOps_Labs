# Docker Compose Wine Prediction Lab

A multi-container application with separate Model Service and API Service for wine quality prediction.

## Folder Structure

```bash
docker_2_lab_06/
├── model-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── api-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── model/
│   ├── wine_model.pkl
│   └── target_names.pkl
├── train_model.py
├── docker-compose.yml
└── README.md
```

## Architecture

- **Model Service** (Port 5000): Flask service that loads the ML model and makes predictions
- **API Service** (Port 8000): FastAPI gateway that validates requests and calls model service
- Communication: API Service → Model Service (internal network)

## How to Run

### 1. Train the Model

```bash
python train_model.py
```

This creates `model/wine_model.pkl` and `model/target_names.pkl`.

### 2. Build and Start Services

```bash
docker-compose build
docker-compose up
```

Wait for both services to start (check logs for "Running on...").

### 3. Test the Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "alcohol": 13.2,
    "malic_acid": 2.5,
    "ash": 2.4,
    "alcalinity_of_ash": 20.0,
    "magnesium": 100.0,
    "total_phenols": 2.8,
    "flavanoids": 2.9,
    "nonflavanoid_phenols": 0.3,
    "proanthocyanins": 1.8,
    "color_intensity": 5.5,
    "hue": 1.0,
    "od280_od315_of_diluted_wines": 3.0,
    "proline": 1000.0
  }'
```

### 4. Check Health

```bash
# API Service
curl http://localhost:8000/

# Model Service
curl http://localhost:5000/health
```

## Stop Services

```bash
docker-compose down
```

## What This Demonstrates

- Multi-container orchestration with docker-compose
- Microservices architecture (API gateway + Model service)
- Container networking and communication
- Volume mounting for shared model files
- Service dependencies with `depends_on`