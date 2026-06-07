import streamlit as st
import pandas as pd
import numpy as np
import pickle
# Load Churn Model
with open("models/churn_model.pkl", "rb") as f:
    churn_model = pickle.load(f)

# Load KMeans Model
with open("models/kmeans_model.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

# Load Scalers
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("models/segment_scaler.pkl", "rb") as f:
    segment_scaler = pickle.load(f)

st.title("Customer Segmentation & Retention Analysis")

st.write("Predict customer churn and customer segment")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
    )

senior = st.selectbox(
    "Senior Citizen",
    ["Yes", "No"]
)
partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.slider(
    "Tenure Months",
    0,
    72
)

monthly_charges = st.number_input(
    "Monthly Charges"
)

total_charges = st.number_input(
    "Total Charges"
)
phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)


if st.button("Predict"):
    gender_male = 1 if gender=="Male" else 0

    senior_yes = 1 if senior=="Yes" else 0

    partner_yes = 1 if partner=="Yes" else 0

    dependents_yes = 1 if dependents=="Yes" else 0
    input_dict = {

        'Tenure Months':tenure,

        'Monthly Charges':monthly_charges,

        'Total Charges':total_charges,

        'Gender_Male':gender_male,

        'Senior Citizen_Yes':senior_yes,

        'Partner_Yes':partner_yes,

        'Dependents_Yes':dependents_yes,

        'Phone Service_Yes':0,

        'Multiple Lines_No phone service':0,

        'Multiple Lines_Yes':0,

        'Internet Service_Fiber optic':0,

        'Internet Service_No':0,

        'Online Security_No internet service':0,

        'Online Security_Yes':0,

        'Online Backup_No internet service':0,

        'Online Backup_Yes':0,

        'Device Protection_No internet service':0,

        'Device Protection_Yes':0,

        'Tech Support_No internet service':0,

        'Tech Support_Yes':0,

        'Streaming TV_No internet service':0,

        'Streaming TV_Yes':0,

        'Streaming Movies_No internet service':0,

        'Streaming Movies_Yes':0,

        'Contract_One year':0,

        'Contract_Two year':0,

        'Paperless Billing_Yes':0,

        'Payment Method_Credit card (automatic)':0,

        'Payment Method_Electronic check':0,

        'Payment Method_Mailed check':0
            
    } 
       # Phone Service
    if phone_service == "Yes":
        input_dict['Phone Service_Yes'] = 1

    # Multiple Lines
    if multiple_lines == "Yes":
        input_dict['Multiple Lines_Yes'] = 1
    elif multiple_lines == "No phone service":
        input_dict['Multiple Lines_No phone service'] = 1

    # Internet Service
    if internet_service == "Fiber optic":
        input_dict['Internet Service_Fiber optic'] = 1
    elif internet_service == "No":
        input_dict['Internet Service_No'] = 1

    # Online Security
    if online_security == "Yes":
        input_dict['Online Security_Yes'] = 1
    elif online_security == "No internet service":
        input_dict['Online Security_No internet service'] = 1

    # Online Backup
    if online_backup == "Yes":
        input_dict['Online Backup_Yes'] = 1
    elif online_backup == "No internet service":
        input_dict['Online Backup_No internet service'] = 1

    # Device Protection
    if device_protection == "Yes":
        input_dict['Device Protection_Yes'] = 1
    elif device_protection == "No internet service":
        input_dict['Device Protection_No internet service'] = 1

    # Tech Support
    if tech_support == "Yes":
        input_dict['Tech Support_Yes'] = 1
    elif tech_support == "No internet service":
        input_dict['Tech Support_No internet service'] = 1

    # Streaming TV
    if streaming_tv == "Yes":
        input_dict['Streaming TV_Yes'] = 1
    elif streaming_tv == "No internet service":
        input_dict['Streaming TV_No internet service'] = 1

    # Streaming Movies
    if streaming_movies == "Yes":
        input_dict['Streaming Movies_Yes'] = 1
    elif streaming_movies == "No internet service":
        input_dict['Streaming Movies_No internet service'] = 1

    # Contract
    if contract == "One year":
        input_dict['Contract_One year'] = 1
    elif contract == "Two year":
        input_dict['Contract_Two year'] = 1

    # Paperless Billing
    if paperless_billing == "Yes":
        input_dict['Paperless Billing_Yes'] = 1

    # Payment Method
    if payment_method == "Credit card (automatic)":
        input_dict['Payment Method_Credit card (automatic)'] = 1

    elif payment_method == "Electronic check":
        input_dict['Payment Method_Electronic check'] = 1

    elif payment_method == "Mailed check":
        input_dict['Payment Method_Mailed check'] = 1
    input_df = pd.DataFrame([input_dict])
    scaled_input = scaler.transform(input_df)
    prediction = churn_model.predict(scaled_input)

    probability = churn_model.predict_proba(scaled_input)[0][1]
    st.subheader("Churn Prediction")

    if prediction[0] == 1:

        st.error(
            f"Customer is likely to churn.\nProbability = {probability:.2%}"
        )

    else:

        st.success(
            f"Customer is likely to stay.\nProbability = {(1-probability):.2%}"
        )
    segment_df = pd.DataFrame({

        'Tenure Months':[tenure],

        'Monthly Charges':[monthly_charges],

        'Total Charges':[total_charges]

    })
    segment_scaled = segment_scaler.transform(
        segment_df
    )
    cluster = kmeans_model.predict(
        segment_scaled
    )
    cluster_names = {

        0:"High Value Customer",

        1:"Loyal Customer",

        2:"Budget Customer",

        3:"At-Risk Customer"

    }
    st.subheader(
        "Customer Segment"
    )

    st.success(
        cluster_names[cluster[0]]
    )
   






