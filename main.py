from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import uvicorn
import os
from src.make_dataset import data_preparation

# call the app
app = FastAPI(title="API",docs_url="/my-custom-docs")

# Load the model and scaler
def load_model():
    with open("models/best_model.pkl", "rb") as f1:
        return pickle.load(f1)

model = load_model()
# 0 = Windows , 1 = Macintosh, 2 = Linux
OS=["Windows","Macintosh","Linux"]

def predict_def(df, endpoint="simple"):
    #Prediction
    prediction=model.predict(df)
    value_predicted= prediction[0]   
    return {"label":OS[value_predicted],"prediction":value_predicted}


class Usuario(BaseModel):
    duracion: int
    paginas: int
    acciones: int
    valor: int
    hora_dia: str
    pais: str
    edad: float
    experiencia: str
    navegador: str
    nivel_usuario: float


# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction:int

    # Endpoints


# Root Endpoint
@app.get("/")
def root():
    return {"API": "Este es un modelo para predecir Default."}


# Prediction endpoint
@app.post("/predict", response_model=Output)
def predict_default(subject: Usuario):
    # Make prediction
    data = pd.DataFrame(subject.dict(), index=[0])
    datan = data_preparation(data,1)
    #print(datan)
    parsed = predict_def(df=datan)
    return parsed


# App Health
@app.get('/health')
async def service_health():
    """Return service health"""
    return {"ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)