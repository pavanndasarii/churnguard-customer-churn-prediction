# ChurnGuard – Telecom Customer Churn Prediction

![ChurnGuard CI](https://github.com/pavanndasarii/churnguard-customer-churn-prediction/actions/workflows/ci.yml/badge.svg)

ChurnGuard is a machine learning project that predicts whether a telecom customer is likely to leave a service. It helps identify potential churn customers using their account and service information.

## Project Overview

- Cleaned and explored telecom customer data.
- Built machine learning pipelines using Scikit-learn.
- Compared Logistic Regression and Random Forest.
- Performed hyperparameter tuning using GridSearchCV.
- Optimized the churn prediction threshold using cross-validation predictions.
- Developed a REST API using FastAPI.
- Containerized the application using Docker.
- Added automated API tests and GitHub Actions CI.

## Dataset

- Original records: 1,030
- Records after duplicate removal: 1,000
- Target variable: `Churn`
- Prediction classes: `yes` and `no`

The dataset includes customer tenure, contract type, internet service, monthly charges, total charges, and other service details.

## Machine Learning Approach

### Data preprocessing
- Removed duplicate records.
- Standardized inconsistent categorical values.
- Handled invalid and missing values.
- Used stratified train-test splitting.
- Applied median imputation and scaling to numerical features.
- Applied most-frequent imputation and one-hot encoding to categorical features.

### Model development and optimization
- Logistic Regression
- Random Forest
- Cross-validation
- GridSearchCV for hyperparameter tuning
- Churn probability threshold optimization using out-of-fold training predictions

The tuned Logistic Regression model was selected based on cross-validation F1-score.

## Model Performance

Final evaluation on the held-out test set:

| Metric | Result |
|---|---:|
| Accuracy | 69.50% |
| Churn Precision | 51.40% |
| Churn Recall | 85.94% |
| Churn F1-score | 64.33% |
| Optimized threshold | 0.4448 |

The threshold was selected using out-of-fold predictions on the training data.

## API Development

Built a REST API using FastAPI to serve predictions from the trained model.

### Available endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/predict` | Predict customer churn |

Interactive API documentation is available at `/docs`.

### Sample prediction request

```json
{
  "SeniorCitizen": 0,
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "TotalCharges": 850.0,
  "gender": "female",
  "PhoneService": "yes",
  "InternetService": "fiber optic",
  "Contract": "month-to-month",
  "PaperlessBilling": "yes",
  "PaymentMethod": "electronic check"
}
```

### Sample prediction response

```json
{
  "churn_prediction": "yes",
  "churn_probability": 0.6488,
  "threshold": 0.4448
}
```

The API returns the predicted churn class, churn probability, and decision threshold.

## Docker

The application has been built and tested locally inside a Docker container.

### Build the Docker image

```bash
docker build -t churnguard-api .
```

### Run the container

```bash
docker run --rm -p 8000:8000 churnguard-api
```

### Open API documentation

```text
http://localhost:8000/docs
```

The `/predict` endpoint was tested successfully through the Dockerized API and returned HTTP 200.

## Automated Testing and CI

- Used Pytest for automated API testing.
- Tested API status and prediction endpoints.
- Used GitHub Actions to run tests automatically on repository pushes.
- Successfully verified the CI workflow.

Run tests locally:

```bash
pip install -r requirements.txt
pytest -q
```

## Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- FastAPI, Pydantic
- Joblib
- Docker
- Pytest, HTTPX
- Git, GitHub
- GitHub Actions
- Google Colab

## Project Structure

```text
ChurnGuard/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_api.py
├── ChurnGuard (1).ipynb
├── churnguard_data.csv
├── churnguard_logistic_model.joblib
├── model_metrics.json
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Future Improvements

- Deploy the API to a cloud platform.
- Add model monitoring and performance tracking.
- Explore additional machine learning models.

---

**Author:** Dasari Pavan Kumar

[GitHub](https://github.com/pavanndasarii)
