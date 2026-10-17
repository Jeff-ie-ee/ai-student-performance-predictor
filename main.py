
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="AI Student Performance Predictor API",
    description="Machine Learning API for predicting student performance",
    version="1.0.0"
)

# ============================================================
# MODEL PATH
# ============================================================

# Root project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model saved inside the backend folder
MODEL_PATH = os.path.join(
    BASE_DIR,
    "backend",
    "student_performance_pipeline.pkl"
)

# ============================================================
# LOAD MODEL
# ============================================================

model = None

try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully!")
    print("Model path:", MODEL_PATH)

except Exception as e:
    print("ERROR loading model:")
    print(e)

# ============================================================
# REQUEST SCHEMA
# ============================================================

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

# ============================================================
# HOME ENDPOINT
# ============================================================

@app.get("/")
def home():
    return {
        "message": "AI Student Performance Predictor API",
        "status": "running",
        "model_loaded": model is not None
    }

# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

# ============================================================
# PREDICTION ENDPOINT
# ============================================================

@app.post("/predict")
def predict_student_performance(student: StudentData):

    if model is None:
        return {
            "error": "Model is not loaded. Check MODEL_PATH."
        }

    try:
        # Convert input into a DataFrame
        input_data = pd.DataFrame(
            [student.model_dump()]
        )

        # Generate prediction
        prediction = model.predict(input_data)[0]

        # Keep the predicted grade within the expected range
        predicted_grade = float(max(0, min(20, prediction)))

        # Determine performance category
        if predicted_grade >= 15:
            performance = "Excellent"
        elif predicted_grade >= 12:
            performance = "Good"
        elif predicted_grade >= 10:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        # Determine risk level
        if predicted_grade < 8:
            risk_level = "High"
        elif predicted_grade < 12:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return {
            "predicted_grade": round(predicted_grade, 2),
            "performance": performance,
            "risk_level": risk_level
        }

    except Exception as e:
        return {
            "error": str(e)
        }
