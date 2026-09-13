import pandas as pd
import joblib


# Load trained model
MODEL_PATH = "models/student_performance_model.pkl"

model = joblib.load(MODEL_PATH)

print("Student Performance Predictor")
print("=" * 40)


# Student details
student = {
    "school": "GP",
    "sex": "M",
    "age": 18,
    "address": "U",
    "famsize": "GT3",
    "Pstatus": "T",
    "Medu": 3,
    "Fedu": 3,
    "Mjob": "services",
    "Fjob": "teacher",
    "reason": "course",
    "guardian": "mother",
    "traveltime": 1,
    "studytime": 3,
    "failures": 0,
    "schoolsup": "no",
    "famsup": "yes",
    "paid": "no",
    "activities": "yes",
    "nursery": "yes",
    "higher": "yes",
    "internet": "yes",
    "romantic": "no",
    "famrel": 4,
    "freetime": 3,
    "goout": 3,
    "Dalc": 1,
    "Walc": 1,
    "health": 4,
    "absences": 4,
    "G1": 14,
    "G2": 15
}


# Convert to DataFrame
student_df = pd.DataFrame([student])


# Make prediction
prediction = model.predict(student_df)[0]


print("\nPredicted Final Grade:")
print(f"{prediction:.2f} / 20")


# Performance category
if prediction >= 16:
    level = "Excellent"
elif prediction >= 12:
    level = "Good"
elif prediction >= 10:
    level = "Average"
else:
    level = "Needs Improvement"


print("Performance Level:", level)