from fastapi import FastAPI, HTTPException
from app.schemas import DiseaseInput
from app.model import model

app = FastAPI(
    title="Disease Prediction API",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "Disease Prediction API", "status": "running"}

@app.post("/predict")
def predict_disease(data: DiseaseInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model failed to load")
    
    input_data = [[
        data.age,
        data.blood_pressure,
        data.cholesterol,
        data.glucose,
        data.bmi,
        data.heart_rate
    ]]
    
    try:
        prediction = model.predict(input_data)[0]
        return {
            "prediction": int(prediction),
            "message": "Disease detected" if prediction == 1 else "No disease detected"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
