import streamlit as st
import sklearn, xgboost, pandas, joblib
import os, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor

# Загружаем или обучаем модель
model = get_model()

# Интерфейс Streamlit
st.title("💰 Salary Prediction App")

experience_years = st.number_input("Years of Experience", value=5)
skills_count = st.number_input("Number of Skills", value=3)
certifications = st.number_input("Certifications", value=1)

job_title = st.selectbox("Job Title", ["Data Scientist", "Software Engineer", "Manager"])
education_level = st.selectbox("Education Level", ["Bachelor", "Master", "PhD"])
industry = st.selectbox("Industry", ["IT", "Finance", "Healthcare"])
company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
location = st.selectbox("Location", ["USA", "Europe", "Asia"])
remote_work = st.selectbox("Remote Work", ["Yes", "No"])

input_data = pd.DataFrame([{
    "experience_years": experience_years,
    "skills_count": skills_count,
    "certifications": certifications,
    "job_title": job_title,
    "education_level": education_level,
    "industry": industry,
    "company_size": company_size,
    "location": location,
    "remote_work": remote_work
}])

prediction = model.predict(input_data)[0]
st.success(f"Предсказанная зарплата: ${prediction:,.0f}")

