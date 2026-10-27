# churnguard-customer-churn-prediction
Telecom customer churn analysis and prediction using Python and machine learning.
# ChurnGuard — Customer Churn Analysis and Prediction

Analyzed telecom customer data and built Logistic Regression models to predict whether a customer might stay or leave.

# Tools Used
Python, Pandas, Matplotlib, Scikit-learn, and Google Colab.

# Dataset and Data Cleaning
- Started with 1,030 records and 12 columns.
- Removed duplicate rows and the customer ID column.
- Standardized category labels and converted total charges to numeric values.
- Handled missing values and removed records outside the assignment’s allowed ranges.
- Retained 980 records for analysis and modeling.

# Exploratory Analysis
- Overall customer churn was 31.73%.
- Month-to-month customers had 47.45% churn, compared with 12.28% for one-year and 7.10% for two-year contracts.
- Customers who left had average monthly charges of 67.99, compared with 63.88 for those who stayed.
- Average tenure was nearly the same for both groups.

These patterns show associations, not the causes of churn.

# Model Approach
- Used an 80/20 stratified train-test split.
- Learned numeric missing-value replacements and scaling parameters from training data only.
- Evaluated Logistic Regression using accuracy, precision, recall, F1-score, and a confusion matrix.
- Compared a 14-feature model with a five-feature model.

# Evaluation Results

| Approach | Test Accuracy |
|---|---:|
| Always predict Stay | 68.37% |
| Logistic Regression — 14 features | 68.88% |
| Logistic Regression — 5 features | 71.43% |

The five-feature model achieved approximately 58% precision and 35% recall for churn.

# Prediction Demonstration
A final five-feature model was trained on all 980 records for demonstration. It accepts tenure, monthly charges, total charges, senior citizen status, and contract type to produce a Stay or Churn prediction.

The evaluation scores above belong to the held-out test experiments, not this final demonstration model.

# How to Run
1. Download the notebook and CSV dataset from this repository.
2. Open the notebook in Google Colab.
3. Run the upload cell and select the CSV.
4. Ensure the filename in pd.read_csv() matches the uploaded CSV filename.
5. Run the remaining cells in order.
6. Enter customer details when prompted.

# Assumptions and Limitations
- Following the assignment’s convention, missing InternetService entries were treated as no internet service.
- Both model versions were compared on the same test split; further validation is needed.
- The five-feature model missed approximately 65% of actual churners in the test set.
- This is an educational project. No reduction in churn or revenue improvement was measured.
