from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib


app = FastAPI(
    title="AI Student Performance Predictor",
    description="Predict student final academic performance using Machine Learning",
    version="1.0"
)


# Load trained ML model
model = joblib.load(
    "../models/student_performance_model.pkl"
)


class StudentData(BaseModel):
    school: str
    sex: str
    age: int
    address: str
    famsize: str
    Pstatus: str
    Medu: int
    Fedu: int
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    traveltime: int
    studytime: int
    failures: int
    schoolsup: str
    famsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    G1: int
    G2: int


@app.get("/")
def home():
    return {
        "message": "AI Student Performance Predictor API",
        "status": "running"
    }


@app.post("/predict")
def predict(student: StudentData):

    student_dict = student.model_dump()

    student_df = pd.DataFrame([student_dict])

    prediction = model.predict(student_df)[0]

    if prediction >= 16:
        performance = "Excellent"
        risk = "Low"
    elif prediction >= 12:
        performance = "Good"
        risk = "Low"
    elif prediction >= 10:
        performance = "Average"
        risk = "Medium"
    else:
        performance = "Needs Improvement"
        risk = "High"

    return {
        "predicted_grade": round(float(prediction), 2),
        "max_grade": 20,
        "performance": performance,
        "risk_level": risk
    }