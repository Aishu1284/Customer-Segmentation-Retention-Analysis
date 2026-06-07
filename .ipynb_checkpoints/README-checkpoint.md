# 🚀 Customer Segmentation & Retention Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>

---

## 📌 Project Overview

Customer retention is one of the most important challenges for businesses. This project combines **Customer Segmentation** and **Churn Prediction** to identify valuable customers and predict which customers are likely to leave.

### 🔥 Key Objectives

* Segment customers into different groups using **K-Means Clustering**
* Predict customer churn using **Machine Learning**
* Identify high-value customers
* Provide actionable business insights
* Build an interactive dashboard using **Streamlit**

---

## 📊 Dataset Information

**Dataset:** Telco Customer Churn Dataset

### Features

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure Months
* Phone Service
* Internet Service
* Contract Type
* Monthly Charges
* Total Charges
* Payment Method
* and many more...

---

# ⚙️ Machine Learning Pipeline

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis (EDA)
     ↓
Feature Engineering
     ↓
Customer Segmentation (K-Means)
     ↓
Churn Prediction
(Logistic Regression, Decision Tree, Random Forest, XGBoost)
     ↓
Model Evaluation
     ↓
Streamlit Dashboard
     ↓
Deployment
```

---

# 🛠 Technologies Used

| Category         | Tools                 |
| ---------------- | --------------------- |
| Language         | Python                |
| Data Analysis    | Pandas, NumPy         |
| Visualization    | Matplotlib, Seaborn   |
| Machine Learning | Scikit-Learn, XGBoost |
| Clustering       | K-Means               |
| Deployment       | Streamlit             |
| Version Control  | Git & GitHub          |

---

# 📈 Exploratory Data Analysis

✔ Customer Churn Distribution

✔ Contract Type Analysis

✔ Monthly Charges Analysis

✔ Tenure Analysis

✔ Correlation Heatmap

✔ Feature Relationships

---

# 🤖 Models Used

## Customer Segmentation

* K-Means Clustering

---

## Churn Prediction Models

* Logistic Regression ✅
* Decision Tree
* Random Forest
* XGBoost

---

# 🏆 Best Model Performance

### Logistic Regression

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 79.99% |
| Precision | 63.77% |
| Recall    | 56.95% |
| F1 Score  | 60.17% |
| ROC-AUC   | 84.86% |

---

# 📌 Confusion Matrix

```text
[[914 121]
 [161 213]]
```

* True Negatives (TN): 914
* False Positives (FP): 121
* False Negatives (FN): 161
* True Positives (TP): 213

---

# 📂 Project Structure

```text
Customer_Segmentation_Retention_Analysis

│
├── data
│
├── models
│     churn_model.pkl
│     kmeans_model.pkl
│     scaler.pkl
│     segment_scaler.pkl
│
├── notebooks
│     01_data_cleaning.ipynb
│     02_eda.ipynb
│     03_feature_engineering.ipynb
│     04_customer_segmentation.ipynb
│     05_churn_prediction.ipynb
│     06_model_evaluation.ipynb
│
├── app.py
├── requirements.txt
├── README.md
```

---

# 🌟 Streamlit Dashboard Features

✅ Customer Churn Prediction

✅ Churn Probability Score

✅ Customer Segmentation

✅ High Value Customer Identification

✅ Interactive User Interface

---

# 📷 Sample Output

### Churn Prediction

```
Customer is likely to churn.
Probability = 82.90%
```

### Customer Segment

```
High Value Customer
```

---

# 💡 Business Insights

* Customers with month-to-month contracts are more likely to churn.
* Customers with shorter tenure have higher churn probability.
* High monthly charges increase churn risk.
* High-value customers can also be at risk of leaving.

---

# 🚀 Future Enhancements

* Hyperparameter Tuning (GridSearchCV)
* SHAP Explainability
* Feature Importance Dashboard
* Docker Deployment
* AWS Deployment
* Power BI Integration

---

# 👨‍💻 Author

**Shubham Kumar**

MCA, NIT Raipur

Machine Learning | Data Science | Python

---

⭐ If you found this project useful, please consider giving it a star!
