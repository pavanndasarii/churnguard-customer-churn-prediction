from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "ChurnGuard API is running"


def test_predict():
    sample_customer = {
        "gender": "Male",
        "SeniorCitizen": 0,
        "tenure": 24,
        "PhoneService": "Yes",
        "InternetService": "Fiber optic",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 75.50,
        "TotalCharges": 1800.00
    }

    response = client.post("/predict", json=sample_customer)

    assert response.status_code == 200
    assert response.json()["churn_prediction"] in ["yes", "no"]
    assert 0 <= response.json()["churn_probability"] <= 1
