import streamlit as st
import sklearn, xgboost, pandas, joblib

st.title("Тест окружения")
st.write("scikit-learn:", sklearn.__version__)
st.write("xgboost:", xgboost.__version__)
st.write("pandas:", pandas.__version__)
st.write("joblib:", joblib.__version__)
st.write("streamlit:", st.__version__)
