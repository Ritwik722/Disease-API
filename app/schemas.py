from pydantic import BaseModel

class DiseaseInput(BaseModel):
    age: int
    blood_pressure: int
    cholesterol: int
    glucose: int
    bmi: float
    heart_rate: int
