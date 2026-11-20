# ChurnGuard – Telecom Customer Churn Prediction

![ChurnGuard CI](https://github.com/pavanndasarii/churnguard-customer-churn-prediction/actions/workflows/ci.yml/badge.svg)

ChurnGuard is a machine learning project that predicts whether a telecom customer is likely to leave the service. It uses customer information and service details to identify potential churn and support customer-retention decisions.

## Project Overview

- Cleaned and explored a telecom customer dataset.
- Built a machine learning pipeline using Scikit-learn.
- Compared Logistic Regression and Random Forest models.
- Applied hyperparameter tuning using GridSearchCV.
- Evaluated model performance using accuracy, precision, recall, and F1-score.
- Developed a REST API using FastAPI.
- Containerized the API using Docker.
- Added automated tests and GitHub Actions CI.

## Dataset

- Original records: 1,030
- Records after duplicate removal: 1,000
- Target variable: `Churn`
- Prediction classes: `yes` and `no`

The dataset contains customer information such as tenure, contract type, internet service, monthly charges, and total charges.

## Machine Learning Approach

**Data preprocessing**
- Removed duplicate records.
- Standardized inconsistent categorical values.
- Handled invalid and missing values.
- Split the data into training and testing sets using stratification.
- Used median imputation and scaling for numerical features.
- Used most-frequent imputation and one-hot encoding for categorical features.

**Model development**
- Logistic Regression
- Random Forest
- Cross-validation
- Hyperparameter tuning using GridSearchCV
- Churn probability threshold selection using training cross-validation predictions

## Model Performance

The tuned Logistic Regression model was selected based on cross-validation F1-score.

| Metric | Test Performance |
|---|---:|
| Accuracy | 69.50% |
| Precision (Churn = Yes) | 51.40% |
| Recall (Churn = Yes) | 85.94% |
| F1-score (Churn = Yes) | 64.33% |

The classification threshold was selected as 0.45 using out-of-fold predictions on the training data.

## API Development

Built a REST API using FastAPI to serve churn predictions.

**Available endpoints**

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/predict` | Predict customer churn |

Interactive API documentation is available at `/docs` when the application is running.

## Docker

The application is containerized using Docker.

Build the Docker image:

```bash
docker build -t churnguard-api .
```

Run the container:

```bash
docker run -p 8000:8000 churnguard-api
```

Open the API documentation:

```text
http://localhost:8000/docs
```

## Automated Testing and CI

- Used Pytest to test the API endpoints.
- Verified the prediction response and probability output.
- Configured GitHub Actions to automatically run tests on pushes and pull requests to the main branch.
- Latest CI workflow completed successfully.

## Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- FastAPI, Pydantic
- Joblib
- Docker
- Pytest
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
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Running Tests

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -q
```

## Future Improvements

- Deploy the API to a cloud platform.
- Add model monitoring and performance tracking.
- Explore additional machine learning models and optimization techniques.

---

**Author:** Dasari Pavan Kumar

[GitHub](https://github.com/pavanndasarii)
