
import joblib
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Load trained model
model = joblib.load("churnguard_logistic_model.joblib")

# Decision threshold
threshold = 0.45

# Customer input validation
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    tenure: Optional[float] = None
    PhoneService: str
    InternetService: Optional[str] = None
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: Optional[float] = None
    TotalCharges: Optional[float] = None

# Create API
app = FastAPI(
    title="ChurnGuard API",
    description="Telecom Customer Churn Prediction API",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "ChurnGuard API is running"}

@app.post("/predict")
def predict_churn(customer: CustomerData):

    customer_df = pd.DataFrame([customer.model_dump()])

    probability = model.predict_proba(customer_df)[0][
        list(model.classes_).index("yes")
    ]

    prediction = "yes" if probability >= threshold else "no"

    return {
        "churn_prediction": prediction,
        "churn_probability": round(float(probability), 4),
        "threshold": threshold
    }
