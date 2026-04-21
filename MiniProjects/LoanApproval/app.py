import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("My ML Classifier")

# Example inputs (change based on your dataset)
feature1 = st.number_input("Enter Feature 1")
feature2 = st.number_input("Enter Feature 2")

if st.button("Predict"):
    input_data = np.array([[feature1, feature2]])
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")


## to run streamlit app write -> streamlit run app.py