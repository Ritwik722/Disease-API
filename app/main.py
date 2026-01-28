from fastapi import FastAPI
from app.schemas import DiseaseInput
from app.model import model

app = FastAPI()

# REQUIRED BY SAGEMAKER
@app.get("/ping")
def ping():
    return {"status": "healthy"}

# REQUIRED BY SAGEMAKER
@app.post("/invocations")
def invocations(data: DiseaseInput):
    input_data = [[
        data.age,
        data.blood_pressure,
        data.cholesterol,
        data.glucose,
        data.bmi,
        data.heart_rate
    ]]
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}

# Optional (for local testing)
@app.post("/predict")
def predict(data: DiseaseInput):
    input_data = [[
        data.age,
        data.blood_pressure,
        data.cholesterol,
        data.glucose,
        data.bmi,
        data.heart_rate
    ]]
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
