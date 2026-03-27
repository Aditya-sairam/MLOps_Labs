from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
from datetime import datetime
from elasticsearch import Elasticsearch

# Load model and metadata
model_dir = os.path.join(os.path.dirname(__file__), '..', 'model')
model = joblib.load(os.path.join(model_dir, 'wine_model.pkl'))
feature_names = joblib.load(os.path.join(model_dir, 'feature_names.pkl'))
target_names = joblib.load(os.path.join(model_dir, 'target_names.pkl'))

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

app = FastAPI()

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
def health_check():
    return {"status": "healthy", "elasticsearch": es.ping()}

@app.post("/predict")
def predict(features: WineFeatures):
    try:
        # Prepare features
        feature_values = [[
            features.alcohol, features.malic_acid, features.ash,
            features.alcalinity_of_ash, features.magnesium, features.total_phenols,
            features.flavanoids, features.nonflavanoid_phenols, features.proanthocyanins,
            features.color_intensity, features.hue, features.od280_od315_of_diluted_wines,
            features.proline
        ]]
        
        # Make prediction
        prediction = model.predict(feature_values)[0]
        prediction_name = target_names[prediction]
        
        # Log to Elasticsearch
        log_data = {
            'timestamp': datetime.utcnow(),
            'prediction': int(prediction),
            'prediction_name': prediction_name,
            'features': features.dict()
        }
        
        es.index(index='wine-predictions', document=log_data)
        
        return {
            "prediction": int(prediction),
            "wine_class": prediction_name
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))