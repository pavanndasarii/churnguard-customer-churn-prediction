import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Load model and threshold
saved = joblib.load("churnguard_logistic_model.joblib")
model = saved["model"]
threshold = saved["threshold"]

app = FastAPI(title="ChurnGuard API")


class CustomerData(BaseModel):
    SeniorCitizen: int
    tenure: float | None = None
    MonthlyCharges: float | None = None
    TotalCharges: float | None = None
    gender: str
    PhoneService: str
    InternetService: str | None = None
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str


@app.get("/")
def home():
    return {"message": "ChurnGuard API is running"}


@app.post("/predict")
def predict(data: CustomerData):
    customer = pd.DataFrame([data.model_dump()])

    yes_index = list(model.classes_).index("yes")
probability = float(model.predict_proba(customer)[0][yes_index])
    prediction = "yes" if probability >= threshold else "no"

    return {
        "churn_prediction": prediction,
        "churn_probability": round(probability, 4),
        "threshold": round(threshold, 4)
    }
