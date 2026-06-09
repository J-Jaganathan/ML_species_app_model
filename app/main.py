from fastapi import FastAPI
from pydantic import BaseModel
from app.predictor import predict

from typing import Literal

class PenguinInput(BaseModel):
    island: Literal["Biscoe", "Dream", "Torgersen"]
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    sex: Literal["male", "female"]

app = FastAPI()

@app.post("/predict")
def predict_species(data: PenguinInput):

    input_dict = data.model_dump()

    result = predict(input_dict)

    return {
        "prediction": result
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }