from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from predict import predict_species

app = FastAPI()

class PenguinData(BaseModel):
    sex: int
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

class PredictionResponse(BaseModel):
    species: str

@app.get("/",status_code=status.HTTP_200_OK)
async def health_ping():
    return {"status":"healthy"}

@app.post("/predict",response_model=PredictionResponse,status_code=status.HTTP_200_OK)
async def predict(penguin: PenguinData):
    try:
        penguin_features = [penguin.bill_depth_mm,penguin.bill_length_mm,
                            penguin.flipper_length_mm,penguin.body_mass_g,penguin.sex]
        prediction = predict_species([penguin_features])
        return PredictionResponse(species=prediction[0])
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Model loading failed: {e}")
