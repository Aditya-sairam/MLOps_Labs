from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Model service URL (docker-compose service name)
MODEL_SERVICE_URL = "http://model-service:5000"

class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

@app.get("/")
def health():
    return {"status": "API Service is running"}

@app.post("/predict")
def predict(wine: WineFeatures):
    try:
        # Convert to list of features
        features = [
            wine.alcohol, wine.malic_acid, wine.ash, wine.alcalinity_of_ash,
            wine.magnesium, wine.total_phenols, wine.flavanoids,
            wine.nonflavanoid_phenols, wine.proanthocyanins,
            wine.color_intensity, wine.hue, wine.od280_od315_of_diluted_wines,
            wine.proline
        ]
        
        # Call model service
        response = requests.post(
            f"{MODEL_SERVICE_URL}/predict",
            json={"features": features}
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=500, detail="Model service error")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))